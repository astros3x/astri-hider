from tkinter import messagebox
import base64
import json

dbPath = 'data\\modules\\encryption\\db_base.json'

def cb_rsa_decrypt(k, m):
            key_split = k.split("_")
            d = int(key_split[1])
            n = int(key_split[2])
            sm = int(key_split[3])

            db = dict(json.loads(open(dbPath,"r").read()))

            m = base64.b64decode(m).decode().split("_")

            message = ""

            for val in m:
                if val != "$$$":

                    c = round((int(val)**d % n) / sm)
                    
                    message+= db[str(c)]

            return message


def cb_rsa_encrypt(k, m):
    key_split = k.split("_")

    e = int(key_split[1])
    n = int(key_split[2])
    sm = int(key_split[3])


    db = dict(json.loads(open(dbPath,"r").read()))

    reverse_db = dict(zip(db.values(),db.keys()))

    encrypted_msg = "$$$_"

    for char in m:

        try:
            enc = int(reverse_db[char])

        except: #KeyError
            enc = int(reverse_db["$_$_$_$_$"])

        c = int(pow((enc*sm),e) % n)

        encrypted_msg+= f"{c}_"

    encrypted_msg+= "$$$"

    return base64.b64encode(encrypted_msg.encode())