#! /usr/bin/env python3
# coding: utf-8

from tkinter import *

import Menu
import DatabaseScripts
import UserList_interface
import addUser_interface
import Users



def initialise_s_window(window):
    window.minsize(width=300, height=250)
    window.title("POINT OF SALE by MBY")
    window.wm_iconbitmap('.\images\ico.ico')
    window['bg'] = '#282b30'


class UsersInterface(Frame):

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
        self.delete_button = Button(self.buttons_frame, text="Supprimer", command=self.deleteclick, width=10, height=2, bg='#FF6347', bd=0, highlightbackground='#e53e1e',font=("Helvetica", 10, 'bold'), fg='white')
        self.delete_button.pack(side=RIGHT, padx=3, pady=20)
        self.edit_button = Button(self.buttons_frame, text="Modifier", command=self.editclick, width=10, height=2, bg='SteelBlue', bd=0, highlightbackground='#7289da',font=("Helvetica", 10, 'bold'), fg='white')
        self.edit_button.pack(side=RIGHT, padx=3, pady=25)
        self.add_button = Button(self.buttons_frame, text="Ajouter", command=self.addclick, width=10, height=2, bg='MediumSeaGreen', bd=0, highlightbackground='green',font=("Helvetica", 10, 'bold'), fg='white')
        self.add_button.pack(side=RIGHT, padx=3, pady=25)
        self.champ_information = Label(self.buttons_frame, text="", fg='green')
        self.champ_information.pack(side=LEFT, padx=25, pady=25)
        self.buttons_frame.pack(fill=X, expand=True)

    def addclick(self):
        self.choice = "add_user"
        w = Toplevel()
        initialise_s_window(w)
        secondary_interface = addUser_interface.AddUserInterface(w)
        w.mainloop()
        _response = 0
        # Enregistrement d'utilisateur
        if secondary_interface.choice == "save":
            while not _response:
                # Recupere les valeurs du formulaire
                contactname_value = secondary_interface.nomContact_saisi.get()
                username_value = secondary_interface.username_saisi.get()
                password_value = secondary_interface.password_saisi.get()
                profile_value= secondary_interface.profil_saisi.get()
                # Creation de l'objet et insertion dans la base
                user_to_add = Users.User(contactname_value, username_value, password_value, profile_value)
                _response = user_to_add.add_user()
                if not _response:
                    secondary_interface.inform_label["text"] = "Nom d'utilisateur existant"
                    secondary_interface.inform_label["fg"] = 'red'
                    secondary_interface.mainloop()
                    if secondary_interface.choice == "back":
                        break
            if _response:
                self.champ_information["text"] = "Utilisateur enregistré"
                self.list_frame.destroy()
                self.list_frame = UserList_interface.UserListInterface()
            secondary_interface.destroy()
        w.destroy()

    def editclick(self):
        self.choice = "edit_user"
        to_edit_id = self.list_frame.tree.selection()
        to_edit_username = self.list_frame.tree.set(to_edit_id, "Nom d'utilisateur")
        to_edit_name = self.list_frame.tree.set(to_edit_id, "Nom du contact")
        to_edit_profile = self.list_frame.tree.set(to_edit_id, "Profil")
        w = Toplevel()
        initialise_s_window(w)
        secondary_interface = addUser_interface.AddUserInterface(w)
        secondary_interface.champ_label["text"] = "Modifier l'utilisateur"
        secondary_interface.profil_saisi.set(to_edit_profile)
        secondary_interface.ligne_username.insert(0, to_edit_username)
        secondary_interface.ligne_NomContact.insert(0, to_edit_name)
        w.mainloop()
        # Recupere les valeurs du formulaire
        username_value = secondary_interface.username_saisi.get()
        contactname_value = secondary_interface.nomContact_saisi.get()
        password_value = secondary_interface.password_saisi.get()
        profile_value = secondary_interface.profil_saisi.get()
        # Creation de l'objet et edition dans la base
        user_to_edit = Users.User(contactname_value, username_value, password_value, profile_value)
        user_to_edit.edit_user()
        self.champ_information["text"] = "Modifications enregistrées"
        secondary_interface.destroy()
        w.destroy()
        self.quit()

    def deleteclick(self):
        self.choice = "delete_user"
        to_delete_id = self.list_frame.tree.selection()
        to_delete_value = self.list_frame.tree.set(to_delete_id, "Nom d'utilisateur")
        DatabaseScripts.delete_user(to_delete_value)
        self.quit()


def main():
    DatabaseScripts.db_file = r".\POS.db"
    window = Tk()
    window.attributes('-fullscreen', True)
    p_interface = Menu.InterfaceMenu(window)
    p_interface.champ_application["text"] = "Gestion des utilisateurs"
    p_interface.content_frame = UsersInterface()
    p_interface.content_frame.principal_frame = UserList_interface.UserListInterface()
    p_interface.mainloop()


if __name__.endswith('__main__'):
    main()