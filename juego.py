# Importamos el módulo random. 
import random

#Definimos la función principal
def main():
    #Capturamos los valores iniciales y finales
    desde = int(input("Desde: "))
    hasta = int(input("Hasta: "))

    #Generamos el número aleatorio
    aleatorio = random.randint(desde, hasta)
    #Solicitamos el primer número
    eleccion = int(input("Escribe un número entre " + str(desde) + " y "+ str(hasta) +": "))

    #Definimos el número de oportunidades
    oportunidades = 5

    while eleccion != aleatorio:
        #Actualizamos el número de oportunidades
        oportunidades -= 1
        print("Te quedan {} intentos".format(oportunidades))
        
        #Si no quedan oportunidades finalizamos el ciclo
        if oportunidades == 0:
            break
        else:
            #De lo contrario continuamos dando unas pistas:
            if eleccion < aleatorio:
                print("Escribe un valor mayor: ")
            elif eleccion > aleatorio:
                print("Escribe un valor menor: ")
              
            eleccion = int(input())
        
    #Evaluamos si se llegó al límite de oportunidades y listo!    
    if oportunidades == 0:
        print("Has perdido :(")
    else:
        print("¡Has ganado!")

#Ejecutamos la función main desde nuestro entry point
if __name__ == "__main__":
    main()


