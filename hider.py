from tkinter import messagebox, filedialog, font
from cryptography.fernet import Fernet
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import customtkinter
from random import *
import pywinstyles
import webbrowser
import requests
import secrets
import shutil
import random
import base64
import string
import json
import sys
import os


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # < --- Self settings --- >
        self.title('Astri@Hider')
        self.attributes('-topmost', ontop)
        self.iconbitmap()
        self.overrideredirect(True)
        self.geometry('690x440')

        # < --- Topbar --- > 
        TopBarFrame = customtkinter.CTkFrame(self, width = 690, height=30, fg_color= black, corner_radius=0)
        TopBarFrame.place(relx = 0, rely = 0)

        TopBarFrame.bind('<ButtonPress-1>', self.drag)
        TopBarFrame.bind('<B1-Motion>', self.move)
        TopBarFrame.bind('<ButtonRelease-1>', self.stop)
        
        Line = self.divline(self, 0.067, self.green_line)
        
        Title = customtkinter.CTkLabel(TopBarFrame, text='Astri@Hider', text_color = white, font = ('Papyrus', 19))
        Title.place(relx = 0.02)

        Close = customtkinter.CTkButton(TopBarFrame, text = '✕', width = 30, height = 30, fg_color = black, hover_color = red, corner_radius = 0, command = self.close)
        Close.place(relx = 0.9558, rely = 0)
        Close.bind('<Enter>', self.mouse1)
        Close.bind('<Leave>', self.mouse0)
        
        HideButton = customtkinter.CTkButton(TopBarFrame, text = '―', width = 30, height = 30, fg_color = black, hover_color = black2, corner_radius = 0, command = None)
        HideButton.place(relx = 0.9124, rely = 0)
        HideButton.bind('<Enter>', self.mouse1)
        HideButton.bind('<Leave>', self.mouse0)

        # < --- Main frame --- > 
        InnerFrame = customtkinter.CTkFrame(self, width = 690, height = 410, fg_color = grey, corner_radius=0)
        InnerFrame.place(rely = 0.068)
        
        global MainFrame
        MainFrame = customtkinter.CTkFrame(self, width = 620, height = 350, fg_color = grey2, corner_radius = 0)
        MainFrame.place(relx = 0.05, rely = 0.13)
        
        
        # < ---------- Tools Bar --------- >
        global FilePath
        FilePath = ""
        
        global ToolsBarActive
        ToolsBarActive = False
        
        global ToolsBarFrames
        ToolsBarFrames = []
        
        global ToolsBarFrame
        ToolsBarFrame = customtkinter.CTkFrame(MainFrame, width = 620, height = 25, fg_color = grey4, corner_radius = 0)
        ToolsBarFrame.place(rely = 0, relx = 0)
        
        
        self.divline(ToolsBarFrame, 0.9, self.black_line)
        
        
        # < --- Tools Bar : File Frame --- >
        def dropdown_file_frame():
            global FileFrame
            global ToolsBarActive
            
            self.delToolsBarFrames(self)
            
            ToolsBarActive = True
            
            FileFrame.place(relx = 0.005, rely = 0.075)
            FileFrame.bind('<Enter>', self.mouse1)
            FileFrame.bind('<Leave>', self.mouse0)
                
            File1Button.place(rely = 0)
            File2Button.place(rely = 0.2)
            File3Button.place(rely = 0.4)
            File4Button.place(rely = 0.6)
            File5Button.place(rely = 0.8)
            
            self.divline(FileFrame, 0.8, self.black_line)
            
            FileFrame.lift()

        global FileFrame
        
        FileFrame = customtkinter.CTkFrame(MainFrame, width = 100, height = 100, fg_color = grey4, bg_color = grey2, corner_radius = 3)
        ToolsBarFrames.append(FileFrame)
        File1Button = customtkinter.CTkButton(FileFrame, width = 100, height=20, text = 'Default dir', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : self.openFolder(defaultPath))
        File2Button = customtkinter.CTkButton(FileFrame, width = 100, height=20, text = 'Converted dir', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : self.openFolder(convertedPath))
        File3Button = customtkinter.CTkButton(FileFrame, width = 100, height=20, text = 'Clean dir', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : self.openFolder(cleanPath))
        File4Button = customtkinter.CTkButton(FileFrame, width = 100, height=20, text = 'Keys dir', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : self.openFolder(keysPath))
        File5Button = customtkinter.CTkButton(FileFrame, width = 100, height=20, text = 'Exit', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = self.close)
        
        FileButton = customtkinter.CTkButton(ToolsBarFrame, width = 40, height = 23, fg_color=grey4, hover_color=black2, text = 'File', corner_radius=0, command = dropdown_file_frame)
        FileButton.place(relx = 0)
        
        
        # < --- Tools Bar : Help Frame --- >
        def dropdown_help_frame():
            global HelpFrame
            global ToolsBarActive
            
            self.delToolsBarFrames(self)
            
            ToolsBarActive = True
            
            HelpFrame.place(relx = 0.075, rely = 0.075)
            HelpFrame.bind('<Enter>', self.mouse1)
            HelpFrame.bind('<Leave>', self.mouse0)
                
            Help1Button.place(rely = 0)
            Help2Button.place(rely = 0.16)
            Help3Button.place(rely = 0.32)
            Help4Button.place(rely = 0.5)
            Help5Button.place(rely = 0.68)
            Help6Button.place(rely = 0.86)
            
            HelpFrame.lift()
        
        global HelpFrame
        HelpFrame = customtkinter.CTkFrame(MainFrame, width = 120, height=150, fg_color = grey4, bg_color = grey2, corner_radius=3)
        ToolsBarFrames.append(HelpFrame)
        
        Help1Button = customtkinter.CTkButton(HelpFrame, width = 120, height=20, text = 'Message Hider', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : callInfobox(notes.hider_info[0], notes.hider_info[1]))
        Help2Button = customtkinter.CTkButton(HelpFrame, width = 120, height=20, text = 'JPG Reader', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : callInfobox(notes.reader_info[0], notes.reader_info[1]))
        Help3Button = customtkinter.CTkButton(HelpFrame, width = 120, height=20, text = 'Message Encrypter', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : callInfobox(notes.encryptionmsghider_info[0], notes.encryptionmsghider_info[1]))
        Help4Button = customtkinter.CTkButton(HelpFrame, width = 120, height=20, text = 'Encrypted Reader', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : callInfobox(notes.encryptionmsgreader_info[0], notes.encryptionmsgreader_info[1]))
        Help5Button = customtkinter.CTkButton(HelpFrame, width = 120, height=20, text = 'Encryption Key', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : callInfobox(notes.encryptionkey_info[0], notes.encryptionkey_info[1]))
        Help6Button = customtkinter.CTkButton(HelpFrame, width = 120, height=20, text = 'JPG Cleaner', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : callInfobox(notes.jpgcleaner_info[0], notes.jpgcleaner_info[1]))
        HelpButton = customtkinter.CTkButton(ToolsBarFrame, width = 40, height = 23, fg_color=grey4, hover_color=black2, text = 'Help', corner_radius=0, command = dropdown_help_frame)
        HelpButton.place(relx = 0.07)

        # < --- Tools Bar : Convert Frame --- >
        def dropdown_convert_frame():
            global ConvertFrame
            global ToolsBarActive
            
            self.delToolsBarFrames(self)
            
            ToolsBarActive = True
            
            ConvertFrame.place(relx = 0.14, rely = 0.075)
            ConvertFrame.bind('<Enter>', self.mouse1)
            ConvertFrame.bind('<Leave>', self.mouse0)
                
            Convert1Button.place(rely = 0)
            Convert2Button.place(rely = 0.5)
            
            ConvertFrame.lift()

        global ConvertFrame
        
        ConvertFrame = customtkinter.CTkFrame(MainFrame, width = 100, height = 50, fg_color = grey4, bg_color = grey2, corner_radius=3)
        ToolsBarFrames.append(ConvertFrame)
        
        Convert1Button = customtkinter.CTkButton(ConvertFrame, width = 100, height=20, text = 'Convert File', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = modules.converter)
        Convert2Button = customtkinter.CTkButton(ConvertFrame, width = 100, height=20, text = 'Open Dir', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda : self.openFolder(convertedPath))

        ConvertButton = customtkinter.CTkButton(ToolsBarFrame, width = 40, height = 23, fg_color=grey4, hover_color=black2, text = 'Convert', corner_radius=0, command = dropdown_convert_frame)
        ConvertButton.place(relx = 0.14)
        
        
        # < --- Tools Bar : Settings Page --- >
        def settingsPage():
            self.delFrames()
            
            winSettings = customtkinter.CTkLabel(MainFrame, width=100, height=30, text = 'Window', font = self.font2)
            winSettings.place(relx = 0.01, rely = 0.1)
            
            setbutton = customtkinter.CTkSwitch(MainFrame, width=50, height=20, text = 'Always on top', command = self.changeOntop, onvalue=1, offvalue=0, progress_color=green)
            setbutton.place(relx = 0.06, rely = 0.2)
            setbutton.select() if ontop else setbutton.deselect()
            
            dirSettings = customtkinter.CTkLabel(MainFrame, width=100, height=30, text = 'Directories', font = self.font2)
            dirSettings.place(relx = 0.045, rely = 0.3)
            
            defaultBox = customtkinter.CTkTextbox(MainFrame, width = 300, height = 28, corner_radius=3, activate_scrollbars=False)
            defaultBox.place(relx = 0.22, rely = 0.4)
            defaultBox.insert('0.0', defaultPath)
            
            changeDefault = customtkinter.CTkButton(MainFrame, width = 100, height = 27, text = 'Default', text_color = black, image = self.folder_btn, anchor = 'w',  corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = lambda : self.changeDir(defaultBox, defaultPath, 'defaultPath'))
            changeDefault.place(relx = 0.05, rely = 0.4)
            
            
            convertedBox = customtkinter.CTkTextbox(MainFrame, width = 300, height = 28, corner_radius=3, activate_scrollbars=False)
            convertedBox.place(relx = 0.22, rely = 0.55)
            convertedBox.insert('0.0', convertedPath)
            
            changeConverted = customtkinter.CTkButton(MainFrame, width = 100, height = 27, text = 'Converted', text_color = black, image = self.folder_btn, anchor = 'w',  corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = lambda : self.changeDir(convertedBox, convertedPath, 'convertedPath'))
            changeConverted.place(relx = 0.05, rely = 0.55)
            
            
            cleanBox = customtkinter.CTkTextbox(MainFrame, width = 300, height = 28, corner_radius=3, activate_scrollbars=False)
            cleanBox.place(relx = 0.22, rely = 0.7)
            cleanBox.insert('0.0', cleanPath)
            
            changeClean = customtkinter.CTkButton(MainFrame, width = 100, height = 27, text = 'Clean', text_color = black, image = self.folder_btn, anchor = 'w',  corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = lambda : self.changeDir(cleanBox, cleanPath, 'cleanPath'))
            changeClean.place(relx = 0.05, rely = 0.7)
            
            for _ in [defaultBox, convertedBox, cleanBox]: _.configure(state = 'disabled')
            
            
            HomeButton = customtkinter.CTkButton(MainFrame, width = 100, height = 30, text = 'Home', text_color= black, image = self.home_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = mainMenu)
            HomeButton.place(relx = 0.42, rely = 0.85)
        
        
        SettingsButton = customtkinter.CTkButton(ToolsBarFrame, width = 40, height = 23, fg_color=grey4, hover_color=black2, text = 'Settings', corner_radius=0, command = settingsPage)
        SettingsButton.place(relx = 0.23)


        # < --- Tools Bar : Credits --- >
        def dropdown_credits_frame():
            global CreditsFrame
            global ToolsBarActive
            
            self.delToolsBarFrames(self)
            
            ToolsBarActive = True
            
            CreditsFrame.place(relx = 0.33, rely = 0.075)
            CreditsFrame.bind('<Enter>', self.mouse1)
            CreditsFrame.bind('<Leave>', self.mouse0)
            
            Credit1_button.place(rely = 0)
            Credit2_button.place(rely = 0.32)
            Credit3_button.place(rely = 0.65)
            
            self.divline(CreditsFrame, 0.32, self.black_line)
            
            CreditsFrame.lift()
        
        global CreditsFrame
        CreditsFrame = customtkinter.CTkFrame(MainFrame, width = 100, height=69, fg_color = grey4, bg_color = grey2, corner_radius=3)
        ToolsBarFrames.append(CreditsFrame)
        Credit1_button = customtkinter.CTkButton(CreditsFrame, width = 100, height=23, text = '🔗 Discord ', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda: webbrowser.open(notes.discord_invite))
        Credit2_button = customtkinter.CTkButton(CreditsFrame, width = 100, height=23, text = '@astros3x ', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda: webbrowser.open(notes.github[0]))
        Credit3_button = customtkinter.CTkButton(CreditsFrame, width = 100, height=23, text = '@captainbeluga ', anchor = 'w', corner_radius = 0, fg_color = grey4, hover_color = black2, command = lambda: webbrowser.open(notes.github[1]))
        
        CreditsButton = customtkinter.CTkButton(ToolsBarFrame, width = 40, height = 23, fg_color  = grey4, hover_color=  black2, text = 'Credits', corner_radius=0, command = dropdown_credits_frame)
        CreditsButton.place(relx = 0.33)
        
        VersionLabel = customtkinter.CTkLabel(ToolsBarFrame, width = 40, height = 23, fg_color = grey4, text = f'v{hiderVersion}')
        VersionLabel.place(relx = 0.93)
        
        MenuButtons = []
    
        def hideMessagePage():
            self.delFrames()
            
            FileInput = customtkinter.CTkEntry(MainFrame, width = 280, height = 40, placeholder_text = 'File path...', corner_radius = 3, border_width = 1)
            FileInput.place(relx = 0.24, rely = 0.3)
            
            LoadFile = customtkinter.CTkButton(MainFrame, width = 40, height = 40, text = None, image = self.upload_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = lambda : self.loadFile(FileInput))
            LoadFile.place(relx = 0.69, rely = 0.3)
            
            MessageInput = customtkinter.CTkEntry(MainFrame, width = 319, height = 40, placeholder_text = 'Message to hide...', corner_radius = 3, border_width = 1)
            
            MessageInput.place(relx = 0.24, rely = 0.45)
            
            encPwLabel  = customtkinter.CTkLabel(MainFrame, width = 100, height = 25, text = 'Encryption: ', text_color = white, font = self.font1)
            encPwLabel.place(relx = 0.24, rely = 0.6)
            
            EncryptedPW = customtkinter.CTkOptionMenu(MainFrame, width = 200, height = 25, fg_color = grey4, text_color=white, button_color=green2, button_hover_color=green, values = keysList)
            EncryptedPW.place(relx = 0.43, rely = 0.6)
            
            HomeButton = customtkinter.CTkButton(MainFrame, width = 30, height = 30, text = None, image = self.home_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = mainMenu)
            HomeButton.place(relx = 0.24, rely = 0.85)
            
            HideButton = customtkinter.CTkButton(MainFrame, width = 245, height = 30, text = 'Hide message', text_color = white, corner_radius = 3, border_width = 1,  border_color = green,
                                               fg_color = grey5, hover_color = grey6, command = lambda : modules.writer(FileInput.get(), MessageInput.get(), keysPath, EncryptedPW.get(), defaultPath))
            HideButton.place(relx = 0.3, rely = 0.85)   
            
            ClearButton = customtkinter.CTkButton(MainFrame, width = 30, height = 30, text = None, image = self.clear_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = lambda : [self.cleanEntry(FileInput), self.cleanEntry(MessageInput)])
            ClearButton.place(relx = 0.705, rely = 0.85)       
                
            
        def messageReaderPage():
            self.delFrames()
            
            FileInput = customtkinter.CTkEntry(MainFrame, width = 280, height = 40, placeholder_text = 'File path...', corner_radius = 3, border_width = 1)
            FileInput.place(relx = 0.24, rely = 0.13)
            
            LoadFile = customtkinter.CTkButton(MainFrame, width = 40, height = 40, text = None, image = self.upload_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = lambda : self.loadFile(FileInput))
            LoadFile.place(relx = 0.69, rely = 0.13)
            
            mTextBox = customtkinter.CTkTextbox(MainFrame, width = 319, height = 135, corner_radius = 3, border_width = 1)
            
            mTextBox.place(relx = 0.24, rely = 0.3)
        
            encPwLabel  = customtkinter.CTkLabel(MainFrame, width = 100, height = 25, text = 'Encryption: ', text_color = white, font = self.font1)
            encPwLabel.place(relx = 0.24, rely = 0.735)
            
            EncryptedPW = customtkinter.CTkOptionMenu(MainFrame, width = 200, height = 25, fg_color = grey4, text_color=white, button_color=green2, button_hover_color=green,
                                                      values = keysList)
            EncryptedPW.place(relx = 0.43, rely = 0.735)
            
            HomeButton = customtkinter.CTkButton(MainFrame, width = 30, height = 30, text = None, image = self.home_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = mainMenu)
            HomeButton.place(relx = 0.24, rely = 0.85)
            
            HideButton = customtkinter.CTkButton(MainFrame, width = 245, height = 30, text = 'Read message', text_color = white, corner_radius = 3, border_width = 1,  border_color = green,
                                               fg_color = grey5, hover_color = grey6, command = lambda : self.callReader(FileInput.get(), keysPath, EncryptedPW.get(), mTextBox))
            HideButton.place(relx = 0.3, rely = 0.85)
            
            ClearButton = customtkinter.CTkButton(MainFrame, width = 30, height = 30, text = None, image = self.clear_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = lambda : [self.cleanTextbox(mTextBox), self.cleanEntry(FileInput)])
            ClearButton.place(relx = 0.705, rely = 0.85)
         
        global genEncryptionKeyPage
        def genEncryptionKeyPage():
            self.delFrames()
            
            
            keyName = customtkinter.CTkEntry(MainFrame, width = 320, height = 40, placeholder_text = 'Key file name...', corner_radius = 3, border_width = 1)
            keyName.place(relx = 0.24, rely = 0.4)

            global EncryptedPW
            EncryptedPW = customtkinter.CTkOptionMenu(MainFrame, width = 200, height = 25, fg_color = grey4, text_color=white, button_color=green2, button_hover_color=green, values = keysList)
            EncryptedPW.place(relx = 0.24, rely = 0.6)
            
            delPwButton = customtkinter.CTkButton(MainFrame, width = 100, height = 25, text='Delete', text_color = black, fg_color = green2, hover_color=green,
                                                     border_width = 1, border_color=black, command = lambda : self.delKey(EncryptedPW.get()))
            delPwButton.place(relx = 0.595, rely = 0.6)
            
            HomeButton = customtkinter.CTkButton(MainFrame, width = 30, height = 30, text = None, image = self.home_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = mainMenu)
            HomeButton.place(relx = 0.24, rely = 0.85)
            
            
            GenButton = customtkinter.CTkButton(MainFrame, width = 245, height = 30, text = 'Generate new key', text_color = white, corner_radius = 3, border_width = 1,  border_color = green,
                                               fg_color = grey5, hover_color = grey6, command = lambda : self.callKeyGen(keyName.get()))
            GenButton.place(relx = 0.3, rely = 0.85)   
            
            ClearButton = customtkinter.CTkButton(MainFrame, width = 30, height = 30, text = None, image = self.clear_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = lambda : self.cleanEntry(KeyWord))
            ClearButton.place(relx = 0.705, rely = 0.85)
            
        
        def jpgCleanerPage():
            self.delFrames()
            
            FileInput = customtkinter.CTkEntry(MainFrame, width = 280, height = 40, placeholder_text = 'File path...', corner_radius = 3, border_width = 1)
            FileInput.place(relx = 0.24, rely = 0.4)
                        
            FolderButton = customtkinter.CTkButton(MainFrame, width = 40, height = 40, text = None, image = self.folder_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = lambda : self.loadFile(FileInput))
            FolderButton.place(relx = 0.69, rely = 0.4)
            
            HomeButton = customtkinter.CTkButton(MainFrame, width = 30, height = 30, text = None, image = self.home_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = mainMenu)
            HomeButton.place(relx = 0.24, rely = 0.85)
            
            GenButton = customtkinter.CTkButton(MainFrame, width = 245, height = 30, text = 'Clean', text_color = white, corner_radius = 3, border_width = 1,  border_color = green,
                                               fg_color = grey5, hover_color = grey6, command = lambda : modules.cleaner(FileInput.get(), cleanPath))
            GenButton.place(relx = 0.3, rely = 0.85)   
            
            ClearButton = customtkinter.CTkButton(MainFrame, width = 30, height = 30, text = None, image = self.clear_btn, corner_radius = 3, border_width = 1,  border_color = black,
                                               fg_color = green2, hover_color = green, command = lambda : self.cleanEntry(FileInput))
            ClearButton.place(relx = 0.705, rely = 0.85)
         
         
        def mainMenu():
            self.delFrames()
               
            HideMessageButton = customtkinter.CTkButton(MainFrame, width = 250, height = 27, text="Message Hider", text_color = black, fg_color = green2, hover_color=green,
                                                        border_width = 1, border_color=black, command = hideMessagePage)    
            HideMessageButton.place(relx = 0.28, rely  = 0.2)
            MenuButtons.append(HideMessageButton)

            ReadJPEGButton = customtkinter.CTkButton(MainFrame, width = 250, height = 27, text="JPG Reader", text_color = black, fg_color = green2, hover_color=green,
                                                     border_width = 1, border_color=black, command = messageReaderPage)  
            ReadJPEGButton.place(relx = 0.28, rely  = 0.4)
            MenuButtons.append(ReadJPEGButton)
            
            EncryptionKeyButton = customtkinter.CTkButton(MainFrame, width = 250, height = 27, text = "Encryption Key", text_color = black, fg_color = green2, hover_color = green,
                                                          border_width = 1, border_color=black,  command = genEncryptionKeyPage)
            EncryptionKeyButton.place(relx = 0.28, rely  = 0.6)
            MenuButtons.append(EncryptionKeyButton)
            
            JPEGCleanerButton = customtkinter.CTkButton(MainFrame, width = 250, height = 27, text = "JPG Cleaner", text_color = black, fg_color = green2, hover_color = green,
                                                        border_width = 1, border_color=black, command = jpgCleanerPage)
            JPEGCleanerButton.place(relx = 0.28, rely  = 0.8)
            MenuButtons.append(JPEGCleanerButton)
        
        mainMenu()
           
        # < --- Interactions --- >
        InnerFrame.bind('<ButtonPress-1>', lambda event: self.delToolsBarFrames(self))
        MainFrame.bind('<ButtonPress-1>', lambda event: self.delToolsBarFrames(self))
        
        for btn in MenuButtons: 
            btn.bind('<Enter>', self.mouse1)
            btn.bind('<Leave>', self.mouse0)
    
  
    # < --- Load file in the entry --- >
    def loadFile(self, entry):
        filePath = filedialog.askopenfilename(title = 'Astri@Hider | Load image', filetypes = [('File JPG', '.jpg')])
        if not filePath:
            return None
        else:
            if entry.get():
                entry.delete(0, customtkinter.END)
            entry.insert(0, filePath)
            self.focus()
    

    def openFolder(self, path):
        os.startfile(path)
    
    
    def close(self):
        #if messagebox.askokcancel('Exit', 'Are you sure to close Astri@Hider?'):
        #    sys.exit()
        sys.exit()
         
         
    def reloadKeys(self):
        keysList.clear()
        keysList.append('None')
        for filename in os.listdir(keysPath):
            if os.path.isfile(os.path.join(keysPath, filename)):
                keysList.append(os.path.splitext(filename)[0])
    
    def delToolsBarFrames(self, event):
        self.focus()
        global ToolsBarActive
        if ToolsBarActive:
            try:
                for _ in ToolsBarFrames:
                    _.place_forget()
            except:
                pass
    
    
    def delFrames(self):
        global MainFrame
        global ToolsBarFrame
        
        for _ in MainFrame.winfo_children():
            if _ is not ToolsBarFrame:
                _.place_forget()
    
    
    def delKey(self, keyName):
        if keyName != 'None':
            try:
                os.remove(f'{keysPath}{keyName}.txt' )
                self.reloadKeys()
                self.delFrames()
                genEncryptionKeyPage()
            except Exception as e:
                callErrorbox('Error', e)
    
                
    def cleanTextbox(self, textbox):
        textbox.delete("0.0", customtkinter.END)
    
    
    def cleanEntry(self, entry):
        entry.delete(0, customtkinter.END)
        entry.focus()
        self.focus()
    
    
    def mouse0(self, event):
        self.config(cursor='')


    def mouse1(self, event):
        self.config(cursor='hand2')


    def drag(self, event):
        self._x = event.x
        self._y = event.y


    def move(self, event):
        new_x = self.winfo_x() - self._x + event.x
        new_y = self.winfo_y() - self._y + event.y
        self.geometry(f'+{new_x}+{new_y}')


    def stop(self, event): 
        self.geometry(f'+{self.winfo_x()}+{self.winfo_y()}')


    def divline(self, master, _y, img):
        return customtkinter.CTkLabel(master, height=1, text = None, image = img).place(rely = _y)


    def changeOntop(self):
        global ontop
        
        if ontop:
            self.attributes('-topmost', False)
            ontop = 0
        else:
            self.attributes('-topmost', True)
            ontop = 1
            
        settings['onTop'] = ontop

        with open(settingsPath, 'w') as file:
            json.dump(settings, file, indent = 4)
        
        self.update()
    
    
    def changeDir(self, textbox, newdir, path):
        newDir = filedialog.askdirectory(title='Interested dir')
        
        if not newDir:
            return None
        
        else:
            textbox.configure(state = "normal")
            textbox.delete("0.0", customtkinter.END)
            textbox.insert('0.0', newDir)
            textbox.configure(state = "disabled")
            
            directories[path] = newDir
            
            with open(directoriesPath, 'w') as file:
                json.dump(directories, file, indent = 4)

            self.update()


    def callReader(self, filePath, keysPath, encryption, textBox):
        text = modules.reader(filePath, keysPath, encryption)
        textBox.delete("0.0", customtkinter.END)
        textBox.insert("0.0", text)


    def callKeyGen(self, fileName):
        keyName = key.keygen(keysPath, fileName)
        key.db_mixer()
        
        self.reloadKeys()
        self.update()
        
    
    font1 = ('Fixedsys', 10)
    font2 = ('Fixedsys', 20)
    
    assetsPath = 'data\\assets\\'
    green_line = customtkinter.CTkImage(Image.open(assetsPath + 'green_line.png'), size=(690, 1))
    black_line = customtkinter.CTkImage(Image.open(assetsPath + 'black_line.png'), size=(620, 1))
    upload_btn = customtkinter.CTkImage(Image.open(assetsPath + 'upload.png'), size = (20, 20))
    folder_btn = customtkinter.CTkImage(Image.open(assetsPath + 'folder.png'), size = (20, 20))
    home_btn = customtkinter.CTkImage(Image.open(assetsPath + 'home.png'), size = (17, 17))
    clear_btn = customtkinter.CTkImage(Image.open(assetsPath + 'clear.png'), size = (17, 17))


if __name__ == '__main__':
    
    def callInfobox(title, msg):
        return messagebox.showinfo(title, msg)

    def callErrorbox(title, msg):
        return messagebox.showerror(title, msg)

    
    # < --- Assets checker --- >
    version = '2.1.0'

    red = '#f23f42'
    black = '#000000'
    black2 = '#242423'
    white = '#ffffff'
    grey = '#2b2b2b'
    grey2 = '#333333'
    grey3 = '#646d77'
    grey4 = '#1f1f1f'
    grey5 = '#343638'
    grey6 = '#565b5e'
    green = '#38b000'
    green2 = '#70e000'

    folders = [
        'data', 
        
        'data\\assets',
        
        'data\\configuration',
        
        'data\\modules',
        'data\\modules\\encryption',
        'data\\modules\\encryption\\keys',
        
        'data\\requirements',
        
        'data\\results',
        'data\\results\\clean',
        'data\\results\\converted',
        'data\\results\\default',
    ]
    
    files = [
        'data\\assets\\black_line.png',
        'data\\assets\\green_line.png',
        'data\\assets\\folder.png',
        'data\\assets\\upload.png',
        'data\\assets\\clear.png',
        'data\\assets\\home.png',
        
        'data\\configuration\\directories.json',
        'data\\configuration\\settings.json',
        
        'data\\modules\\encryption\\db_base.json',
        
        'data\\modules\\cb_rsa.py',
        'data\\modules\\key.py',
        'data\\modules\\modules.py',
        'data\\modules\\notes.py',
        
        'data\\requirements\\install.py',
        'data\\requirements\\requirements.txt',
    ]


    def assetsDownloader():
        try:
            os.remove('data')
        except:
            os.system(f"mkdir data > NUL 2>&1")

        for x in files:
            x = x.replace("\\","/")
            r = requests.get(f"https://raw.githubusercontent.com/astros3x/astri-hider/main/{x}")
            open(x, "wb").write(r.content)

    def foldersChecker():
        for x in folders:
            if not os.path.exists(x): 
                os.system(f"mkdir {x} > NUL 2>&1")


    def assetsChecker():
        try:
            for x in files:
                open(x)
                
            return True
        
        except FileNotFoundError:
            return False


    #Version check
    try:
        r = requests.get('https://raw.githubusercontent.com/astros3x/astri-hider/main/version.txt').text.strip()

        if r != version:
            if messagebox.askokcancel('Update Available', 'A new version is available. Wanna download it?'):
                webbrowser.open(release)

    except Exception as e:
        callErrorbox('ERROR', "Version check failed http error / offline.\nPress 'Ok' to continue.")

    #Assets check
    try:
        foldersChecker()
                
        if not assetsChecker():
            try: 
                assetsDownloader()
            except Exception as e:
                callErrorbox('Assets download error', e)
    
    except Exception as e:
        callErrorbox('Assets download error', e)
        
        
    
    # < --- Load configuration --- >
    
    from data.modules import notes, key, modules
    
    keysList = ['None']
    keysPath = 'data\\modules\\encryption\\keys\\'
    
    for filename in os.listdir(keysPath):
        if os.path.isfile(os.path.join(keysPath, filename)):
            keysList.append(os.path.splitext(filename)[0])

    directoriesPath = 'data\\configuration\\directories.json'
    with open(directoriesPath) as file:
        directories = json.load(file)
        
    defaultPath = directories['defaultPath']
    convertedPath = directories['convertedPath']
    cleanPath = directories['cleanPath']
    
    
    settingsPath = 'data\\configuration\\settings.json'
    with open(settingsPath) as file:
        settings = json.load(file)

    ontop = settings['onTop']

    
    App().mainloop()