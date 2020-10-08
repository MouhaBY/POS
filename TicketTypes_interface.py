#! /usr/bin/env python3
# coding: utf-8

from tkinter import *

import Menu
import DatabaseScripts
import addTicketType_interface
import TicketList_interface
import TicketTypes


def initialise_s_window(window):
    window.minsize(width=300, height=250)
    window.title("POINT OF SALE by MBY")
    window.wm_iconbitmap('.\images\ico.ico')
    window['bg'] = '#282b30'


class TicketTypesInterface(Frame):

    def __init__(self, **kwargs):
        Frame.__init__(self, **kwargs)
        self.pack(fill=BOTH)
        self.choice = "0"
        self['bg'] = '#F0F0ED'

        self.list_frame = Frame(self, bd=0, )
        self.list_frame.pack(fill=BOTH, expand=True)

        self.buttons_frame = Frame(self, bd=0)
        self.vide3 = Label(self.buttons_frame)
        self.vide3.pack(side=RIGHT, padx=40, pady=25)
        self.delete_button = Button(self.buttons_frame, text="Supprimer", command=self.delete_click, width=10, height=2, bg='#FF6347', bd=0, highlightbackground='#7289da',font=("Helvetica", 10, 'bold'), fg='white')
        self.delete_button.pack(side=RIGHT, padx=3, pady=25)
        self.edit_button = Button(self.buttons_frame, text="Modifier", command=self.edit_click, width=10, height=2, bg='SteelBlue', bd=0, highlightbackground='#7289da',font=("Helvetica", 10, 'bold'), fg='white')
        self.edit_button.pack(side=RIGHT, padx=3, pady=25)
        self.add_button = Button(self.buttons_frame, text="Ajouter", command=self.add_click, width=10, height=2, bg='MediumSeaGreen', bd=0, highlightbackground='green',font=("Helvetica", 10, 'bold'), fg='white')
        self.add_button.pack(side=RIGHT, padx=3, pady=25)
        self.champ_information = Label(self.buttons_frame, text="", fg='green')
        self.champ_information.pack(side=LEFT, padx=25, pady=25)
        self.buttons_frame.pack(fill=X, expand=True)

    def add_click(self):
        self.choice = "add_ticketType"
        w = Toplevel()
        initialise_s_window(w)
        secondary_interface = addTicketType_interface.AddTicketTypeInterface(w)
        w.mainloop()
        _response = 0
        # Enregistrement d'utilisateur
        if secondary_interface.choice == "save":
            while not _response:
                # Recupere les valeurs du formulaire
                reference_value = secondary_interface.reference_saisi.get()
                name_value = secondary_interface.name_saisi.get()
                price_value = secondary_interface.price_saisi.get()
                solde_value = secondary_interface.solde_saisi.get()
                # Creation de l'objet et insertion dans la base
                ticket_to_add = TicketTypes.TicketTypes(reference_value, name_value, price_value, solde_value)
                _response = ticket_to_add.add_tickettype()
                if not _response:
                    secondary_interface.inform_label["text"] = "Référence existante"
                    secondary_interface.inform_label["fg"] = 'red'
                    secondary_interface.mainloop()
                    if secondary_interface.choice == "back":
                        break
            if _response:
                self.champ_information["text"] = "Ticket enregistré"
                self.list_frame.destroy()
                self.list_frame = TicketList_interface.TicketListInterface()
            secondary_interface.destroy()
        w.destroy()

    def edit_click(self):
        self.choice = "edit_ticketType"
        to_edit_id = self.list_frame.tree.selection()
        to_edit_reference = self.list_frame.tree.set(to_edit_id, "Référence")
        to_edit_name = self.list_frame.tree.set(to_edit_id, "Désignation")
        to_edit_price = self.list_frame.tree.set(to_edit_id, "Prix unitaire")
        to_edit_solde = self.list_frame.tree.set(to_edit_id, "Solde")
        w = Toplevel()
        initialise_s_window(w)
        secondary_interface = addTicketType_interface.AddTicketTypeInterface(w)
        secondary_interface.champ_label["text"] = "Modifier le ticket"
        secondary_interface.ligne_reference.insert(0, to_edit_reference)
        secondary_interface.ligne_name.insert(0, to_edit_name)
        secondary_interface.ligne_price.insert(0, to_edit_price)
        secondary_interface.ligne_solde.insert(0, to_edit_solde)
        w.mainloop()
        # Recupere les valeurs du formulaire
        reference_value = secondary_interface.reference_saisi.get()
        name_value = secondary_interface.name_saisi.get()
        price_value = secondary_interface.price_saisi.get()
        solde_value = secondary_interface.solde_saisi.get()
        # Creation de l'objet et edition dans la base
        ticket_to_edit = TicketTypes.TicketTypes(reference_value, name_value, price_value, solde_value)
        ticket_to_edit.edit_tickettype()
        self.champ_information["text"] = "Modifications enregistrées"
        secondary_interface.destroy()
        w.destroy()

    def delete_click(self):
        self.choice = "delete_ticketType"
        to_delete_id = self.list_frame.tree.selection()
        to_delete_value = self.list_frame.tree.set(to_delete_id, "Référence")
        DatabaseScripts.delete_tickettype(to_delete_value)
        self.quit()


def main():
    DatabaseScripts.db_file = r".\POS.db"
    window = Tk()
    window.attributes('-fullscreen', True)
    p_interface = Menu.InterfaceMenu(window)
    p_interface.champ_application["text"] = "Gestion des tickets"
    p_interface.content_frame = TicketTypesInterface()
    p_interface.content_frame.principal_frame = TicketList_interface.TicketListInterface()
    p_interface.mainloop()


if __name__.endswith('__main__'):
    main()