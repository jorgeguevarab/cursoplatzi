import random, string

def generar_contrasena(numero_caracteres):
    # mayusculas = string.ascii_uppercase
    # minusculas = string.ascii_lowercase
    # numeros = string.digits
    # simbolos = string.punctuation
    # temporal = mayusculas + minusculas + numeros + simbolos
    # sizetemporal = len(temporal)
    # temporal = string.printable
    temporal = string.ascii_letters + string.digits + string.punctuation
    final = ''
    
    for i in range(numero_caracteres):
        # aleatorio = random.randint(0,len(temporal)-1)
        # final = final + temporal[aleatorio]
        final = final + random.choice(temporal)
    
    return final
  

def run():
    contrasena = generar_contrasena(int(input('Longitud de la contraseña: ')))
    print('Tu nueva contraseña es: ' + contrasena)
    

if __name__ == '__main__':
    run()