#! /usr/bin/env python3
# coding: utf-8

from tkinter import *


class InterfaceMenu(Frame):

    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, **kwargs)
        self.pack(fill=BOTH)
        window.minsize(width=1280, height=700)
        self.choice = "0"
        self.contactname = "Connecté en tant que : TEST"
        self.authorized = 0
        img = PhotoImage(file='.\images\logo.png')
        window['bg'] = '#F0F0ED'

        self.top_frame = Frame(window, bg='#424549', height=70)
        self.disconnect_button = Button(self.top_frame, width=12, height=1, bg='#FF6347', bd=0,
                                        highlightbackground='#7289da',
                                        text="Se déconnecter", command=self.disconnect, font=("Helvetica", 10, 'bold'),
                                        fg='white')
        self.disconnect_button.pack(ipadx=3, fill=Y, side=RIGHT)
        self.champ_acceuil = Label(self.top_frame, bg='#424549', text=self.contactname, font=("Helvetica", 10, 'bold'),fg='white')
        self.champ_acceuil.pack(padx=4, pady=10, side=RIGHT)
        self.champ_logo = Label(self.top_frame, image=img, bd=0)
        self.champ_logo.image = img #keep a reference
        self.champ_logo.pack(side=LEFT, fill=Y)
        self.top_frame.pack(side=TOP, fill=X)

        self.side_frame = Frame(window, bg='#EE741D', width=230)
        self.champ_menu = Label(self.side_frame, bg='#EE741D', text="", font=("Helvetica", 12, 'bold'), fg='white')
        self.champ_menu.pack(padx=112, pady=15)

        self.sell_button = Button(self.side_frame, width=12, height=1, bg='#EE741D', bd=0, highlightbackground='#EE741D', text="Point de vente", command=self.sell_click, font=("Helvetica", 14), fg='white')
        self.sell_button.pack(anchor=W, padx=5, pady=5, fill=X)
        self.champ_menu1 = Label(self.side_frame, bg='#EE741D', text="Consultations", font=("Helvetica", 11, 'bold'), fg='#424549')
        self.champ_menu1.pack(anchor=W, padx=10, pady=5)
        self.sellings_button = Button(self.side_frame, width=12, height=1, bg='#EE741D', bd=0,
                                  highlightbackground='#EE741D', text="Ventes", command=self.sellings_click,
                                  font=("Helvetica", 14), fg='white')
        self.sellings_button.pack(padx=10, pady=2, anchor=W, fill=X)
        self.badges_button = Button(self.side_frame, width=12, height=1, bg='#EE741D', bd=0,
                                  highlightbackground='#EE741D', text="Badges", command=self.badges_click,
                                  font=("Helvetica", 14), fg='white')
        self.badges_button.pack(padx=10, pady=2, anchor=W, fill=X)
        self.champ_menu3 = Label(self.side_frame, bg='#EE741D', text="Configurations", font=("Helvetica", 11, 'bold'), fg='#424549')
        self.champ_menu3.pack(anchor=W, padx=10, pady=5)
        self.users_button = Button(self.side_frame, width=12, height=1, bg='#EE741D', bd=0,
                                   highlightbackground='#EE741D', text="Utilisateurs", command=self.users_click,
                                   font=("Helvetica", 14), fg='white')
        self.users_button.pack(padx=10, pady=1, anchor=W, fill=X)
        self.tickets_button = Button(self.side_frame, width=12, height=1, bg='#EE741D', bd=0,
                                    highlightbackground='#EE741D', text="Tickets", command=self.tickets_click,
                                    font=("Helvetica", 14), fg='white')
        self.tickets_button.pack(padx=10, pady=2, anchor=W, fill=X)

        self.side_frame.pack(anchor=W, side=LEFT, expand=False, fill=Y)

        self.principal_frame = Frame(window,)
        self.champ_application = Label(self.principal_frame, text="Menu", font=("Helvetica", 16), fg='#1e2124')
        self.champ_application.pack(anchor=W, padx=5, pady=5)
        self.principal_frame.pack(anchor=N, fill=BOTH, side=TOP, expand=False)

        self.content_frame = Frame(self.principal_frame,)
        self.content_frame.pack(fill=BOTH, side=TOP, expand=True)

    def users_click(self):
        self.choice = "users"
        self.quit()

    def disconnect(self):
        self.choice="back"
        self.quit()

    def sell_click(self):
        self.choice="sell"
        self.quit()

    def sellings_click(self):
        self.choice="sellings"
        self.quit()

    def badges_click(self):
        self.choice="badges"
        self.quit()

    def tickets_click(self):
        self.choice="tickets"
        self.quit()


def main():
    window = Tk()
    p_interface = InterfaceMenu(window)
    img = PhotoImage(file='.\images\logo.png')
    p_interface.mainloop()
    p_interface.destroy()
    window.destroy()


if __name__.endswith('__main__'):
    main()