#------------------------------------------Practica---------------------------------------

#Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000
#Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado

print('\n')
print('Bienvenido al juego Par o Impar \nPor favor Ingrese un número del 1 al 1000')
print('\n')
while True:
    try:
        numero = float(input('¿En que número estás pensando:  '))
    except:
        print('Ingrese solo números')
        continue
    if numero < 1 or numero > 1000 :
        print('Número fuera de rango')
        break
    elif numero % 2 != 0 :
        print('Número impar')
        next = input('¿Quieres añadir otro número? ')
        next = next.lower()
        if next == 'si' :
            continue
        elif next == 'no':
            print('¡ Adios !')
            break
        else:
            print('Ingresaste una respuesta diferente a si o no.')
            break
    else:
        print('Número par')
        next_2 = input('¿Quieres añadir otro número? ')
        next_2 = next_2.lower()
        if next_2 == 'si' :
            continue
        elif next_2 == 'no':
            print('¡ Adios !')
            break
        else:
            print('Ingresaste una respuesta diferente a si o no')
            break
