from tkinter import messagebox
import secrets
import random
import base64
import string
import json


dbPath = 'data\\modules\\encryption\\db_base.json'


def db_mixer():
    db = dict(json.loads(open(dbPath, 'r').read()))

    body = '{'


    keys = []

    for k in db:
        keys.append(db[k])

    for x in range(len(db) +1):
        if x != 0:
            delimiter = ''

            choice = secrets.choice(keys)
            keys.remove(choice)

            if choice == '':
                choice = ' '
            
            elif x != len(db):
                delimiter = ','

            body += f'"{x}" : "{choice}"{delimiter}\n'


    body += '}'

    open(dbPath,'w').write(body)
    

def keygen(keysPath, fileName):
    numbers = string.digits

    def gen_number():
        while True:

            x = ''

            for _ in range(3):
                x+= secrets.choice(numbers)

            x = int(x)

            if(isPrime(x)):
                return x


    def isPrime(n, k=5):
        if n <= 1:
            return False
        if n <= 3:
            return True

        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2

        for _ in range(k):
            a = random.randint(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False

        return True




    def mcd(a,b):
        while b:
            a, b = b, a % b
        return a

            
    p = gen_number()
    q = gen_number()
    sm = ''

    for _ in range(3):
        sm+= secrets.choice(numbers)

    sm = int(sm)


    n = p * q

    z = (p-1) * (q-1)
    while True:
        e = ''

        for _ in range(5):
            e+= secrets.choice(numbers)
        
        e = int(e)

        if mcd(e,z) == 1:
            break


    d = pow(e,-1,z)


    if((d*e) % z == 1):

        PUBLIC_KEY = f'KKK_{e}_{n}_{sm}_KKK'

        PRIVATE_KEY = f'KKK_{d}_{n}_{sm}_KKK'



        to_write = f'{PUBLIC_KEY}\n{PRIVATE_KEY}'

        open(f'{keysPath}{fileName}.txt','w').write(to_write)
        
    return fileName
                
