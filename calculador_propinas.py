# Prorgrama que calcula la propina en base a si el cliente quiere dar el 100%
# o si quiere dividir la propina entre los comensales
from time import sleep
import os
print('\n')
print('Restaurante Python')
while True:
    try:
        factura = float(input('Indique el valor total de la factura: '))
    except:
        print('Solo valores númericos')
        continue
    print(factura,'\n')
    print('¿Desea dividir la factura de forma equitativa? ( si/no )')
    respuesta = input('>>> ').lower()
    if respuesta == 'si':
        try:
            clientes = int(input('¿número de personas: ?'))
        except:
            print('Solo valores númericos')
            sleep(2)
            os.system('cls')
            continue
        print('En base al servicio recibido indique el porcentaje que quiere dar: ')
        try:
            porcentaje = float(input('>>> '))
        except:
            print('Solo valores númericos')
            sleep(2)
            os.system('cls')
            continue
        propina = factura * porcentaje / 100
        print('Total factura: ',factura, 'porcentaje selecionado ',porcentaje, '= ',round(propina,2))
        print('Total propina: ',round(propina,2))
        print('Total por cliente = ', round(round(propina,2)/clientes),2)
        break
    elif respuesta == 'no':
        print('En base al servicio recibido indique el porcentaje que quiere dar: ')
        try:
            porcentaje = float(input('>>> '))
        except:
            print('Solo valores númericos')
            sleep(2)
            os.system('cls')
            continue
        propina = factura * porcentaje / 100
        print('Total factura: ',factura, 'porcentaje selecionado ',porcentaje, '= ',round(propina,2))
        print('Total propina: ',round(propina,2))
        break
    else:
        print('Ingrese solo las opciones dadas')
        sleep(2)
        os.system('cls')
        continue