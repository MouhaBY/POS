#! /usr/bin/env python3
# coding: utf-8

from tkinter import *

import Menu
import DatabaseScripts

def initialise_s_window(window):
    window.minsize(width=300, height=250)
    window.title("POINT OF SALE by MBY")
    window.wm_iconbitmap('.\images\ico.ico')
    #window['bg'] = '#282b30'


class PosInterface(Frame):

    def __init__(self, **kwargs):
        Frame.__init__(self, **kwargs)
        self.pack(fill=BOTH)
        self.choice = "0"
        #self['bg'] = '#F0F0ED'

        self.products_frame = Frame(self, bd=0, bg='green')
        self.champ_1 = Label(self.products_frame, bg=self.products_frame['bg'], text="Choix du type de tickets", font=("Helvetica", 16), fg='#1e2124')
        self.champ_1.pack(padx=5, pady=5)
        self.tickets_list = DatabaseScripts.read_tickettypes()
        for i in self.tickets_list:
            self.tickets_button = Button(self.products_frame, height=2, bd=0,
                                          text= i[1], command=self.quit,
                                         font=("Helvetica", 14), fg='black')
            self.tickets_button.pack(ipadx=5, padx=10, pady=20, side=LEFT)
        self.products_frame.pack(fill=BOTH, expand=True)

        self.list_frame = Frame(self, bd=0, bg='blue')
        self.champ_2 = Label(self.list_frame, bg=self.list_frame['bg'], text="Détails de la vente en cours", font=("Helvetica", 16), fg='#1e2124')
        self.champ_2.pack(padx=5, pady=5)
        self.list_frame.pack(fill=BOTH, expand=True)

        self.sell_frame = Frame(self, bd=0, bg='yellow')
        self.champ_3 = Label(self.sell_frame, bg=self.sell_frame['bg'], text="Informations du client", font=("Helvetica", 16), fg='#1e2124')
        self.champ_3.pack(padx=5, pady=5)
        self.sell_frame.pack(fill=X, expand=True)


def main():
    DatabaseScripts.db_file = r".\POS.db"
    window = Tk()
    window.attributes('-fullscreen', True)
    p_interface = Menu.InterfaceMenu(window)
    p_interface.champ_application["text"] = "Point de vente"
    p_interface.content_frame = PosInterface()
    p_interface.mainloop()


if __name__.endswith('__main__'):
    main()