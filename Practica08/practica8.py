# -*- coding: utf-8 -*-

from bottle import post, request, run, get, template
from pymongo import MongoClient


@get('/add_user')
def add_user():
    return template('formularios/form-add-user.tpl')


@post('/add_user')
def do_add_user():
    _id = request.forms.get('_id')
    country = request.forms.get('country')
    zip = request.forms.get('zip')
    email = request.forms.get('email')
    gender = request.forms.get('gender')
    likes = request.forms.get('likes')
    password = request.forms.get('password') 
    year = request.forms.get('year') 
    
    nuevo = {
        "_id": _id,
             "address": {
                 "country": country,
                 "zip": int(zip)},
        "email": email,
        "gender": gender,
        "likes": [likes],
        "password": password,
        "year": int(year)}
    
    client = MongoClient('localhost', 27017)
    try:
        nuevo_id = client.giw.users.insert_one(nuevo).inserted_id
        print "el usuario se ha insertado con exito"
    except:
        print "el usuario ya existe"
        
    
@get('/change_email')
def change_email():
    return template('formularios/form-change-email.tpl')
    
    
@post('/change_email')
def do_change_email():
    _id = request.forms.get('_id')
    email = request.forms.get('email')
    
    client = MongoClient('localhost', 27017)
    result = client.giw.users.update_many(
        {"_id": _id},
        {"$set": {"email": email}})
    print result.modified_count


@get('/insert_or_update')
def insert_or_update():
    return template('formularios/form-insert-or-update.tpl')
    
    
@post('/insert_or_update')
def do_insert_or_update():
    _id = request.forms.get('_id')
    country = request.forms.get('country')
    zip = request.forms.get('zip')
    email = request.forms.get('email')
    gender = request.forms.get('gender')
    likes = request.forms.get('likes')
    password = request.forms.get('password') 
    year = request.forms.get('year') 
    
    client = MongoClient('localhost', 27017)
    cursor = client.giw.users.find({"_id": _id})
    
    if (cursor.count() == 0):
        nuevo = {
            "_id": _id,
            "address": {
                "country": country,
                "zip": int(zip)},
            "email": email,
            "gender": gender,
            "likes": [likes],
            "password": password,
            "year": int(year)}
        
        nuevo_id = client.giw.users.insert_one(nuevo).inserted_id
        print "el usuario se ha insertado con exito"
        
    elif (cursor.count() == 1):
        result = client.giw.users.update_one(
            {"_id": _id},
            {"$set": {
                    "address": {
                        "country": country, 
                        "zip": int(zip)},
                    "email": email,
                    "gender": gender,
                    "likes": [likes],
                    "password": password,
                    "year": int(year)}})
        print "el usuario se ha modificado con exito"


@get('/delete')
def delete_id():
    return template('formularios/form-delete-id.tpl')


@post('/delete')
def do_delete_id():
    _id = request.forms.get('_id')
    
    client = MongoClient('localhost', 27017)
    result = client.giw.users.delete_one({"_id": _id})
    print result.deleted_count
    
    
@get('/delete_year')
def delete_year():
    return template('formularios/form-delete-year.tpl')
       
       
@post('/delete_year')
def do_delete_year():
    year = request.forms.get('year')
    
    client = MongoClient('localhost', 27017)
    result = client.giw.users.delete_many({"year": int(year)})
    print result.deleted_count
    

run (host='localhost', port=80)
