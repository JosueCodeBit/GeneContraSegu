# Importación de Librerías
import random
import string

# Definición de Variables
bandera1 = True
longitud = int 

# Solicitud y Validación de la Longitud de la Contraseña a Generar
print("---------------Generador de Contraseñas Seguras---------------")
print("--------------------------Bienvenido--------------------------")
# Bucle While para validar la longitud que el usuario pueda ingresar
while bandera1 == True:  # Se utiliza una bandera para cuando el ingreso del dato sea correcto salga del bucle y continue con el resto del código
    try:  # Se utiliza try y except para manejar excepciones en caso de que el usuario pueda introducir un dato no solicitado
        dato = input("Ingrese la longitud deseada de la contraseña a generar, en valor numérico entero del 8 - 30: ")
        longitud = int(dato)  # En caso de no poder convertir este dato a entero, se manejará con el except
        if 8 <= longitud <= 30:  # Se verifica que el ingreso del entero sea entre los valores de 8 a 30
            bandera1 = False  # En el caso de que el dato ingresado sea correcto, la bandera se apaga y esto permite salir del bucle
        else:
            print("Por favor ingrese un número entre 8 y 30.")
    except ValueError:
        print("¡No se ha ingresado un caracter numérico entero!")

# Conjunto de caracteres disponibles para generar la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation  # Conjunto de caracteres (letras, dígitos y símbolos) que se utilizarán

# Bucle para generar y verificar la contraseña
while True:
    # Uso de la lista de compresión para crear la contraseña
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))  # Generación de la contraseña

    # Verificación de que la contraseña tenga al menos una letra, un dígito y un símbolo
    tiene_letra = False
    tiene_digito = False
    tiene_simbolo = False

    for c in contraseña:
        if c.isalpha():  # Verificar si el carácter es una letra
            tiene_letra = True
        if c.isdigit():  # Verificar si el carácter es un dígito
            tiene_digito = True
        if c in string.punctuation:  # Verificar si el carácter es un símbolo
            tiene_simbolo = True

    # Si la contraseña cumple con los 3 requisitos, salir del bucle
    if tiene_letra and tiene_digito and tiene_simbolo:
        break  # La contraseña es válida, salimos del bucle

    else:
        print("La contraseña generada no cumple con los requisitos de tener letras, números y símbolos. Generando una nueva...")

# Impresión de la Contraseña Generada
print(f"Tu contraseña segura es: {contraseña}")

# Fin del Programa 
print("--------------------Gracias por usar el Generador de Contraseñas Seguras--------------------")
