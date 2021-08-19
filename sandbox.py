
palabra = input('Escribe una palabra: ')



if palabra.replace(' ','').lower() == palabra[::-1].replace(' ','').lower():
    print('***** ES PALÍNDROMO *****')
else:
    print('***** noespalíndromo *****')

# print(palabra[::-1])


# import bs4
# import requests as rq
# import re
# from datetime import date

# #Entro a la página que quiero scrapear
# url  =  "https://es.finance.yahoo.com/quote/COP%3DX?p=COP%3DX"
# respuesta = rq.get(url)
# soup = bs4.BeautifulSoup(respuesta.text , "html.parser")

# # print(respuesta)
# # print(soup)

# # Escribiendo archivo html
# # result = open("sopa.html", "a")
# # result.write(str(soup))
# # result.close()

# parte = soup.select("data-reactid")

# print(parte)

# try:
#     a = int(input())
#     print(str(a))
# except ValueError:
#     print('Parece que hubo un error')
# except SyntaxError:
#     print('Error de sintaxis')
# except NameError:
#     print('Error de nombre')

