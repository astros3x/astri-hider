from data.modules.cb_rsa import cb_rsa_encrypt, cb_rsa_decrypt
from tkinter import messagebox, filedialog
from PIL import Image
import shutil
import os

def converter():
    file_path = filedialog.askopenfilename(title = 'Astri@Hider | Convert image', filetypes = [('File PNG', '.png'), ('File WEBP', '.webp'), ('File BMP', '.bmp'),
                                                                                              ('File TIFF', '.tiff'), ('File GIF',  '.gif')])
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    try:
        with Image.open(file_path) as img:
            img.convert('RGB').save(f'data\\results\\converted\\{file_name}.jpg', 'JPEG')
            
    except Exception as e:
        call_errorbox('Astri@Hider | Converter', f'Error : {e}')
        
    
def function_clear(path):
    with open(path, "rb+") as f:
        content = f.read()
        off = content.index(bytes.fromhex("FFD9"))
        if off != -1:
            f.seek(off + 2)
            f.truncate()


def check_ext(path):
    if path.endswith('.jpg'):
        return True
    
    else:
        return False


def get_filename(path):
    available = ["\\","/"]

    for z in available:
        if z in path:
            return path.split(z)[-1]


def file_present(path):
    try:
        open(path,"r")
        return True
    except FileNotFoundError:
        return False


def writer(filePath, msg, keysPath, encryption, outputPath):
    try:
        if file_present(filePath):
            if check_ext(filePath):

                #SCRIPT TO ADD THE MESSAGE TO THE JPG
                fileName = get_filename(filePath)

                shutil.copy(filePath, outputPath)

                path = f"{outputPath}\\{fileName}"

                function_clear(path)

                f = open(path, "ab")
                
                if encryption != 'None':
                    f.write(cb_rsa_encrypt(open(f'{keysPath}{encryption}.txt',"r").read().split("\n")[0], msg))
                else:
                    f.write(msg.encode())

                messagebox.showinfo("DONE !",f"Message successfully hide => `{fileName}` ")

            else:
                messagebox.showerror("ERROR", f"Your Image is NOT a JPG !")
        else:
            messagebox.showerror("ERROR", f"`{filePath}` NOT found !")

    except Exception as e:
        if "No such file" in str(e):
            messagebox.showinfo("Create a KEYS PAIR","You need to GENERATE a Keys Pair and a JSON SCHEME !")
        else:
            messagebox.showerror('Error', f'{e}')
    
    
def reader(filePath, keysPath, encryption):
    try:
        if(check_ext(filePath)):

            #SCRIPT TO EXTRACT THE MESSAGE FROM THE JPG

            f = open(filePath,"rb")

            content = f.read()
            off = content.index(bytes.fromhex('FFD9'))
            f.seek(off + 2)



            msg = f.read().decode('utf-8')

            filename = get_filename(filePath)


            if encryption != 'None':
                return cb_rsa_decrypt(open(f'{keysPath}{encryption}.txt',"r").read().split("\n")[1], msg)
            else:
                return msg

        else:
            messagebox.showerror('ERROR', 'Your Image is NOT a JPG !')
            
    except Exception as e:
        if "No such file" in str(e):

            if "db.json" in str(e):
                messagebox.showerror("SCHEME MISSING", f"GENERATE A JSON SCHEME !")
            
            else:
                messagebox.showerror("ERROR", f"`{filePath}` NOT found !")

        else:
            messagebox.showerror('Error', f'Private Key NOT CORRECT !')


def cleaner(filePath, outputPath):
    if filePath is not None:
        try:
            if (file_present(filePath)):
                if(check_ext(filePath)):
                    #SCRIPT TO CLEAR THE HIDDEN CONTENT FROM THE JPG

                    filename = get_filename(filePath)
                    shutil.copy(filePath, outputPath)

                    with open(f"{outputPath}\\{filename}", "rb+") as f:

                        content = f.read()
                        off = content.index(bytes.fromhex("FFD9")) #this function delet only the content at the end of the hex code

                        if off != -1:
                            f.seek(off + 2)
                            f.truncate()
                            messagebox.showinfo("DONE !",f"Image Cleared => `{filename}` ")
                        else:
                            messagebox.showerror('Error', 'No hidden content in this file!')
                            
                else:
                    messagebox.showerror("ERROR", f"Your Image is NOT a JPG !")
            else:
                messagebox.showerror("ERROR", f"`{filePath}`found !")

        except Exception as e:
            messagebox.showerror('Error', f'{e}')