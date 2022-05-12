from random import randint
import os


print('\n')
print('Bienvenido al juego ¡ Piedra Papel o Tijera \nTu openente sera el COMPUTADOR !')
print('\n')


contador_computador = 0
contador_jugador = 0
contador_empate = 0

while True:
    choice = ['piedra', 'papel','tijeras']
    computer = choice[randint(0,2)]
    print('¡ piedra papel o tijeras !')
    jugador = input('>>> ').lower()
    if jugador == computer:
        print('Computador: ',computer, 'Jugador: ',jugador)
        print('¡ Empate !')
        contador_empate += 1
        revancha = input('¿Desea volver a jugar? ')
        if revancha == 'si':
            continue
        elif revancha == 'no':
            os.system('cls')
            print('Total puntuación: ', '\nComputador: ',contador_computador, 'Jugador: ', contador_jugador, 'Empate: ', contador_empate)
            break
        else:
            print('Has realizado una eleccion diferente')
            break
    elif jugador == 'piedra' and computer == 'papel':
        print('Computador: ',computer, 'Jugador: ',jugador)
        print('¡ Has perdido!')
        contador_computador += 1
        revancha = input('¿Desea volver a jugar? ')
        if revancha == 'si':
            continue
        elif revancha == 'no':
            os.system('cls')
            print('Total puntuación: ', 'Computador: ',contador_computador, 'Jugador: ', contador_jugador, 'Empate: ', contador_empate)
            break
        else:
            print('Has realizado una eleccion diferente')
            break
    elif jugador == 'piedra' and computer == 'tijeras':
        print('Computador: ',computer, 'Jugador: ',jugador)
        print('¡ Has ganado !')
        contador_jugador += 1
        revancha = input('¿Desea volver a jugar? ')
        if revancha == 'si':
            continue
        elif revancha == 'no':
            os.system('cls')
            print('Total puntuación: ', 'Computador: ',contador_computador, 'Jugador: ', contador_jugador, 'Empate: ', contador_empate)
            break
        else:
            print('Has realizado una eleccion diferente')
            break
    elif jugador == 'papel'and computer == 'piedra':
        print('Computador: ',computer, 'Jugador: ',jugador)
        print('¡ Has ganado !')
        contador_jugador += 1
        revancha = input('¿Desea volver a jugar? ')
        if revancha == 'si':
            continue
        elif revancha == 'no':
            os.system('cls')
            print('Total puntuación: ', 'Computador: ',contador_computador, 'Jugador: ', contador_jugador, 'Empate: ', contador_empate)
            break
        else:
            print('Has realizado una eleccion diferente')
            break
    elif jugador == 'papel' and computer == 'tijeras' :
        print('Computador: ',computer, 'Jugador: ',jugador)
        print('¡ Has perdido !')
        contador_computador += 1
        revancha = input('¿Desea volver a jugar? ')
        if revancha == 'si':
            continue
        elif revancha == 'no':
            os.system('cls')
            print('Total puntuación: ', 'Computador: ',contador_computador, 'Jugador: ', contador_jugador, 'Empate: ', contador_empate)
            break
        else:
            print('Has realizado una eleccion diferente')
            break
    elif jugador == 'tijeras' and computer == 'piedra' :
        print('Computador: ',computer, 'Jugador: ',jugador)
        print('U+1F636¡ Has perdido')
        contador_computador += 1
        revancha = input('¿Desea volver a jugar? ')
        if revancha == 'si':
            continue
        elif revancha == 'no':
            os.system('cls')
            print('Total puntuación: ', 'Computador: ',contador_computador, 'Jugador: ', contador_jugador, 'Empate: ', contador_empate)
            break
        else:
            print('Has realizado una eleccion diferente')
            break
    elif jugador == 'tijeras' and computer == 'papel':
        print('Computador: ',computer, 'Jugador: ',jugador)
        print('¡ Has ganado !')
        contador_jugador += 1
        revancha = input('¿Desea volver a jugar? ')
        if revancha == 'si':
            continue
        elif revancha == 'no':
            os.system('cls')
            print('Total puntuación: ', 'Computador: ',contador_computador, 'Jugador: ', contador_jugador, 'Empate: ', contador_empate)
            break
        else:
            print('Has realizado una eleccion diferente')
            break
    else:
        print('Has realizado una eleccion diferente')
        continue

print('linea de prueba para git')





