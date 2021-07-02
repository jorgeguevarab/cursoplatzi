
from datetime import date

#ES Almacenamos la fecha actual en la variable hoy con formato de fecha larga 
#EN Declare variable "hoy" for store current date with large format
hoy = date.today().strftime("%A %d de %B de %y")

#ES Declaramos e inicializamos variables donde almacenaremos los tipos de moneda
#EN Declare and set currency names
moneda1 = "USD"
moneda2 = "COP"

print('''
******Convertidor de monedas*******
***********************************
Fecha: {}
Moneda 1: {}
Moneda 2: {}

'''.format(hoy, moneda1, moneda2))

#ES Capturamos el factor de conversión de la moneda
#EN Capture conversion factor among currencies
factorconv = float(input("1 {} equivale en {} a: ".format(moneda1, moneda2)))

#ES Imprimimos el menú de opciones
#EN Print options menu and input 
print("""

=== Selecciona una de las siguientes opciones ===
    (1) Para convertir de {} a {}
    (2) Para convertir de {} a {}
*************************************************    
""".format(moneda1, moneda2, moneda2, moneda1))

opcion = int(input("Escribe una de las opciones: "))


if opcion == 1:
    valor1 = float(input("Valor en {} ".format(moneda1)))
    resultado = round((valor1 * factorconv),2)
    print("{} {} equivalen a {} {}".format(str(valor1),moneda1,str(resultado), moneda2))
else:
    if opcion == 2:
        valor1 = float(input("Valor en {} ".format(moneda2)))
        resultado = round((valor1 / factorconv),2)
        print("{} {} equivalen a {} {}".format(str(valor1),moneda2,str(resultado), moneda1))
    else:
        print("No seleccionaste una opción válida. Vuelve a iniciar")


        






    


