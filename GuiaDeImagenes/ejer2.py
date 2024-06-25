from PIL import Image
import os

def guardar_img():
    ruta_foto = input('ingrese la ruta de la foto: ')
    foto_original = Image.open(ruta_foto)
    foto_original.show()

    foto_copy = foto_original.copy()

    nombre_ft = 'perro_copia.jpg'

    ruta_copia = os.path.join(os.getcwd(), nombre_ft)

    foto_copy.save(ruta_copia)
    print('la copia se guardo perfectamente!!')

guardar_img()