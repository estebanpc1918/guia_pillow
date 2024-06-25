from PIL import Image
import os

def rotacion_img():
    #carga de imagen y de angulo
    ruta_foto = input('ingrese la ruta de la foto: ')
    foto_original = Image.open(ruta_foto)
    rotar_foto = int(input('ingrese el el angulo de rotacion de la foto: '))


    #copia de la imagen
    foto_rotada = foto_original.rotate(rotar_foto, expand= False)

    foto_rotada.save("nombreArchivoOriginalRot.extOriginal.jpg")
    
    foto_rotada.show()
rotacion_img()



