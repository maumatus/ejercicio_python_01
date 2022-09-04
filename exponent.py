#Este programa pregunta un numero, luego un exponente y devuelve el resultado.
#esta version solo es para numeros enteros

print("Bienvenido a la calculadora de exponente de Python V 1.0")

base = int(input("ingresa un numero base"))

exponente = int(input("ingresa un exponente"))

resultado = base ** exponente

respuesta = f"{base} elevado a {exponente} es igual a {resultado}"

print(respuesta)



