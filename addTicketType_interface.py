#! /usr/bin/env python3
# coding: utf-8

from tkinter import *


class AddTicketTypeInterface(Frame):

    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, **kwargs)
        self.pack(fill=BOTH)
        self.choice = "0"
        self['bg'] = '#282b30'
        self.reference_saisi = StringVar()
        self.name_saisi = StringVar()
        self.price_saisi = StringVar()
        self.solde_saisi = StringVar()

        self.champ_label = Label(self, text="Ajouter un ticket", bg='#282b30', font=("Helvetica", 16, 'bold'), fg = 'white')
        self.champ_label.pack(pady=30)

        self.name_label = Label(self, text="Référence", bg='#282b30', font=("Helvetica", 12), fg = 'white')
        self.name_label.pack(pady=5)

        self.ligne_reference = Entry(self, textvariable=self.reference_saisi, bg='white', font=("Helvetica", 12), width=25)
        self.ligne_reference.pack(pady=5)

        self.username_label = Label(self, text="Désignation", bg='#282b30', font=("Helvetica", 12), fg = 'white')
        self.username_label.pack(pady=5)

        self.ligne_name = Entry(self, textvariable=self.name_saisi, bg='white', font=("Helvetica", 12), width=25)
        self.ligne_name.pack(pady=5)

        self.password_label = Label(self, text="Prix unitaire", bg='#282b30', font=("Helvetica", 12), fg = 'white')
        self.password_label.pack(pady=5)

        self.ligne_price = Entry(self, textvariable=self.price_saisi, width=25, bg='white', font=("Helvetica", 12))
        self.ligne_price.pack(pady=5)

        self.solde_label = Label(self, text="Solde", bg='#282b30', font=("Helvetica", 12), fg='white')
        self.solde_label.pack(pady=5)

        self.ligne_solde = Entry(self, textvariable=self.solde_saisi, width=25, bg='white', font=("Helvetica", 12))
        self.ligne_solde.pack(pady=5)

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
    p_interface = AddTicketTypeInterface(window)
    img = PhotoImage(file='.\images\logo.png')
    p_interface.mainloop()
    p_interface.destroy()
    window.destroy()


if __name__.endswith('__main__'):
    main()