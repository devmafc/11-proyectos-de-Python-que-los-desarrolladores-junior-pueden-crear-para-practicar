#Contador de palabras

#Preguntamos al usuario en que está pensando. Cuando se introduce la respuesta, 
#realizará el conteo de palabras en la sentencia e imprimimos en la salida el resultado.
print('\n')
print('¡ Bienvenido al contador de palabras !')
print('\n')
print('Escoja la opción meidante la cual desea contar palabras ')
print('1. Ingresar texto mediante teclado \n2. Ingresar ruta del archivo .txt')
print('\n')

lista = []
contador = 0

while True:
    try:
        respuesta = int(input('>>>  '))
    except:
        print('Solo se aceptan  las respuestas númericas indicadas en el menú')
        continue
    if respuesta == 1:
        texto = input('A continuación escriba el texto: ')
        lista = texto.split()
        print('El texto que has ingresa contiene ', len(lista), 'palabra(s)')
        respuesta2 = input('¿ Desea utilizar el programa contador de palabras nuevamente ( si / no ) ')
        respuesta2 = respuesta2.lower()
        if respuesta2 == 'si':
            continue
        elif respuesta2 == 'no':
            print('¡ Adios !')
            break
        else:
            print('Ingreso una respuesta diferente a ( si / no )')
            break
    elif respuesta == 2:
        rut = input('Ingrese ruta del archivo: ')
        try:
            ruta = open(rut)
        except:
            print('Archivo no existente')
            continue
        for linea in ruta :
            linea = linea.split()
            total = len(linea)
            contador = contador + total
        print('Su archivo ',rut,' contiene ', contador, 'palabra(s)')
        respuesta3 = input('¿ Desea utilizar el programa contador de palabras nuevamente ( si / no ) ')
        respuesta3 = respuesta3.lower()
        if respuesta3 == 'si':
            continue
        elif respuesta3 == 'no':
            print('¡ Adios !')
            break
        else:
            print('Ingreso una respuesta diferente a ( si / no )')
            break
    else:
        print('opcion fuera de margen \n ¡ Adios !')
        break