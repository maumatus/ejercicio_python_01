file = open(r"/Users/mauricio/Desktop/prueba_escritura_python.txt ", "w+")

"""este codigo reemplaza letras por numeros"""

user_story = input("cuentame una historia")

nuevo_texto = user_story.replace("a", "4")
nuevo_texto = nuevo_texto.replace("b", "8")
nuevo_texto = nuevo_texto.replace("e", "3")
nuevo_texto = nuevo_texto.replace("l", "1")
nuevo_texto = nuevo_texto.replace("o", "0")
nuevo_texto = nuevo_texto.replace("s", "5")
nuevo_texto = nuevo_texto.replace("t", "7")

L = nuevo_texto

L = ["Esto es una prueba escritura \n","Pewi esta pintando \n","Con acuarelas nuevas \n"]
# \n is placed to indicate EOL (End of Line)
file.writelines(L)
file.close()