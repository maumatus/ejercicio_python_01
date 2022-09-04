# renombrador de archivos por lote
# cambia el nombre dentro de la misma carpeta contenedora
import os

def main():
    i = 0
    # Aqui definimos la ruta/carpeta de las imagenes a ser renombradas
    path = "/Users/mauricio/Desktop/prueba/"
    for filename in os.listdir(path):
        my_dest = "sec_a_" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1
if __name__ =='__main__':
    main()
