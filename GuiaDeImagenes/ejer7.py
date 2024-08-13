from PIL import Image

def filter():
    ruta_foto = input("ingrese la ruta de la foto: ")
    foto = Image.open(ruta_foto)
    foto.show()

with Image.open(ruta_foto) as img:
    nue_foto = img.convert('L')

    nue_foto.save = (ruta_foto)
