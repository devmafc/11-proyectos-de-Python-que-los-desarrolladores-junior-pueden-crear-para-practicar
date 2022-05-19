import re
"""
	Usar expresiones regulares para ver si es un correo electrónico válido en Python
	Recuerda importar el módulo re
	Por cierto, está probado con Python 3, si usas la versión 2 y no funciona, no trates
	de adaptarlo, mejor actualiza tu versión
	@author parzibyte
"""
 
 
def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

# Probamos con algunos correos
correos = [
    "hola@", "contacto@parzibyte.me", "staff@hotmail.com",
    "juan.perez@sitio.com", "maggie@outlook.com", "parzibyte@gmail.com", "asd",
    "luis@gmail@hotmail.com"
]
 
for correo in correos:
    print("Probando si '{}' es válido...{}".format(correo,
                                                   es_correo_valido(correo)))