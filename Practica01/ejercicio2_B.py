global fichero


def cargarEntrada():
    fich = raw_input('Introduzca el nombre del fichero: ')
    global fichero 
    fichero = fich


def crearEntrada():
    global fichero
    
    try:
        nombre = raw_input('Nombre: ')
        apellido1 = raw_input('Primer apellido: ')
        apellido2 = raw_input('Segundo apellido: ')
        telefono = raw_input('Telefono: ')
    
        manf = open(fichero, 'r')
		
        fsal = open('temp.txt', 'w')
        
        for linea in manf:
            fsal.write(linea)
    
        manf.close()
        fsal.close()
        
        manf = open('temp.txt', 'r')
        
        fsal = open(fichero, 'w')
        
        for linea in manf:
            fsal.write(linea)
        
        linea = nombre + "\n"
        fsal.write(linea)
        linea = apellido1 + "\n"
        fsal.write(linea)
        linea = apellido2 + "\n"
        fsal.write(linea)
        linea = telefono + "\n"
        fsal.write(linea)

        manf.close()
        fsal.close()
        
    except:
        print 'No se pudo abrir el fichero'
        exit()
        
    
def borrarEntrada():
    global fichero
    
    try:
        target = raw_input('Introduzca el numero de entrada que desea borrar: ')
    
        manf = open(fichero, 'r')
        
        fsal = open('temp.txt', 'w')
        
        n = 1
        cont = 1
        for linea in manf:
            if (str(n) != target):
                fsal.write(linea);
            if (cont == 4):
                cont = 1
                n = n + 1
            else:
                cont = cont + 1
            
        manf.close()
        fsal.close()
        
        manf = open('temp.txt', 'r')
        
        fsal = open(fichero, 'w')
        
        for linea in manf:
            fsal.write(linea);
        
        manf.close()
        fsal.close()
        
    except:
        print 'No se pudo abrir el fichero'
        exit()
        

def buscarEntrada():
    global fichero
    
    try:
        target = raw_input('Introduzca el termino de busqueda: ')
        print "\n"
        target = target + "\n"
        
        manf = open(fichero, 'r')
        
        n = 1
        cont = 1
        encontrado = False
        for linea in manf:
            if cont == 1:
                nombre = linea
            elif cont == 2:
                apellido1 = linea
            elif cont == 3:
                apellido2 = linea
            elif cont == 4:
                telefono = linea
                
            if (cont == 4):
                if (nombre == target or apellido1 == target or apellido2 == target or telefono == target):
                    encontrado = True
                else:
                    encontrado = False
                    
                cont = 1
                
                if encontrado:
                    print "  #" + str(n) + "\n" + " " + nombre + " " + apellido1 + " " + apellido2 + " " + telefono
                    
                n = n + 1
            else:
                cont = cont + 1
        
        manf.close()          
    
    except:
        print 'No se pudo abrir el fichero'
        exit()

                                                                                                                                                                                                                    
def menu():
    print "\n"
    print 'Menu: \n'
    print 'Opcion 1: Crear entrada \n'
    print 'Opcion 2: Borrar entrada \n'
    print 'Opcion 3: Buscar por nombre, apellido o telefono \n'
    print 'Opcion 4: Cargar entrada \n'
    print 'Opcion 5: Salir \n'


def main():
    menu()
    opcion = raw_input('Opcion: ')
    print "\n"
        
    while (opcion != '5'):
        if opcion == '1':
            crearEntrada()
        elif opcion == '2':
            borrarEntrada()
        elif opcion == '3':
            buscarEntrada()
        elif opcion == '4':
            cargarEntrada()
            
        menu()
        opcion = raw_input('Opcion: ')
        print "\n"


if __name__ == "__main__":
    main()