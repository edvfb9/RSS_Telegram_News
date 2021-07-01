import pathlib
import requests
import os

class chats:
    
    def __init__(self, filename="settings/chats.config"):

        #only checks whether the file exists if default path is used
        if filename=="settings/chats.config":
            try:
                pathlib.Path("settings").mkdir()
                file = open(filename, 'w+')
                file.close()
            except Exception:
                pass
        self.filename = filename

    def get_chats(self):
        config = open(self.filename, 'r')
        return config.readlines()

    def __add_chats(self, chat_ids):
        config = open(self.filename, 'a')
        config.writelines(chat_ids)

    def get_new_chats(self, api_key):
        chats = self.get_chats()

        json = requests.post(f'https://api.telegram.org/bot{api_key}/getUpdates').json()
        try:
            new_chats = [x["message"]["chat"]["id"] for x in json["result"]]
            new_chats = [x for x in new_chats if str(x) not in chats]
            self.__add_chats(new_chats)
        except Exception:
            pass
        