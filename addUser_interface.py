#! /usr/bin/env python3
# coding: utf-8

from tkinter import *


class AddUserInterface(Frame):

    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, **kwargs)
        self.pack(fill=BOTH)
        self.choice = "0"
        self['bg'] = '#282b30'
        self.username_saisi = StringVar()
        self.password_saisi = StringVar()
        self.nomContact_saisi = StringVar()
        self.profil_saisi = StringVar()
        profil_list = ("Administrateur", "Superviseur", "Caissier")

        self.champ_label = Label(self, text="Ajouter un utilisateur", bg='#282b30', font=("Helvetica", 16, 'bold'), fg = 'white')
        self.champ_label.pack(pady=30)

        self.profile_label = Label(self, text="Profil", bg='#282b30', font=("Helvetica", 12), fg='white')
        self.profile_label.pack(pady=5)

        self.optionmenu_widget = OptionMenu(self, self.profil_saisi, *profil_list)
        self.optionmenu_widget.config(width=25, font=('Helvetica', 12), fg='white', bg='#282b30')
        self.optionmenu_widget.pack(pady=5, padx=60)

        self.name_label = Label(self, text="Nom du contact", bg='#282b30', font=("Helvetica", 12), fg = 'white')
        self.name_label.pack(pady=5)

        self.ligne_NomContact = Entry(self, textvariable=self.nomContact_saisi, bg='white', font=("Helvetica", 12), width=25)
        self.ligne_NomContact.pack(pady=5)

        self.username_label = Label(self, text="Nom d'utilisateur", bg='#282b30', font=("Helvetica", 12), fg = 'white')
        self.username_label.pack(pady=5)

        self.ligne_username = Entry(self, textvariable=self.username_saisi, bg='white', font=("Helvetica", 12), width=25)
        self.ligne_username.pack(pady=5)

        self.password_label = Label(self, text="Mot de passe", bg='#282b30', font=("Helvetica", 12), fg = 'white')
        self.password_label.pack(pady=5)

        self.ligne_password = Entry(self, textvariable=self.password_saisi, width=25, show='*', bg='white', font=("Helvetica", 12))
        self.ligne_password.pack(pady=5)

        self.add_button = Button(self, text="Enregistrer", command=self.saveclick, width=12,height=1, bg='green', bd=0, highlightbackground='green', font=("Helvetica", 10, 'bold'), fg = 'white')
        self.add_button.pack(padx=5, pady=5)

        self.back_button = Button(self, text="Annuler", command=self.backclick, width=12,height=1, bg='#e53e1e', bd=0, highlightbackground='#7289da', font=("Helvetica", 10, 'bold'), fg = 'white')
        self.back_button.pack(padx=5, pady=5)

        self.inform_label = Label(self, text="", bg='#282b30')
        self.inform_label.pack()

    def backclick(self):
        self.choice = "back"
        self.quit()

    def saveclick(self):
        self.choice = "save"
        self.quit()


def main():
    window = Tk()
    p_interface = AddUserInterface(window)
    img = PhotoImage(file='.\images\logo.png')
    p_interface.mainloop()
    p_interface.destroy()
    window.destroy()


if __name__.endswith('__main__'):
    main()