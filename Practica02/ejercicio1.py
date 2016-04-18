import csv


def frecuenciaAnyos():
    try:
        archivo = open("PitchingPost.csv")
        lector = csv.reader (archivo)
        
        diccionario = dict()

        for linea in lector:
            if linea[1] in diccionario:
                diccionario[linea[1]] = diccionario[linea[1]] +1
            else:
                diccionario[linea[1]] = 1
                
        salida = open("AcumAnnos.csv", "w")
        escritor = csv.writer(salida)
        escritor.writerow(["Anyos","Frecuencia"])
        
        for palabra in diccionario:
            escritor.writerow([palabra, str(diccionario[palabra])])
            
        salida.close()
        archivo.close()
        
    except:
        print "Error con los ficheros"


def frecuenciaNombre():
    try:
        archivo = open("PitchingPost.csv")
        lector = csv.reader (archivo)
        
        diccionario = dict()

        for linea in lector:
            if linea[0] in diccionario:
                diccionario[linea[0]] = diccionario[linea[0]]+1
            else:
                diccionario[linea[0]] = 1
                
        salida = open("AcumJugadores.csv", "w")
        escritor = csv.writer(salida)
        escritor.writerow(["Nombre","Frecuencia"])
        
        for palabra in diccionario:
            escritor.writerow([palabra, str(diccionario[palabra])])
            
        salida.close()
        archivo.close()
        
    except:
        print "Error con los ficheros"


def ordenado():
    try:
        archivo = open("PitchingPost.csv")
        lector = csv.reader(archivo)
        datos = list(lector)

        datos.sort()
        
        salida = open("Ordenado.csv", "w")
        escritor = csv.writer(salida)
        escritor.writerow(["Nombre"])
        
        for linea in datos:
            escritor.writerow(linea)

        salida.close()  
        archivo.close()
        
    except:
        print "Error con los ficheros"


def main():
    frecuenciaAnyos()
    frecuenciaNombre()
    ordenado()


if __name__ == "__main__":
    main()