#! /usr/bin/env python3
# coding: utf-8

import DatabaseScripts


class TicketTypes:
    def __init__(self, reference, name, price, solde):
        self.reference = reference
        self.name = name
        self.price = price
        self.solde = solde
        self.active = 1

    def add_tickettype(self):
        # Verifier la presence de la reference
        _existe = 0
        _verif_existe = DatabaseScripts.check_tickettype(self.reference)
        if _verif_existe != "" and _verif_existe is not None:
            _existe = 1
        # Ajouter dans la bd
        if not _existe:
            DatabaseScripts.insert_tickettype((self.reference, self.name, self.price, self.solde, self.active))
            return 1
        else:
            return 0

    def edit_tickettype(self):
        # Verifier la presence de la reference
        _verif_existe = DatabaseScripts.check_tickettype(self.reference)
        if _verif_existe != "" and _verif_existe is not None:
            DatabaseScripts.edit_tickettype((self.name, self.price, self.solde, self.active, self.reference))
        else:
            DatabaseScripts.insert_tickettype((self.reference, self.name, self.price, self.solde, self.active))