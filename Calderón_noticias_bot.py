import telegram
import requests
from bs4 import BeautifulSoup
import os
import asyncio

TOKEN = '8380191817:AAEOK6-wp5qYo1adbCQW5yEP4c-krZcBxGY'  
ID_de_usuario = -1002271840069  
URL_BBC_Mundo = 'https://www.bbc.com/mundo/'  
Ultimo_Post_registrado = 'calde_noticias.txt'  

bot = telegram.Bot(token=TOKEN)

def obtener_ultima_noticia():
    if os.path.exists(Ultimo_Post_registrado):
        with open(Ultimo_Post_registrado, 'r') as f:
            return f.read().strip()
    return None

def guardar_ultima_noticia(enlace):
    with open(Ultimo_Post_registrado, 'w') as f:
        f.write(enlace)

def obtener_noticias():
    print("Obteniendo las noticias de BBC Mundo...")
    
    respuesta = requests.get(URL_BBC_Mundo)
    if respuesta.status_code != 200:
        print(f"Error al obtener la página, código de estado: {respuesta.status_code}")
        return []

    extraer_html = BeautifulSoup(respuesta.text, 'html.parser')
    
    noticias = []
    for item in extraer_html.find_all('a', href=True):
        enlace = item['href']
        if '/mundo/articles/' in enlace:
            titular = item.get_text(strip=True)
            if not enlace.startswith('http'):
                enlace = 'https://www.bbc.com' + enlace
            noticias.append((titular, enlace))

    print("Noticias extraídas:")
    for titular, enlace in noticias:
        print(f"{titular}: {enlace}")

    return noticias

async def procesar_noticias():
    noticias = obtener_noticias()
    
    if not noticias:
        print("No se encontraron noticias.")
        return

    ultimo_titular = obtener_ultima_noticia()
    noticias_nuevas = []

    for titular, enlace in noticias:
        if enlace == ultimo_titular:
            break
        noticias_nuevas.append((titular, enlace))

    if not noticias_nuevas and noticias[0][1] != ultimo_titular:
        print("El último titular guardado no se encuentra en las noticias. Reiniciando...")
        guardar_ultima_noticia(noticias[0][1])
        return

    for titular, enlace in reversed(noticias_nuevas):
        print(f"Enviando noticia: {titular} - {enlace}")
        message = f"📰 *{titular}*\n\n[Leer más]({enlace})"
        try:
            await bot.send_message(
                chat_id=ID_de_usuario,
                text=message,
                parse_mode='Markdown',  
                disable_web_page_preview=True  
            )
            print(f"Noticia enviada al bot: {titular}")
            await asyncio.sleep(2)  
        except Exception as e:
            print(f"Error al enviar el mensaje: {e}")

    if noticias_nuevas:
        guardar_ultima_noticia(noticias_nuevas[0][1])
        print(f"Último titular guardado: {noticias_nuevas[0][1]}")
    else:
        print("No hay noticias nuevas.")

if __name__ == '__main__':
    asyncio.run(procesar_noticias())
