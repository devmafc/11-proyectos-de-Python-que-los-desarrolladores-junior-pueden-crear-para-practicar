#-----------------MAD LIB------------------

#Pedimos al usuario que introduzca varias entradas con varias preguntas.
#Puede ser cualquier cosa, como un nombre, un adjetivo, un pronombre o incluso una acción. Una vez que se obtiene la entrada, se puede reorganizar para construir su propia historia.


import os
from time import sleep
print('\n')
print('Bienvenido a su version de Rinrín renacuajo \nPor favor responda las siguientes preguntas')
print('\n')


nombre = input('Escriba un nombre: ')
prenda = input('Escriba una prenda de vestir: ')
frase_mama = input('¡ Frase de tú mamá ! ')
animal = input('Escriba un animal: ')
parentesco = input('Escriba un parentesco: ')
sleep(2)
os.system('cls')



print('Su version de Rinrin renacuajo')
print('\n')
print('El hijo de ', nombre, 'Rinrín renacuajo \nSalió esta mañana muy tieso y muy majo\nCon', prenda, 'corbata a la moda\nSombrero encintado y chupa de boda')
print('-¡ ',frase_mama,'!- le grita mamá \npero él hace un gesto y orondo se va.')
print('Halló en el camino, a un ' ,animal,' vecino \nY le dijo: -¡ ',parentesco,'!- venga usted conmigo,\nVisitemos juntos a doña ratona \nY habrá francachela y habrá comilona.')
print('\n')
