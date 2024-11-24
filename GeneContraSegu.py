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
while bandera1 == True: # Se utiliza una bandera para cuando el ingreso del dato sea correcto slaga del bulce y continue con el resto del código
    try: # Se utiliza try y except para manejar excepciones en caso de que el usuario pueda introducir un dato no solicitado
        dato = input("Ingrese la longitud deseada de la contraseña a generar, en valor numérico entero del 8 - 30: ")
        longitud = int(dato) # En caso de no poder convertir este dato a entero, se manejara con el except
        if 8 <= longitud <= 30: # Se verifica que el ingreso del entero sea entre los valores de 8 a 30, para el establecimiento de una contraseña bastante segura
            bandera1 = False # En el caso de que el dato ingresado sea correcto la bandera se apaga y esto permite salir del bucle continuando con el programa
        else:
            print("Por favor ingrese un número entre el 8 y 30.")
    except ValueError:
        print("No se ha ingresado un caracter numérico entero!")
# Este es el 25% del software
# Hasta Aquí todo Perfecto!!
# Nos quedamos en el Paso 2. Empezar el paso 3
print("Ha salido correctamente del bucle y la longitud es", longitud, ", El cual es un valor correcto!")