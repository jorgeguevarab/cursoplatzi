def convertir(moneda,factor,tipo):

    # valor1 = float(input("Valor en {} ".format(moneda)))
    valor1 = float(moneda)

    if tipo == 1:
        resultado = round((valor1 * factor),2)
    elif tipo == 2:
        resultado = round((valor1 / factor),2)
    else:
        print("No value selected")
    
    # print("{} {} equivalen a {} {}".format(str(valor1),moneda1,str(resultado), moneda2))

    return resultado


def mensaje(valor, resultado, m1, m2):
    print("{} {} equivalen a {} {}".format(str(valor),m1,str(resultado), m2))


def espalindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.upper()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
