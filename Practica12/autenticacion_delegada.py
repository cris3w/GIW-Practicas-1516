from bottle import run, get, request
import urllib, json, hashlib, string, random


# Credenciales 
# https://developers.google.com/identity/protocols/OpenIDConnect#appsetup
CLIENT_ID     = "679848970183-29tkhvu7dv4luiv3b4g1jdp1b5updor6.apps.googleusercontent.com"
CLIENT_SECRET = "DJYW1MbnxsCNFV4TbxTii1mY"
REDIRECT_URI  = "http://localhost:8080/token"

# Fichero de descubrimiento para obtener el 'authorization endpoint' y el 'token endpoint'
# https://developers.google.com/identity/protocols/OpenIDConnect#authenticatingtheuser
DISCOVERY_DOC = "https://accounts.google.com/.well-known/openid-configuration"

# Token validation endpoint para decodificar JWT
# https://developers.google.com/identity/protocols/OpenIDConnect#validatinganidtoken
TOKEN_VALIDATION_ENDPOINT = "https://www.googleapis.com/oauth2/v3/tokeninfo"


STATE = ""


def gen_secret():
    length = 16
    chars = string.ascii_uppercase + "234567" 
    return "".join(random.sample(chars*length, length)) 


@get('/login_google')
def login_google():
    
    global STATE
    STATE = hashlib.sha512(gen_secret()).hexdigest() # synchronizer token
    
    global CLIENT_ID, REDIRECT_URI
    url = "https://accounts.google.com/o/oauth2/v2/auth?"
    url += "client_id=" + CLIENT_ID
    url += "&response_type=code"
    url += "&scope=openid%20email"
    url += "&redirect_uri=" + REDIRECT_URI
    url += "&state=" + STATE
    
    return '''<a href=''' + url + '''>Autenticarse</a>'''


@get('/token')
def token():
    code = request.query.code
    estado = request.query.state
    
    global STATE
    if (estado == STATE): # si no coinciden, se trata de un ataque CSRF y se ignora
    
        global DISCOVERY_DOC
        data = json.load(urllib.urlopen(DISCOVERY_DOC))
        
        global CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
        params = urllib.urlencode({
                            "code": code, 
                            "client_id": CLIENT_ID, 
                            "client_secret": CLIENT_SECRET,
                            "redirect_uri": REDIRECT_URI,
                            "grant_type": "authorization_code"})
        
        data = json.load(urllib.urlopen(data['token_endpoint'], params))
        
        global TOKEN_VALIDATION_ENDPOINT
        params = urllib.urlencode({
                            "id_token": data['id_token']})
         
        data = json.load(urllib.urlopen(TOKEN_VALIDATION_ENDPOINT, params))
    
        return '''Bienvenido ''' + data['email']


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
