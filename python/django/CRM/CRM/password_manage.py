import bcrypt

def password_generator(password):
    password = str(password).encode('utf8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password, salt)
    return hash

def password_verify(password,hash):
    password = str(password).encode('utf8')
    if bcrypt.checkpw(password,hash):
        return True
    else:
        return False