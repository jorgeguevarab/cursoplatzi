# Código original: Nicoll Idaly Angulo Mejia de Platzi
import bs4
import requests as rq
import re
from datetime import date

#Entro a la página que quiero scrapear
url  =  "https://es.finance.yahoo.com/quote/COP%3DX?p=COP%3DX"
respuesta = rq.get(url)
soup = bs4.BeautifulSoup(respuesta.text , "html.parser")

#Seleciono el identificador que quiero
v  = soup.select("#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)")
# Lo convierto a float
d     = str(v[0].text)
# Reemplazo la , por el punto para convertir en float
d1    = d.replace(".", "")
d2    = d1.replace(",",".")
dolar = float(d2)

today = date.today()

def usd_co(cantidad):
    conversion = round(cantidad * dolar, 2)
    print("{} dolares equivalen a {} pesos colombianos".format(cantidad, conversion))
    exit()

def co_usd(cantidad):
    conversion = round(cantidad / dolar, 2)
    print("{} pesos colombianos equivalen a {} dolares".format(cantidad, conversion))
    exit()

print("""
Hoy {}, el dolar está en {} pesos colombianos. 
Esta información se obtuvo desde: 
{}""".format(today,d, url))

moneda = int(input('''
Ingresa el 1 o  2 según  el tipo de cambio:
    [1] Dolar a pesos colombianos
    [2] Pesos colombianos a dolares
    Selecciona: '''))
print('********************************')
        
cantidad = int(input('Ingresa la cantidad que quieres convertir sin punto de miles: '))

if moneda == 1:
    usd_co(cantidad)
elif moneda ==2:
    co_usd(cantidad)
else:
    print("Parece que no elegiste la solución correcta")
    exit()
