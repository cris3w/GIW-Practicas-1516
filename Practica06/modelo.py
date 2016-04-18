import sqlite3


def buscar_usuario(usuario):
    conn = sqlite3.connect('Peliculas.sqlite3')
    cur = conn.cursor()
        
    usuario_r = ''
    password_r = ''
    cur.execute('SELECT Usuario, Password FROM Usuarios WHERE Usuario == ?', (usuario,))
    for i in cur.fetchall():
        usuario_r = i[0]
        password_r = i[1]
    
    cur.close()
    
    return usuario_r, password_r


def buscar_datos(usuario):
    conn = sqlite3.connect('Peliculas.sqlite3')
    cur = conn.cursor()
        
    usuario_r = ''
    password_r = ''
    nombre_r = ''
    apellido_r = ''
    cur.execute('SELECT Usuario, Password, Nombre, Apellido FROM Usuarios WHERE Usuario == ?', (usuario,))
    for i in cur.fetchall():
        usuario_r = i[0]
        password_r = i[1]
        nombre_r = i[2]
        apellido_r = i[3]
    
    cur.close()
    
    return usuario_r, password_r, nombre_r, apellido_r
        

def insertar_usuario(usuario, password, nombre, apellido):
    conn = sqlite3.connect('Peliculas.sqlite3')
    cur = conn.cursor()
        
    cur.executemany('INSERT INTO Usuarios(Usuario, Password, Nombre, Apellido) VALUES ( ?, ?, ?, ? )',
                [(usuario, password, nombre, apellido)])
        
    cur.close()
    conn.commit()


def modificar_usuario(usuario, password, nombre, apellido, usu):
    conn = sqlite3.connect('Peliculas.sqlite3')
    cur = conn.cursor()

    cur.execute('UPDATE Usuarios SET Usuario = ?, Password = ?, Nombre = ?, Apellido = ? WHERE Usuario = ?', 
                (usuario, password, nombre, apellido, usu,))

    cur.close()
    conn.commit()
    
    
def buscar_pelicula(titulo):
    conn = sqlite3.connect('Peliculas.sqlite3')
    cur = conn.cursor()
        
    titulo_r = ''
    autor_r = ''
    genero_r = ''
    cur.execute('SELECT Titulo, Autor, Genero FROM Peliculas WHERE Titulo == ?', (titulo,))
    for i in cur.fetchall():
        titulo_r = i[0]
        autor_r = i[1]
        genero_r = i[2]
    
    cur.close()
    
    return titulo_r, autor_r, genero_r
    
    
def insertar_pelicula(titulo, autor, genero):
    conn = sqlite3.connect('Peliculas.sqlite3')
    cur = conn.cursor()
    
    cur.executemany('INSERT INTO Peliculas(Titulo, Autor, Genero) VALUES ( ?, ?, ? )',
                [(titulo, autor, genero)])
        
    cur.close()
    conn.commit()
    
    
def listar_peliculas():
    conn = sqlite3.connect('Peliculas.sqlite3')
    cur = conn.cursor()
    
    lista = []
    cur.execute('SELECT Titulo FROM Peliculas')
    for i in cur.fetchall():
        lista.append(i[0])
    
    cur.close()
    
    return lista


def eliminar_pelicula(titulo):
    conn = sqlite3.connect('Peliculas.sqlite3')
    cur = conn.cursor()
        
    cur.execute('DELETE FROM Peliculas WHERE Titulo = ?', (titulo,))
    
    cur.close()
    conn.commit()
    
    
def modificar_pelicula(titulo, autor, genero, title):
    conn = sqlite3.connect('Peliculas.sqlite3')
    cur = conn.cursor()
    
    cur.execute('UPDATE Peliculas SET Titulo = ?, Autor = ?, Genero = ? WHERE Titulo = ?', (titulo, autor, genero, title,))
    
    cur.close()
    conn.commit()