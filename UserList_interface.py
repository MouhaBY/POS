#! /usr/bin/env python3
# coding: utf-8

from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk

import DatabaseScripts


class UserListInterface(Frame):

    def __init__(self, **kwargs):
        Frame.__init__(self, **kwargs)
        self.pack(fill=BOTH)

        # the data ...
        self.users_header = ['Nom du contact', "Nom d'utilisateur", "Profil"]
        self.users_list = DatabaseScripts.read_users()
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        container = ttk.Frame(self)
        container.pack(padx=30, pady=30, fill='both', expand=True)

        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=self.users_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in self.users_header:
            # Self.tree.heading(col, text=col.title(), command=lambda c=col: sortby(self.tree, c, 0))
            self.tree.heading(col, text=col.title())
            # Adjust the column's width to the header string
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

        for item in self.users_list:
            self.tree.insert('', 'end', values=item)

            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(self.users_header[ix], width=None) < col_w:
                    self.tree.column(self.users_header[ix], width=col_w)