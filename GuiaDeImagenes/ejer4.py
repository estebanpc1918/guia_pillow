from PIL import Image
import os

def recortar_imagen():
    # Solicitar nombre de la imagen
    nombre_imagen = input("Ingrese el nombre de la imagen (incluyendo la extensión): ")
    
    # Verificar si la imagen existe
    if not os.path.exists(nombre_imagen):
        print("Error: La imagen especificada no existe.")
        return

    try:
        # Abrir la imagen
        imagen = Image.open(nombre_imagen)
        
        # Obtener dimensiones de la imagen original
        ancho_original, alto_original = imagen.size
        
        # Solicitar coordenadas iniciales
        x = int(input("Ingrese la coordenada X inicial para el recorte: "))
        y = int(input("Ingrese la coordenada Y inicial para el recorte: "))
        
        # Solicitar ancho y alto del recorte
        ancho = int(input("Ingrese el ancho del recorte: "))
        alto = int(input("Ingrese el alto del recorte: "))
        
        # Verificar si los parámetros son válidos
        if x < 0 or y < 0 or x + ancho > ancho_original or y + alto > alto_original:
            print("Error: Los parámetros de recorte exceden los límites de la imagen original.")
            return
        
        # Realizar el recorte
        imagen_recortada = imagen.crop((x, y, x + ancho, y + alto))
        
        # Generar nombre para la imagen recortada
        nombre_base, extension = os.path.splitext(nombre_imagen)
        nombre_recorte = f"{nombre_base}_recortada{extension}"
        
        # Guardar la imagen recortada
        imagen_recortada.save(nombre_recorte)
        print(f"La imagen recortada se ha guardado como: {nombre_recorte}")
        
    except IOError:
        print("Error: No se pudo abrir la imagen.")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos para las coordenadas, ancho y alto.")

# Ejecutar la función
recortar_imagen()