from funciones import espalindromo


def run():
    texto = input('Escribe la palabra a evaluar: ')
    print(str(espalindromo(texto)))


if __name__ == '__main__':
    run()
