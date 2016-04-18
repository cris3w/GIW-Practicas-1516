import urllib
import xml.dom.minidom


serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'


def geolocalizacion():
    address = ''
    
    while address != 'stop':
        address = raw_input('Entrar ubicacion: ')
        
        if address != 'stop':
            if len(address) < 1 : break
        
            url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': address})
            uh = urllib.urlopen(url)
            data = uh.read()
        
            try:
                fsal = open('temporal.txt', 'w')
                fsal.write(data)
                fsal.close()
            except:
                print 'Error con el fichero temporal'
    
            arbol = xml.dom.minidom.parse("temporal.txt")
            response = arbol.documentElement
            results = response.getElementsByTagName("result")
        
            for result in results:
                dir_formateada = result.getElementsByTagName("formatted_address")[0].childNodes[0].data
            
                a_components = result.getElementsByTagName("address_component")
                for a_component in a_components:
                    tipo = a_component.getElementsByTagName("type")[0].childNodes[0].data
                    if (tipo == 'locality'):
                        ciudad = a_component.getElementsByTagName("long_name")[0].childNodes[0].data
                    if (tipo == 'administrative_area_level_1'):
                        entidad_nivel_1 = a_component.getElementsByTagName("long_name")[0].childNodes[0].data
                    if (tipo == 'country'):
                        pais_corto = a_component.getElementsByTagName("short_name")[0].childNodes[0].data
                        pais = a_component.getElementsByTagName("long_name")[0].childNodes[0].data
            
                geometry = result.getElementsByTagName("geometry")
                for geo in geometry:
                    location = geo.getElementsByTagName("location")
                    for loc in location:
                        latitud = loc.getElementsByTagName("lat")[0].childNodes[0].data
                        longitud = loc.getElementsByTagName("lng")[0].childNodes[0].data
        
            print 'Informacion:'
            print 'Nombre: ' + ciudad
            print 'Pais: ' + pais
            print 'Nombre corto de pais: ' + pais_corto
            print 'Entidad de nivel 1: ' + entidad_nivel_1
            print 'Direccion formateada: ' + dir_formateada
            print 'Latitud: ' + latitud + ' Longitud: ' + longitud


if __name__ == "__main__":
    geolocalizacion()
