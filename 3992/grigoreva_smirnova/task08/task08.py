import random
import string
def get_pwd(l, d=True, u=True, lo=True, s=True):
    chars = ''
    need = []
    if lo:
        chars += string.ascii_lowercase
        need.append(random.choice(string.ascii_lowercase))
    if u:
        chars += string.ascii_uppercase
        need.append(random.choice(string.ascii_uppercase))
    if d:
        chars += string.digits
        need.append(random.choice(string.digits))
    if s:
        chars += string.punctuation
        need.append(random.choice(string.punctuation))
    if len(need) > l: return "слишком коротко"
    
    pwd = need + [random.choice(chars) for _ in range(l - len(need))]
    random.shuffle(pwd)
    return''.join(pwd)
print (get_pwd(10))
        
