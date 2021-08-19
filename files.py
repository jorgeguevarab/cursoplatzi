# Import secction here
import random

def read():
    frases = []
    with open("./data/data.txt", "r", encoding="utf-8") as f:
        for frase in f:
            frases.append(frase)
    # print(frases)
    print(random.choice(frases))

def write(frase):
    
    with open("./data/data.txt", "a", encoding="utf-8") as f:
        f.write(frase)
        f.write("\n")
        
    


def run():
    write(input("Escribe la frase de tu santo: "))
    print("Frase guardada con éxito")

if __name__ == "__main__":
    run()
    
    