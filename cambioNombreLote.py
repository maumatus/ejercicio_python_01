#Herramienta Python para cambio nombre archivos por lote
#Funciona en un directorio o carpeta

#importar modulo OS, es base para funcionamiento script

import os

# Funcion para renombrar multiples archivos

def main():

    for count, filename in enumerate(os.listdir('/Users/mauricio/Volumes/SSD_02/Desarrollos_MotionGraphics/Render02')):
        dst = "cubo" + str(count) + ".png"
        src = "mauricio/Volumes/SSD_02/Desarrollos_MotionGraphics/Render02" + filename
        dst = "mauricio/Volumes/SSD_02/Desarrollos_MotionGraphics/Render02b" + dst

        #rename() function will
        #rename all the files
        os.rename(src, dst)

#Driver code

if __name__ == '__main__':

    #calling main() function
    main()