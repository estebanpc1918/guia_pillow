from PIL import Image, ImageColor
import os

def img():
    ruta_foto = input("ingrese la ruta de la foto: ")
    foto = Image.open(ruta_foto)
    foto.show()
    
    nombre_foto = os.path.basename(ruta_foto)
    print(f"nombre: {nombre_foto}")
    print(f"extension: {foto.format}")
    width, height = foto.size
    pixeles_total = width * height
    print(f"resolucion: {width}x{height}")
    width, height = foto.size
    pixeles_total = width * height
    print(f"cantidad de pixeles es de: {pixeles_total}")
    print(f"ruta: {foto.filename}")
    

img()

