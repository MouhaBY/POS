#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
from tkinter import messagebox
import Connexion
import Menu
import DatabaseScripts
import Users_interface
import UserList_interface
import TicketTypes_interface
import TicketList_interface
import POS_interface

def initialise_window(window):
    window.minsize(width=1280, height=700)
    window.title("POINT OF SALE by MBY")
    window.wm_iconbitmap('.\images\ico.ico')
    window['bg'] = '#1e2124'
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.attributes('-fullscreen', True)


# Quitter l'application
def on_closing():
    if messagebox.askokcancel("Quit", "Arrêter l'application ? "):
            window.destroy()
    else:
        return 1


def show_user(window):
    _username_connected = window.username.get()
    _contact_name_connected = DatabaseScripts.get_user(_username_connected)
    _contact_connected = "Utilisateur connecté : " + _contact_name_connected
    return _contact_connected


def main():
    # Create Database
    DatabaseScripts.db_file = r".\POS.db"
    DatabaseScripts.initialise_database()

    # construction de la fenetre
    global window
    window = tk.Tk()
    initialise_window(window)

    # Construction de la premiere page d'Acceuil
    p_interface = Connexion.InterfaceConnexion(window)

    # Application lancée et toujours fonctionnelle jusqu'a arret
    running=1
    while running:
        p_interface.mainloop()

        # Quitter l'application
        if p_interface.choice == "stop":
            running = on_closing()

        # Acces menu
        if p_interface.authorized ==1:
            user_connected_shown = show_user(p_interface)
            p_interface.destroy()
            window.destroy()
            s_window=tk.Tk()
            initialise_window(s_window)
            p_interface=Menu.InterfaceMenu(s_window)
            p_interface.champ_acceuil["text"] = user_connected_shown
            p_interface.mainloop()
            while p_interface.choice != "back":
                if p_interface.choice == "users":
                    p_interface.champ_application["text"]="Gestion des utilisateurs"
                    p_interface.content_frame.destroy()
                    p_interface.content_frame = Users_interface.UsersInterface()
                    p_interface.content_frame.list_frame = UserList_interface.UserListInterface()
                    p_interface.mainloop()
                    p_interface.content_frame.list_frame.destroy()
                if p_interface.choice == "sell":
                    p_interface.champ_application["text"] = "Point de vente"
                    p_interface.content_frame.destroy()
                    p_interface.content_frame = POS_interface.PosInterface()
                    p_interface.mainloop()
                    p_interface.content_frame.list_frame.destroy()
                if p_interface.choice == "sellings":
                    p_interface.champ_application["text"] = "Historique de ventes"
                    p_interface.content_frame.destroy()
                    p_interface.mainloop()
                if p_interface.choice == "badges":
                    p_interface.champ_application["text"] = "Liste des badges"
                    p_interface.content_frame.destroy()
                    p_interface.mainloop()
                if p_interface.choice == "tickets":
                    p_interface.champ_application["text"] = "Gestion des tickets"
                    p_interface.content_frame.destroy()
                    p_interface.content_frame = TicketTypes_interface.TicketTypesInterface()
                    p_interface.content_frame.list_frame = TicketList_interface.TicketListInterface()
                    p_interface.mainloop()
                    p_interface.content_frame.list_frame.destroy()
            p_interface.destroy()
            s_window.destroy()
            window=tk.Tk()
            initialise_window(window)
            p_interface = Connexion.InterfaceConnexion(window)


if __name__.endswith('__main__'):
    main()
