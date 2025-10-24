import re
import filetype

def validate_nombre(n):
    return bool(n and len(n.strip()) >= 3 and len(n.strip()) <= 200)

def validate_email(e):
    if not e: return False
    return "@" in e and len(e) <= 100

def validate_celular(c):
    if not c: return True
    return bool(re.match(r"^\+\d{2,}\.?\d{6,}$", c)) or bool(re.match(r"^\d{7,}$", c))

def validate_tipo(tipo):
    return tipo in ("gato", "perro")

def validate_cantidad(c):
    try:
        v = int(c)
        return v >= 1
    except:
        return False

def validate_unidad(un):
    return un in ("m", "a")

def validate_foto(fileobj):
    if not fileobj: return False
    try:
        f = filetype.guess(fileobj)
        if not f: return False
        return f.extension in ("png","jpg","jpeg","gif")
    except:
        return False
