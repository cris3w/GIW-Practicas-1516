import json

global lista


def crearLista():
    global lista
    
    manf = open('tweets.txt', 'r')
    
    pos = 0
    lista = []
    for linea in manf:
        tweet = json.loads(linea)
        if 'text' in tweet:
            lista.append(tweet)
        pos = pos + 1
		
    manf.close() 
    
    
def frecuencia():
    global lista
    
    termino = raw_input('Introduce termino: ')
        
    crearLista()
        
    frecTotal = 0
    diccionario = dict()
    for linea in lista:
        texto =  linea[u'text']
            
        palabras = texto.replace('.', ' ').replace(',',' ').replace(')',' ').replace('^',' ').replace('~',' ').replace('*',' ').replace('(',' ').replace('|',' ').replace('-',' ').replace('/',' ').replace(':',' ').replace('!',' ').replace('?',' ').replace('"',' ').replace(';',' ').split()
            
        for palabra in palabras:
            palabra.encode("UTF8")
            if palabra in diccionario:
                valor = diccionario[palabra] 
                diccionario[palabra] = valor + 1
            else:
                diccionario[palabra] = 1
            frecTotal = frecTotal + 1
             
    try:
        fsal = open('frecuencias.txt', 'w')
                
        for palabra in diccionario:
            frecTermino = diccionario[palabra]
            frecuencia = float(frecTermino) / frecTotal
            linea = palabra.encode("UTF8") + " " + str(frecuencia) + "\n"  
            fsal.write(linea)
            if palabra == termino:
                print 'La frecuencia de ' + termino + ' es: ' + str(frecuencia)
                
        if not termino in diccionario:
            print 'El termino ' + termino + ' no aparece'
            
        fsal.close()
            
    except:
        print 'Error con el fichero'
    
    
def topHashtags():
    global lista
    
    crearLista()
    
    ranking = dict()
    pos = 0
    for tweet in lista:
        entities = []
        if u'entities' in tweet:
            entities =  lista[pos][u'entities']
            if u'hashtags' in entities:
                hashtags = entities[u'hashtags']
                for hashtag in hashtags:
                    if u'text' in hashtag:
                        texto = hashtag[u'text']
                        if texto in ranking:
                            ranking[texto] = ranking[texto] + 1
                        else:
                            ranking[texto] = 1
            
        pos = pos + 1
        
    top = list(ranking.items())
    from operator import itemgetter
    top.sort(key=itemgetter(1), reverse=True)
    
    try: 
        i = 0
        fsal = open('ranking.txt', 'w')
        
        while i < 10:
            texto = top[i][0]
            valor = top[i][1]
            texto.encode("UTF8")
            linea = texto + " " + str(valor) + "\n"
            fsal.write(linea)
            i = i + 1
        fsal.close() 
        
    except:
        print 'Error con el fichero'
        
        
def main():
    frecuencia()
    topHashtags()


if __name__ == "__main__":
    main()