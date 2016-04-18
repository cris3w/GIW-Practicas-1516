import sqlite3


def crear():

    conn = sqlite3.connect('Peliculas.sqlite3')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Usuarios')
    cur.execute('CREATE TABLE Usuarios (Usuario TEXT PRIMARY KEY, Password TEXT, Nombre TEXT, Apellido TEXT)')
    cur.execute('DROP TABLE IF EXISTS Peliculas')
    cur.execute('CREATE TABLE Peliculas (Titulo TEXT PRIMARY KEY, Autor TEXT, Genero TEXT)')
    
    cur.close()
    conn.commit()
    print "Tablas creadas \n"

    
def main():
    crear()
    
    
if __name__ == "__main__":
    main()
