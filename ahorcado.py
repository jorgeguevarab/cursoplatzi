# Import secction here
import random
import os

# Global declarations
correct_chars = []
opportunities = 0
current_word = []



def read():
    lineas = []
       
    with open("ascii.txt", "r", encoding="utf-8") as f:
        for linea in f:
            lineas.append(linea[:-1])                
    return lineas
    
def dibuja(lista, tlevels):
    inicio = tlevels[0]
    fin = tlevels[1]
    filtrado = [elemento for elemento in lista[inicio-1:fin]]
      
    for i in filtrado:
        print(i)
        
        
def select_words():
    all_words = []
    selected_word = ""
    with open("words.txt", "r", encoding="utf-8") as f:
        for word in f:
            all_words.append(word)
    
        selected_word = random.choice(all_words)
    
    return selected_word.upper()
    
            
def fill_list(char, word, current_word):
    # Return list with chars and underscores
    index = 0
    # current_word = ['_ ' for i in range(len(word) - 1)]
    is_hit = False
    # new_word = ['_ ' for i in enumerate(word)]
    
    for letter in word:
        if letter == char.upper():
            current_word[index] = char.upper()
            is_hit = True
            
        index += 1
    os.system("clear")  
    
    return is_hit    

def write(frase):
    
    with open("./data/data.txt", "a", encoding="utf-8") as f:
        f.write(frase)
        f.write("\n")    
    


def run():
    # os.system("clear")
    hangman = read()
    # dibuja(lista, 61,70)
    
    # print(select_words())
    levels = [(61, 70), (51, 60), (41, 50), (31, 40), (21, 30), (11, 20), (1, 10)]
    
    is_hit = False
    os.system("clear")
    palabra = select_words()
    
    # print(palabra)
    
    current_word = ['_ ' for i in range(len(palabra))]
    print("".join(current_word))
    
    opportunities = 7
            
    while opportunities != 0:
        if palabra.strip() != "".join(current_word).strip():
            is_hit = fill_list(input("Inserta caracter: "), palabra, current_word)
            print("".join(current_word).strip())
            if is_hit != True:
                opportunities -= 1
                print("Tienes %s oportunidades\n" % opportunities)
                
                dibuja(hangman, levels[opportunities])                
        else:
             print("GANASTEEEEE")
             break
      
            
    
       
    

    
    
    

if __name__ == "__main__":
    run()
    
    