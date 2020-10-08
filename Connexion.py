#! /usr/bin/env python3
# coding: utf-8

from tkinter import *

import hashlib

import DatabaseScripts


def log_in(username, password):
    _unlocked = 0
    # encode password recu pour avoir un type bytes
    password_encode = password.encode()
    password_encode = hashlib.sha1(password_encode).hexdigest()
    # get username AND password chiffre from database
    data = DatabaseScripts.check_user(username)
    # verifie que data non null
    if data is not None:
        # test username password if correct
        password_hash = data
        if password_encode == password_hash:
            _unlocked = 1
    # return result
    if _unlocked:
        return 1
    else:
        return 0


class InterfaceConnexion(Frame):
    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, **kwargs)
        self.pack(fill=Y)
        self['bg'] = '#282b30'

        self.username = StringVar()
        self.password = StringVar()
        self.authorized = 0
        self.choice = "1"

        self.champ_vide1 = Label(self, bg='#1e2124', height=10)
        self.champ_vide1.pack(fill=BOTH, )

        self.champ_label = Label(self, bg='#282b30', text="Connexion", font=("Helvetica", 18, 'bold'), fg = 'white')
        self.champ_label.pack(padx=90, pady=30, fill=BOTH)

        img = PhotoImage(file=".\images\logo.png")
        self.champ_logo = Label(self, image=img, bd=0, bg='#282b30')
        self.champ_logo.image = img  # keep a reference
        self.champ_logo.pack(fill=X, expand=True,pady=25)

        self.champ_label1 = Label(self, bg='#282b30', text="Nom d'utilisateur",  font=("Helvetica", 12), fg = 'white')
        self.champ_label1.pack(pady=4)

        self.ligne_texte1 = Entry(self, bg='white', textvariable=self.username, font=("Helvetica", 12), width=20)
        self.ligne_texte1.pack(pady=4, padx=20, fill=X)
        self.ligne_texte1.focus_set()

        self.champ_label2 = Label(self, bg='#282b30', text="Mot de passe", font=("Helvetica", 12), fg='white')
        self.champ_label2.pack(pady=4)

        self.ligne_texte2 = Entry(self, bg='white', textvariable=self.password, font=("Helvetica", 12), width=20, show='*')
        self.ligne_texte2.pack(pady=2, padx=20, fill=X)

        self.champ_label3 = Label(self, bg='#282b30', text=" ", font=("Helvetica", 10, 'bold'), fg='white')
        self.champ_label3.pack(pady=2)

        self.buttons_frame = Frame(self, bg='#282b30')
        self.close_button = Button(self.buttons_frame, width=12, height=2, bg='#e53e1e', bd=0, highlightbackground='#7289da', text="Quitter", command=self.quit_function, font=("Gotham SSm A", 11, 'bold'), fg='white')
        self.close_button.pack(ipadx=2, padx=8, pady=7, side=RIGHT)
        self.connect_button = Button(self.buttons_frame, width=12,height=2, bg='#0084bd', bd=0, highlightbackground='#0084bd', text="Se connecter", command=self.test_connexion, font=("Gotham SSm A", 11, 'bold'), fg = 'white')
        self.connect_button.pack(ipadx=2, padx=8, pady=7, side=RIGHT)
        self.buttons_frame.pack(fill=X, expand=False, padx=40, pady=30)

        # self.champ_vide2 = Label(self, bg='#282b30')
        # self.champ_vide2.pack(padx=20, pady=10, fill=BOTH)

    def test_connexion(self):
        if log_in(self.username.get(), self.password.get()):
            self.champ_label3["text"] = "Connexion réussie"
            self.champ_label3["fg"] = 'white'
            self.authorized = 1
            self.quit()
        else:
            self.champ_label3["text"] = "Données erronées"
            self.champ_label3["fg"] = '#e53e1e'

    def quit_function(self):
        self.choice = "stop"
        self.quit()