from PIL import Image
import os, sys

print('CON ESTE PROGRAMA PODRAS AGREGAR MARCA DE AGUA A TUS IMAGENES')
print('-------------------------------------------------------------')

print('Ingrese la ruta de la imagen')
ruta = input('-->')
img = Image.open(ruta)

print('Ingrese la ruta de la marca de agua')
ruta_marca = input('-->')
marca_agua = Image.open(ruta_marca)

margen = 50

print('Seleccione donde quiere que vaya la marca de agua')
print('Escriba 1, 2, 3 o 4')
print('\t1_Superior izquierda')
print('\t2_Superior derecha')
print('\t3_Inferior izquierda')
print('\t4_Inferior derecha')
ubicacion = input()

if ubicacion not in ['1', '2', '3', '4']:
    sys.exit('++Error: Usted debía ingresar 1, 2, 3 o 4++')
else:
    image_new = img.copy()

    
    if marca_agua.mode != 'RGBA':
        marca_agua = marca_agua.convert('RGBA')

    alpha_mask = marca_agua.split()[3]

    if ubicacion == '1':
        image_new.paste(marca_agua, (margen, margen), mask=alpha_mask)
    elif ubicacion == '2':
        pos_x = img.width - marca_agua.width - margen
        image_new.paste(marca_agua, (pos_x, margen), mask=alpha_mask)
    elif ubicacion == '3':
        pos_y = img.height - marca_agua.height - margen
        image_new.paste(marca_agua, (margen, pos_y), mask=alpha_mask)
    else:
        pos_x = img.width - marca_agua.width - margen
        pos_y = img.height - marca_agua.height - margen
        image_new.paste(marca_agua, (pos_x, pos_y), mask=alpha_mask)

    ruta_salida = 'Manipulacion de imagenes/imagenes-recortes/imagen_con_marca_de_agua.png'
    image_new.save(ruta_salida)
    print(f'La imagen con marca de agua ha sido guardada como {ruta_salida}')


    image_new.show()
