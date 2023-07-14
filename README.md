<div align="center">
    
<img src="https://github.com/astros3x/astri-hider/assets/87500882/2262a6b3-c7a7-4b5d-ba5f-ddd780c65906">

# ASTRI@HIDER

</div>

</div>

## 📍 About
Astri@Hider is a tool written in python that allows you to hide secret text messages in a JPG file without actually changing the image. It has a clean and flat [GUI](https://github.com/TomSchimansky/CustomTkinter) that make it intuitive and easy to use. ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) ![version](https://img.shields.io/badge/python-3.9-green)
<div align="center">

<img src="https://github.com/astros3x/astri-hider/assets/87500882/66993e6f-9640-4ede-b05f-2b36492f5f20">

</div>



## 🗒️ Features
* Hide a message: Hide a message in a .jpg file without actually changing the image.
```
message = str(("message")).encode()
f = open("file.jpeg","ab")
f.write(message)
```
* Reader: Read any text added to a .jpg file.
```
f = open("file.jpeg","rb")
content = f.read()
off = content.index(bytes.fromhex('FFD9'))
f.seek(off + 2)
msg = f.read().decode('utf-8')
```
* Encrypted MSG: Write an encrypted message using the .key in a .jpg file.
* Read encrypted: Read a secret message inside a .jpg using the .key file used to encrypt it.
* Encryption key: Change the .key to encrypt yur message as you want.
* Clear: Clear a .jpg from any text/useless bytes.
```
with open("file.jpeg", "rb+") as f:
    content = f.read()
    off = content.index(bytes.fromhex("FFD9"))
    if off != -1:
        f.seek(off + 2)
        f.truncate()
```

## :question: Support
If you have any issues or need help contact us in our [discord server](https://discord.gg/XnRjFmgPYz).
