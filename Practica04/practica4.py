# -*- coding: utf-8 -*-

import sqlite3


    # CREAR TABLAS 

def crear():

    conn = sqlite3.connect('Universidad.sqlite3')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Universidades')
    cur.execute('CREATE TABLE Universidades (Nombre_Univ TEXT PRIMARY KEY, Comunidad TEXT, Plazas INTEGER)')
    cur.execute('DROP TABLE IF EXISTS Estudiantes')
    cur.execute('CREATE TABLE Estudiantes (ID INTEGER PRIMARY KEY, Nombre_Est TEXT, Nota INTEGER, Valor INTEGER)')
    cur.execute('DROP TABLE IF EXISTS Solicitudes')
    cur.execute('CREATE TABLE Solicitudes (ID INTEGER, Nombre_Univ TEXT, Carrera TEXT, Decision TEXT, CONSTRAINT ID_FK FOREIGN KEY (ID) REFERENCES Estudiantes (ID) ON DELETE CASCADE ON UPDATE CASCADE, CONSTRAINT Nombre_FK FOREIGN KEY (Nombre_Univ) REFERENCES Universidades (Nombre_Univ) ON DELETE CASCADE ON UPDATE CASCADE, CONSTRAINT Solicitudes_PK PRIMARY KEY (ID, Nombre_Univ, Carrera))')

    cur.close()
    conn.commit()
    print "TABLAS CREADAS \n"


    # INTRODUCIR DATOS

def rellenar():
    
    conn = sqlite3.connect('Universidad.sqlite3')
    cur = conn.cursor()
    
    cur.executemany('INSERT INTO Universidades (Nombre_Univ, Comunidad, Plazas) VALUES ( ?, ?, ? )',
                [('Universidad Complutense de Madrid', 'Madrid', 15000),
                ('Universidad de Barcelona', 'Barcelona', 36000),
                ('Universidad de Valencia', 'Valencia', 10000),
                ('UPM', 'Madrid', 21000)])
    cur.executemany('INSERT INTO Estudiantes (ID, Nombre_Est, Nota, Valor) VALUES (?, ?, ?, ? )',
                [(123, 'Antonio', 8.9, 1000),
                (234, 'Juan', 8.6, 1500),
                (345, 'Isabel', 8.5, 500),
                (456, 'Doris', 7.9, 1000),
                (543, 'Pedro', 5.4, 2000),
                (567, 'Eduardo', 6.9, 2000),
                (654, 'Alfonso', 7.9, 1000),
                (678, 'Carmen', 5.8, 200),
                (765, 'Javier', 7.9, 1500),
                (789, 'Isidro', 8.4, 800),
                (876, 'Irene', 6.9, 400),
                (987, 'Elena', 6.7, 800)])
    cur.executemany('INSERT INTO Solicitudes (ID, Nombre_Univ, Carrera, Decision) VALUES (?, ?, ?, ? )',
                [(123, 'Universidad Complutense de Madrid', 'Informatica', 'si'),
                (123, 'Universidad Complutense de Madrid', 'Economia', 'no'),
                (123, 'Universidad de Barcelona', 'Informatica', 'si'),
                (123, 'UPM', 'Economia', 'si'),
                (234, 'Universidad de Barcelona', 'Biologia', 'no'),
                (345, 'Universidad de Valencia', 'Bioingenieria', 'si'),
                (345, 'UPM', 'Bioingenieria', 'no'),
                (345, 'UPM', 'Informatica', 'si'),
                (345, 'UPM', 'Economia', 'no'),
                (678, 'Universidad Complutense de Madrid', 'Historia', 'si'),
                (987, 'Universidad Complutense de Madrid', 'Informatica', 'si'),
                (987, 'Universidad de Barcelona', 'Informatica', 'si'),
                (876, 'Universidad Complutense de Madrid', 'Informatica', 'no'),
                (876, 'Universidad de Valencia', 'Biologia', 'si'),
                (876, 'Universidad de Valencia', 'Biologia Marina', 'no'),
                (765, 'Universidad Complutense de Madrid', 'Historia', 'si'),
                (765, 'UPM', 'Historia', 'no'),
                (765, 'UPM', 'Psicologia', 'si'),
                (543, 'Universidad de Valencia', 'Informatica', 'no')])

    cur.close()
    conn.commit()
    print "DATOS INTRODUCIDOS \n"


    # CONSULTAS
    
def consultar():
    
    conn = sqlite3.connect('Universidad.sqlite3')
    cur = conn.cursor()
    
        # CONSULTA 1
        # Obtener los nombres y notas de los estudiantes así como el resultado de su solicitud de
        # manera que tengan un valor de corrección menor que 1000 y hayan solicitado la carrera de
        # "Informática" en la "Universidad Complutense de Madrid"
        
    cur.execute('SELECT E.Nombre_Est, E.Nota, S.Decision FROM Estudiantes E, Solicitudes S WHERE S.ID=E.ID AND E.Valor<1000 AND S.Carrera="Informatica" AND S.Nombre_Univ="Universidad Complutense de Madrid"')
    print "RESULTADO CONSULTA 1:"
    for i in cur.fetchall():
        print "Nombre: " + i[0] + ", Nota: " + str(i[1]) + ", Decision: " + i[2]
    print "\n"
     
        # CONSULTA 2:
        # Obtener los estudiantes cuya nota ponderada cambia en más de un punto respecto a la nota original
        # nota ponderada = (nota*valor)/1000-nota
        
    cur.execute('SELECT ID, Nombre_Est, Nota, Nota*Valor/1000.0 as POND FROM Estudiantes WHERE ABS(Nota*(Valor/1000.0)-Nota)>1.0')
    print "RESULTADO CONSULTA 2:"
    for i in cur.fetchall():
        print '{:<5} {:<9} {:<5} {:<5}'.format(str(i[0]), i[1], str(i[2]), str(i[3]))
    print "\n"
        
        # CONSULTA 3:
        # Modificar la tabla solicitudes de forma que aquellos estudiantes que no solicitaron ninguna
        # universidad, soliciten "Informática" en la "Universidad de Jaen"
        
    cur.execute('INSERT INTO Universidades (Nombre_Univ, Comunidad) VALUES (?, ?)', ('Universidad de Jaen', 'Jaen'))
    conn.commit()
    cur.execute('SELECT ID FROM Estudiantes WHERE ID NOT IN (SELECT ID FROM Solicitudes)')
    for i in cur.fetchall():
        cur.execute('INSERT INTO Solicitudes (ID, Nombre_Univ, Carrera) VALUES (?, ?, ? )', (i[0], 'Universidad de Jaen', 'Informatica'))
        conn.commit()
    cur.execute('SELECT ID, Nombre_Univ, Carrera, Decision FROM Solicitudes WHERE Nombre_Univ="Universidad de Jaen" AND Carrera="Informatica"')
    print "RESULTADO CONSULTA 3:"
    for i in cur.fetchall():
        print "ID: " + str(i[0]) + ", Universidad: " + i[1] + ", Carrera: " + i[2]
    print "\n"
    
        # CONSULTA 4
        # Admitir en la "Universidad de Jaen" a todos los estudiantes de "Económicas" que no
        # fueron admitidos en dicha carrera en otras universidades
        
    cur.execute('SELECT ID, Carrera FROM Solicitudes WHERE Carrera="Economia" AND Decision="no" AND ID NOT IN (SELECT ID FROM Solicitudes WHERE Carrera="Economia" AND Decision="si")')
    for i in cur.fetchall():
        cur.execute('INSERT INTO Solicitudes (ID, Nombre_Univ, Carrera, Decision) VALUES ( ?, ?, ?, ? )', (i[0], 'Universidad de Jaen', i[1], 'si'))
        conn.commit()
    cur.execute('SELECT ID, Nombre_Univ, Carrera, Decision FROM Solicitudes WHERE Carrera="Economia" AND Nombre_Univ="Universidad de Jaen"')
    print "RESULTADO CONSULTA 4:"
    for i in cur.fetchall():
        print "ID: " + str(i[0]) + ", Universidad: " + i[1] + ", Carrera: " + i[2] + ", Decision: " + i[3]
    print "\n"
    
        # CONSULTA 5
        # Borrar a todos los estudiantes que solicitaron más de 2 carreras diferentes
        
    cur.execute('SELECT E1.ID FROM Estudiantes E1 WHERE 2 < (SELECT COUNT(DISTINCT Carrera) FROM Estudiantes E2, Solicitudes S WHERE E2.ID=S.ID AND E2.ID=E1.ID GROUP BY E2.ID)')
    print "RESULTADO CONSULTA 5:"
    for i in cur.fetchall():
        print "ID: " + str(i[0])
    cur.execute('SELECT E1.ID FROM Estudiantes E1 WHERE 2 < (SELECT COUNT(DISTINCT Carrera) FROM Estudiantes E2, Solicitudes S WHERE E2.ID=S.ID AND E2.ID=E1.ID GROUP BY E2.ID)')
    for i in cur.fetchall():
        cur.execute('DELETE FROM Estudiantes WHERE ID = ' + str(i[0]))
        cur.execute('DELETE FROM Solicitudes WHERE ID = ' + str(i[0]))
        conn.commit()
        
    cur.close()
    

def main(): 
    crear()
    rellenar()
    print "\n"
    consultar()
    

if __name__ == "__main__":
    main()