def contadorPalabras(fichero):
    try:
        manf = open(fichero, 'r')
        
        texto = manf.read()
        palabras = texto.split()
        diccionario = dict()
        for palabra in palabras:
            if palabra in diccionario:
                diccionario[palabra] = diccionario[palabra]+1
            else:
                diccionario[palabra] = 1
    
        manf.close()
        
        fsal = open('salida.txt', 'w')
        
        for palabra in diccionario:
            linea = palabra + ": " + str(diccionario[palabra]) + "\n"
            fsal.write(linea)

        fsal.close()
        
    except:
        print 'No se pudo abrir el fichero: ', fichero
        exit()


def main():
    contadorPalabras('texto.txt')
    
    
if __name__ == "__main__":
    main()