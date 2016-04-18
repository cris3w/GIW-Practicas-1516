import urllib
import re
from BeautifulSoup import *


def buscadorPalabrasClave():
    entrada = raw_input("Introduzca las palabras a buscar (Separadas con espacios): ")
    palabras = entrada.split()
	
    html = urllib.urlopen('http://trenesytiempos.blogspot.com.es/').read()
    soup = BeautifulSoup(html)
    posts = soup.findAll('a', {"class":"post-count-link"})

    lista = []
    i = 0
    for post in posts:
        if (i > 0):
            lista.append(post.get('href', None))
        i = i + 1
        
    for entrada in lista:
        html = urllib.urlopen(entrada).read()
        i = 0
        for palabra in palabras:
            buscar = re.findall("[\s|( |¿ |¡]" + palabra + "[\s|)|.|,|?|!]", html)
            ok = False
            for buscado in buscar:
                ok = True
            if (ok == True):
                i = i + 1
        if (i == len(palabras)):
            print entrada

			
def main(): 
    buscadorPalabrasClave()


if __name__ == "__main__":
    main()