#inicio

#este codigo lee archivo txt desde directorio indicado
file = open(r"/Users/mauricio/Desktop/traductor_loco.txt ", "w")

# este codigo reemplaza letras por numeros, cuerpo funcional del traductor

user_story = input("cuentame una historia")

nuevo_texto = user_story.replace("a", "4")
nuevo_texto = nuevo_texto.replace("b", "8")
nuevo_texto = nuevo_texto.replace("e", "3")
nuevo_texto = nuevo_texto.replace("l", "1")
nuevo_texto = nuevo_texto.replace("o", "0")
nuevo_texto = nuevo_texto.replace("s", "5")
nuevo_texto = nuevo_texto.replace("t", "7")

#traspaso de datos de conversion a variable "L"
L = nuevo_texto

# escribe resultados a archivo .txt sin formato
file.writelines(L)
file.close()

#Fin