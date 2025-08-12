from tkinter import Tk, Canvas,Button
from PIL import Image, ImageTk

ventana = Tk()
ventana.title= ("Bienvenidos al zoologico")
ventana.geometry("400x400")

#agregar fondo
#abrir imagen
imagen = Image.open("zoologico.jpg")
imagen = imagen.resize ((400,400))
imagen_tk = ImageTk.PhotoImage(imagen)

# canva
canva = Canvas(ventana, width=600, height=800)
canva.pack(fill="both")
canva.create_image(0,0,image = imagen_tk, anchor = "nw")

imagen1 = Image.open("boton_lobo.png")
imagen1= imagen1.resize((50,50))
imagen1_tk= ImageTk.PhotoImage(imagen1)

boton1= Button(ventana, image=imagen1_tk, borderwidth=0)
boton1.place(x=150,y=230)



ventana.mainloop()