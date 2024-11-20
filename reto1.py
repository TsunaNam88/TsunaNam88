"""
Desarrollo de una aplicacion que envie un mensaje recordatorio 
para devolver un libro

Esta funcion solicita los datos del usuario, valida el formato de la fecha
y crea un mensaje recordatorio personalizado.

Args:
    nombre (str)
    titulo_dellibro (str)
    fecha_de_vencimiento (str)
Returns:
    str: mensaje de recordatorio
Raises: 
    ValueError: si la fecha no esta en el formato
"""
from datetime import datetime
    
def generar_recordatorio(nombre, titulo_del_libro, fecha_de_vencimiento):
    try:
        fecha = datetime.strptime(fecha_de_vencimiento, '%d/%m/%Y')
        mensaje_fecha = (f", antes del {fecha.day} de {fecha.month} de {fecha.year}")
    except ValueError as e:
        print(f"Error: {e}, introduzca una fecha valida de modo (DD/MM/AAAA)")
        return None
    mensaje = (
        f"Hola {nombre}, recuerda devolver el libro '{titulo_del_libro}'{mensaje_fecha}")
    return mensaje

nombre = input("¿Cual es tu nombre: ")
titulo_del_libro = input("A continuacion, indique el titulo del libro: ")
fecha_de_vencimiento = input(
    "Finalmente, indique la fecha de vencimiento (DD/MM/AAAA): "
)
# Llamando a la funcion generar_recordatorio
recordatorio = generar_recordatorio(nombre, titulo_del_libro, fecha_de_vencimiento)
print(recordatorio)

