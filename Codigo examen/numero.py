"""
Módulo que agrupa todas las funcionalidades
que permiten solicitar introducir un dato numérico
"""


import sys


MIN=0
MAX=100

##### Hay que modificar los maximos y minimos dependiendo de lo que nos pida el ejercicio.

def solicitar_introducir_numero(invite):
    """
    Esta función verifica que tenemos un número
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end=": ")
        datoIntroducido = input()

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            print("Solo están autorizados los caracteres [0-9].", file=sys.stderr)
            
            ##### El sys.stderr almacena los datos introducidos en el input previo.
            ##### Hay que cambiar el [0-9] si tambien cambiamos los numeros maximos que se pueden meter.
        else:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido

def solicitar_introducir_numero_extremo(invite, minimum=MIN, maximum=MAX):
    """
    Esta función utiliza el anterior y añade una post-condición
    sobre los extremos del número a introducir
    """
    invite = "{} entre {} y {} incluídos".format(invite, minimum, maximum)
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        datoIntroducido = solicitar_introducir_numero(invite)

        if minimum <= datoIntroducido <= maximum:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido