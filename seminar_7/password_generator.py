import string as s 
import random
def generate_password(length, allow_symbols):
    i = 0
    password = ""
    first = s.ascii_letters + s.digits + s.punctuation
    second = s.ascii_letters + s.digits
    if allow_symbols == True:
        while i < length:
            i += 1
            password = "".join(random.choices(first, k=length))
    else:
       while i < length:
            i += 1
            password = "".join(random.choices(second, k=length))
    return password 

