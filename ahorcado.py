# Import secction here
import random
import os

def read():
    lineas = []
       
    with open("ascii.txt", "r", encoding="utf-8") as f:
        for linea in f:
            lineas.append(linea[:-1])                
    return lineas
    
def dibuja(lista, inicio, fin):
    filtrado = [elemento for elemento in lista[inicio-1:fin]]
      
    for i in filtrado:
        print(i)
    

def write(frase):
    
    with open("./data/data.txt", "a", encoding="utf-8") as f:
        f.write(frase)
        f.write("\n")
        
    


def run():
    # os.system("clear")
    lista = read()
    dibuja(lista, 11,20)
    
    
    
    

if __name__ == "__main__":
    run()
    
    