import pathlib
import requests
import os
import sqlite3

class chats:
    
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

    def __add_chats(self, chat_ids):
        cur = self.con.cursor()
        for id in chat_ids:
            cur.execute('''INSERT INTO Users(''' + str(id) + ')')
        self.con.commit()

    def get_new_chats(self, api_key):
        chats = self.get_chats()

        json = requests.post(f'https://api.telegram.org/bot{api_key}/getUpdates').json()
        try:
            new_chats = [x["message"]["chat"]["id"] for x in json["result"]]
            new_chats = [x for x in new_chats if str(x) not in chats]
            self.__add_chats(new_chats)
        except Exception:
            pass
        