#! /usr/bin/env python3
# coding: utf-8

import hashlib

import DatabaseScripts


class User:
    def __init__(self, name, username, password, profile):
        self.name = name
        self.username = username
        self.password = password
        self.profile = profile
        self.active = 1

    def add_user(self):
        # Verifier la presence du username
        _existe = 0
        _verif_existe = DatabaseScripts.check_user(self.username)
        if _verif_existe != "" and _verif_existe is not None:
            _existe = 1
        # Ajouter dans la bd
        if not _existe:
            # Hash Password
            password_encode = self.password.encode()
            password_encode = hashlib.sha1(password_encode).hexdigest()
            DatabaseScripts.insert_user((self.name, self.username, password_encode, self.profile, self.active))
            return 1
        else:
            return 0

    def edit_user(self):
        password_encode = self.password.encode()
        password_encode = hashlib.sha1(password_encode).hexdigest()
        # Verifier la presence de la reference
        _verif_existe = DatabaseScripts.check_user(self.username)
        if _verif_existe != "" and _verif_existe is not None:
            DatabaseScripts.edit_user((self.name, self.password, self.profile, self.username))
        else:
            DatabaseScripts.insert_user((self.name, self.username, password_encode, self.profile, self.active))
        pass
        #ne rien faire ici


def main():
    DatabaseScripts.db_file = r"..\Stock.db"
    DatabaseScripts.initialise_database()
    user_to_add = User('Administrateur', 'admin', '123')
    user_to_add.add_user()
    user_to_add = User('Mouha BEN YAHIA', 'mouha', '123')
    user_to_add.add_user()

if __name__.endswith('__main__'):
    main()