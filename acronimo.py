#---------------Programa de Acronimos-------------------
#Vamos a pedir al usuario que ingrese el significado completo de una organización o concepto
#y con ello como resultado obtendremos el acrónimo

while True:
    frase = input('Ingrese frase que quiera convertir en acronimo:  \n').lower()
    if frase == 'fin':
        break

    cadena = frase.split()          # divide la frase que ingresa por palabras
    salida = "" 

    for word in cadena:             # itera sobre la frase ya dividida en palabras
        salida += word[0]           # a medida de la variable de iteracion itera sobre cada palabra toma la posicion 0 y la agrega a la variable salida


    salida = salida.upper() 
    print(salida )
    solicitud = input('¿Desea generar otro acronimo? ( si/no ) ').lower()
    if solicitud == 'si':
        continue
    elif solicitud == 'no':
        break
    else:
        print('Ingresaste una respuesta diferente')
        break

    



