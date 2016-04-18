import re
import urllib
from BeautifulSoup import BeautifulSoup
import os


def buscadorImagenes():
    html = urllib.urlopen('http://trenesytiempos.blogspot.com.es/').read()
    soup = BeautifulSoup(html)
    posts = soup.findAll('a', {"class":"post-count-link"}, href = re.compile("http://trenesytiempos.blogspot.com.es/2015"))
    numeros = soup.findAll('span', {"class":"post-count", "dir":"ltr"})
    
    i = 0
    m = 0
    n = 0
    num = 0

    entradas = []
    fechas = []
    
    for post in posts:
        entradas.append(post.get('href', None))
        fechas.append(post.contents[0])

    i = 1
    for entrada in entradas:
        html = urllib.urlopen(entrada).read()
        soup = BeautifulSoup(html)
        fotos = soup.findAll('a', {"imageanchor":"1"})
        carpeta = "entrada" + str(i)
        os.mkdir(carpeta)
        os.chdir(carpeta)

        j = 1
        for foto in fotos:
            archivo = open("foto" + str(j) + ".jpg", "wb")
            imagen = urllib.urlopen(foto.get('href', None))
            while True:
                info = imagen.read(100000)
                if (len(info)) < 1: break
                archivo.write(info)
            archivo.close()
            j = j + 1
        
        i = i + 1
        os.chdir(os.path.dirname(os.getcwd()))


def main(): 
    buscadorImagenes()


if __name__ == "__main__":
    main()