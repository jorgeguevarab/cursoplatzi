from funciones import espalindromo


def run():
    texto = input('Escribe la palabra a evaluar: ')
    print(str(espalindromo(texto)))

#Entry point
if __name__ == '__main__':
    run()
