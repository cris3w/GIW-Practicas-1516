from bottle import route, run, request, template
from modelo import *


global user


@route ('/inicio')
def iniciar():
	return template('vistas/index.tpl')


@route ('/login')
def login():
	return template('vistas/formularios/form-login.tpl')


@route('/login', method='post')
def do_login():
	usuario = request.forms.get('usuario')
	password = request.forms.get('password')
	
	try:
		usuario_r, password_r = buscar_usuario(usuario)
	except:
		return template('vistas/errores/error-base-datos.tpl', accion="dar acceso", sujeto="al usuario")
	
	if (usuario_r == '' and password_r == ''):
		return template('vistas/errores/error-usuario.tpl')
	elif (password != password_r):
		return template('vistas/errores/error-pass.tpl')
	elif (password == password):
		global user
		user = usuario
		return template('vistas/bienvenida.tpl', nombre=user)


@route ('/registro')
def registro():
	return template('vistas/formularios/form-registro.tpl')


@route ('/registro', method='post')
def do_registro():
	nombre = request.forms.get('nombre')
	apellido = request.forms.get('apellido')
	usuario = request.forms.get('usuario')
	password = request.forms.get('password')
	
	if (nombre == '' or apellido == '' or usuario == '' or password == ''):
		return template('vistas/errores/error-campos-vacios.tpl')
	else:
		try:
			usuario_r, password_r = buscar_usuario(usuario)
		except:
			return template('vistas/errores/error-base-datos.tpl', accion="registrar", sujeto="el usuario")
		
		if (usuario_r != '' and password_r != ''):
			return template('vistas/errores/error-registro.tpl') 
		else:
			insertar_usuario(usuario, password, nombre, apellido)
			global user
			user = usuario
			return template('vistas/salidas/registro.tpl', nombre=user)


@route ('/personales')
def modificar_datos():
	try:
		global user
		usuario_r, password_r, nombre_r, apellido_r = buscar_datos(user)
		return template('vistas/formularios/modificar-datos.tpl', nombre=nombre_r, apellido=apellido_r, usuario=usuario_r, password=password_r)
	except:
		return template('vistas/errores/error-base-datos.tpl', accion="modificar", sujeto="los datos del usuario")


@route ('/personales', method='post')
def do_modificar_datos():
	nombre = request.forms.get('nombre')
	apellido = request.forms.get('apellido')
	usuario = request.forms.get('usuario')
	password = request.forms.get('password')
	
	try:
		global user
		usuario_n = ''
		if (usuario != ''):
			usuario_n, password_n = buscar_usuario(usuario)
		usuario_r, password_r, nombre_r, apellido_r = buscar_datos(user)
		
		if (usuario_n != '' and usuario_n != user):
			return template('vistas/errores/error-modificar-datos.tpl') 
		else:
			if (usuario == ''):
				usuario = usuario_r
			if (password == ''):
				password = password_r
			if (nombre == ''):
				nombre = nombre_r
			if (apellido == ''):
				apellido = apellido_r
				
			modificar_usuario(usuario, password, nombre, apellido, user)
			user = usuario
		return template('vistas/salidas/exito.tpl', sujeto="El usuario", accion="modificado")
	except:
		return template('vistas/errores/error-base-datos.tpl', accion="modificar", sujeto="los datos del usuario")


@route('/nueva')
def nueva():
	return template('vistas/formularios/form-nueva.tpl')


@route('/nueva', method='post')
def do_nueva():
	titulo = request.forms.get('titulo')
	autor = request.forms.get('autor')
	genero = request.forms.get('genero')
	
	if (titulo == ''):
		return template('vistas/errores/error-titulo-vacio.tpl')
	
	try:
		titulo_r, autor_r, genero_r = buscar_pelicula(titulo)
		if (titulo_r != '' and autor_r != '' and genero_r != ''):
			return template('vistas/errores/error-ya-existe.tpl', sujeto="la pelicula")
		else:
			insertar_pelicula(titulo, autor, genero)
	except:
		return template('vistas/errores/error-base-datos.tpl', accion="insertar", sujeto="la pelicula")
	
	global user
	return template('vistas/salidas/exito.tpl', sujeto="La pelicula", accion="insertado")


@route('/listar')
def listar():
	try:
		lista = listar_peliculas()
	except:
		return template('vistas/errores/error-base-datos.tpl', accion="listar", sujeto="las peliculas")
		
	if (lista.__len__() == 0):
		return template('vistas/salidas/no-hay-peliculas.tpl')
	else:
		return template('vistas/salidas/listar.tpl', lista=lista)
		
	
@route('/buscar')
def buscar():
	return template('vistas/formularios/form-buscar.tpl', direccion="/buscar", accion="Buscar")


@route('/buscar', method='post')
def do_buscar():
	titulo = request.forms.get('titulo')
	
	try:
		titulo_r, autor_r, genero_r = buscar_pelicula(titulo)
	except:
		return template('vistas/errores/error-base-datos.tpl', accion="buscar", sujeto="la pelicula")
	
	if (titulo_r == '' and autor_r == '' and genero_r == ''):
		return template('vistas/errores/error-no-existe.tpl', sujeto="la pelicula")
	else:
		return template('vistas/salidas/buscar.tpl', titulo=titulo_r, autor=autor_r, genero=genero_r)

	
@route('/eliminar')
def eliminar():
	return template('vistas/formularios/form-buscar.tpl', direccion="/eliminar", accion="Eliminar")


@route('/eliminar', method='post')
def do_eliminar():
	titulo = request.forms.get('titulo')
	
	try:
		titulo_r, autor_r, genero_r = buscar_pelicula(titulo)
		
		if (titulo_r == '' and autor_r == '' and genero_r == ''):
			return template('vistas/errores/error-no-existe.tpl', sujeto="la pelicula")
		else:
			eliminar_pelicula(titulo)
			return template('vistas/salidas/exito.tpl', sujeto="La pelicula", accion="eliminado")
	except:
		return template('vistas/errores/error-base-datos.tpl', accion="eliminar", sujeto="la pelicula")


@route('/modificar')
def pre_modificar():
	return template('vistas/formularios/form-buscar.tpl', direccion="/modificar", accion="Modificar")
	
	
@route('/modificar', method='post')
def modificar():
	titulo = request.forms.get('titulo')
	
	try:
		titulo_r, autor_r, genero_r = buscar_pelicula(titulo)
		
		if (titulo_r == '' and autor_r == '' and genero_r == ''):
			return template('vistas/errores/error-no-existe.tpl', sujeto="la pelicula")
		else:
			return template('vistas/formularios/modificar.tpl', titulo=titulo_r, autor=autor_r, genero=genero_r)
			
	except:
		return template('vistas/errores/error-base-datos.tpl', accion="modificar", sujeto="la pelicula")
		
	
@route('/modificar/<title>', method='post')
def do_modificar(title):
	titulo = request.forms.get('titulo')
	autor = request.forms.get('autor')
	genero = request.forms.get('genero')
	
	try:
		titulo_n = ''
		if (titulo != ''):
			titulo_n, autor_n, genero_n = buscar_pelicula(titulo)
		titulo_r, autor_r, genero_r = buscar_pelicula(title)
		
		if (titulo_n != '' and titulo_n != title):
			return template('vistas/errores/error-ya-existe.tpl', sujeto="esa pelicula")
		else:
			if (titulo == ''):
				titulo = titulo_r
			if (autor == ''):
				autor = autor_r
			if (genero == ''):
				genero = genero_r
			
			modificar_pelicula(titulo, autor, genero, title)
			return template('vistas/salidas/exito.tpl', sujeto="La pelicula", accion="modificado")
	except:
		return template('vistas/errores/error-base-datos.tpl', accion="modificar", sujeto="la pelicula")


@route('/principal')
def show_principal():
	global user
	return template('vistas/bienvenida.tpl', nombre=user)


run(host='localhost', port=80)