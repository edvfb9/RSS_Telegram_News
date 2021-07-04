import pathlib
import requests
import os
import sqlite3

class Data:
    
    def __init__(self, filename="settings/chats.db"):

        #only checks whether the file exists if default path is used
        self.con = sqlite3.connect(filename)
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Users(userId INT PRIMARY KEY)''')
        self.con.commit()

    def get_chats(self):
        cur = self.con.cursor()
        cur.execute('''SELECT * FROM userId''')
        users = [x[0] for x in cur.fetchall()]
        cur.close()
        return users

    def add_chats(self, chat_ids):
        cur = self.con.cursor()
        for id in chat_ids:
            cur.execute('''INSERT INTO Users(''' + str(id) + ')')
        self.con.commit()

    def remove_chats(self, chat_ids):
        cur = self.con.cursor()
        for id in chat_ids:
            cur.execute('''DELETE FROM Users WHERE userId=''' + str(id))
        self.con.commit()