# -*- coding: utf-8 -*-

from bottle import run, get, post, request, template
from pymongo import MongoClient
import hashlib, uuid, random, string
import onetimepass as otp


APP_NAME = "GIW_grupo01"


# APARTADO A 


@get('/signup')
def signup_form():
    
    return template('vistas/form-registro.tpl', accion='/signup')


@post('/signup')
def signup():
    nickname = request.forms.get('nickname')
    name = request.forms.get('name')
    country = request.forms.get('country')
    email = request.forms.get('email')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')

    client = MongoClient('localhost', 27017)
    
    if (password != password2):
        return template('vistas/error.tpl', mensaje="las contraseñas no coinciden")
    
    cursor = client.giw.users.find({"nickname": nickname})
        
    if (cursor.count() > 0):
        return template('vistas/error.tpl', mensaje="el alias de usuario ya existe")
    
    salt = uuid.uuid4().hex
    pass_encrypted = hashlib.sha512(password + salt).hexdigest()
            
    nuevo = {
        "nickname": nickname,
        "name": name,
        "country": country,
        "email": email,
        "password": pass_encrypted,
        "salt": salt}
            
    client.giw.users.insert_one(nuevo).inserted_id
    return template('vistas/bienvenida.tpl', name=name)


@get('/change_password')
def change_password_form():
    
    return template('vistas/form-change-password.tpl')


@post('/change_password')
def change_password():
    nickname = request.forms.get('nickname')
    old_password = request.forms.get('old_password')
    new_password = request.forms.get('new_password')

    client = MongoClient('localhost', 27017)
    
    usuario = client.giw.users.find_one({"nickname": nickname})
    
    if not usuario:
        return template('vistas/error.tpl', mensaje="usuario o contraseña incorrectos")
    
    old_encrypted = hashlib.sha512(old_password + usuario["salt"]).hexdigest()
    
    if (old_encrypted != usuario["password"]):
        return template('vistas/error.tpl', mensaje="usuario o contraseña incorrectos")
    
    new_salt = uuid.uuid4().hex
    new_encrypted = hashlib.sha512(new_password + new_salt).hexdigest()
    
    client.giw.users.update_one(
        {"nickname": nickname},
        {"$set": {
            "password": new_encrypted,
            "salt": new_salt}})
    
    return template('vistas/change-pass-exito.tpl', nickname=nickname)


@get('/login')
def login_form():
    
    return template('vistas/form-login.tpl')


@post('/login')
def login():
    nickname = request.forms.get('nickname')
    password = request.forms.get('password')

    client = MongoClient('localhost', 27017)

    usuario = client.giw.users.find_one({"nickname": nickname})
        
    if not usuario:
        return template('vistas/error.tpl', mensaje="usuario o contraseña incorrectos")
            
    pass_encrypted = hashlib.sha512(password + usuario["salt"]).hexdigest()
    
    if (usuario["password"] != pass_encrypted):
        return template('vistas/error.tpl', mensaje="usuario o contraseña incorrectos")
            
    return template('vistas/bienvenida.tpl', name=usuario["name"])


# APARTADO B 


# Genera una cadena aleatoria de 16 caracteres a escoger entre las 26 letras mayúsculas del inglés y los dígitos 2, 3, 4, 5, 6 y 7
def gen_secret():
    length = 16
    chars = string.ascii_uppercase + "234567" 
    return "".join(random.sample(chars*length, length))   
    
    
# Genera la URL para insertar una cuenta en Google Authenticator   
def gen_gauth_url(app_name, username, secret):
    
    return "otpauth://totp/" + username + "?secret=" + secret + "&issuer=" + app_name
        

# Genera la URL para generar el código QR que representa 'gauth_url'
def gen_qrcode_url(gauth_url):
    
    return "http://api.qrserver.com/v1/create-qr-code/?data=" + str(gauth_url)
    

@get('/signup_totp')
def signup_totp_form():
    
    return template('vistas/form-registro.tpl', accion='/signup_totp')


@post('/signup_totp')
def signup_totp():
    nickname = request.forms.get('nickname')
    name = request.forms.get('name')
    country = request.forms.get('country')
    email = request.forms.get('email')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')

    client = MongoClient('localhost', 27017)
    
    if (password != password2):
        return template('vistas/error.tpl', mensaje="las contraseñas no coinciden")
    
    cursor = client.giw.users.find({"nickname": nickname})
        
    if (cursor.count() > 0):
        return template('vistas/error.tpl', mensaje="el alias de usuario ya existe")
    
    semilla = gen_secret()
    
    salt = uuid.uuid4().hex
    pass_encrypted = hashlib.sha512(password + salt).hexdigest()
    
    nuevo = {
        "nickname": nickname,
        "name": name,
        "country": country,
        "email": email,
        "password": pass_encrypted,
        "salt": salt,
        "semilla": semilla}
            
    nuevo_id = client.giw.users.insert_one(nuevo).inserted_id
    
    global APP_NAME
    gauth_url = gen_gauth_url(APP_NAME, str(nuevo_id), nuevo["semilla"]);
    qrcode = gen_qrcode_url(gauth_url)
    
    return template('vistas/bienvenida-totp.tpl', name=name, qrcode=qrcode, semilla=nuevo["semilla"])
        

@get('/login_totp')
def login_totp_form():
    
    return template('vistas/form-login-totp.tpl')
        
        
@post('/login_totp')
def login_totp():
    nickname = request.forms.get('nickname')
    password = request.forms.get('password')
    totp = request.forms.get('totp')

    client = MongoClient('localhost', 27017)
    
    usuario = client.giw.users.find_one({"nickname": nickname})
        
    if not usuario:
        return template('vistas/error.tpl', mensaje="usuario o contraseña incorrectos")
            
    pass_encrypted = hashlib.sha512(password + usuario["salt"]).hexdigest()
    
    if (usuario["password"] != pass_encrypted):
        return template('vistas/error.tpl', mensaje="usuario o contraseña incorrectos")
    
    semilla = usuario["semilla"]
    valido = otp.valid_totp(totp, semilla)
    
    if not valido:
        return template('vistas/error.tpl', mensaje="usuario o contraseña incorrectos")
    
    return template('vistas/bienvenida.tpl', name=usuario["name"])

    
if __name__ == "__main__":
    run(host='localhost', port=80, debug=True)
