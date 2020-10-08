#! /usr/bin/env python3
# coding: utf-8

"""creation du fichier de la base des donnees et des donnees de demarrage"""

import sqlite3
from sqlite3 import Error

global db_file


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def execute_query(query):
    try:
        conn = sqlite3.connect(db_file)
        with conn:
            _result = conn.execute(query)
            conn.commit()
            return _result
        conn.close()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' has occurred")


def execute_query_data(query,data):
    try:
        conn = sqlite3.connect(db_file)
        with conn:
            _result = conn.execute(query, data)
            conn.commit()
            return _result
        conn.close()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' has occurred")


def create_table_users():
    sql = """ CREATE TABLE USERS (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            username TEXT UNIQUE,
            password TEXT,
            profile TEXT,
            active BOOLEAN
            );
        """
    execute_query(sql)


def insert_user(data):
    sql = 'INSERT INTO USERS (name, username, password, profile, active) values(?, ?, ?, ?, ?)'
    execute_query_data(sql, data)


def check_user(username_req):
    sql = "SELECT name, username, password FROM USERS WHERE username == (?)"
    _result = execute_query_data(sql, (username_req,))
    try:
        return _result.fetchone()[2]
    except TypeError:
        return None


def get_user(username_req):
    sql = "SELECT username, password, name FROM USERS WHERE username == (?)"
    _result = execute_query_data(sql, (username_req,))
    try:
        return _result.fetchone()[2]
    except TypeError:
        return None


def read_users():
    sql = "SELECT name, username, profile FROM USERS"
    _result = execute_query(sql)
    return _result


def delete_user(username_req):
    sql = """ DELETE FROM USERS WHERE username == (?) """
    execute_query_data(sql, (username_req,))


def edit_user(data):
    sql = """ UPDATE USERS SET name = (?), password = (?), profile = (?) WHERE username == (?) """
    execute_query_data(sql, data)


def create_table_tickettypes():
    sql = """ CREATE TABLE TICKETTYPES (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            reference TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            price FLOAT,
            solde INTEGER,
            active BOOLEAN
            );
        """
    execute_query(sql)


def insert_tickettype(data):
    sql = 'INSERT INTO TICKETTYPES (reference, name, price, solde, active) values(?, ?, ?, ?, ?)'
    execute_query_data(sql, data)


def check_tickettype(reference_req):
    sql = "SELECT reference, name, price FROM TICKETTYPES WHERE reference == (?)"
    _result = execute_query_data(sql, (reference_req,))
    try:
        return _result.fetchone()[2]
    except TypeError:
        return None


def read_tickettypes():
    sql = "SELECT reference, name, price, solde FROM TICKETTYPES"
    _result = execute_query(sql)
    return _result


def delete_tickettype(reference):
    sql = """ DELETE FROM TICKETTYPES WHERE reference == (?) """
    execute_query_data(sql, (reference,))

def edit_tickettype(data):
    sql = """ UPDATE TICKETTYPES SET name = (?), price = (?), solde = (?), active = (?) WHERE reference == (?) """
    execute_query_data(sql, data)

def initialise_database():
    create_connection()
    try:
        create_table_users()
        insert_user(('Administrateur', 'admin', '40bd001563085fc35165329ea1ff5c5ecbdbbeef', 'sysadmin', 'True'))
    except sqlite3.OperationalError:
        pass
    try:
        create_table_tickettypes()
    except sqlite3.OperationalError:
        pass


def main():
    initialise_database()
    insert_tickettype(('1', '1', '1', '1', 'True'))


if __name__.endswith('__main__'):
    main()