import sqlite3
import requests
from Database import Data

def get_update(self, database: Data, api_key: String):
    chats = self.get_chats()

    json = requests.post(f'https://api.telegram.org/bot{api_key}/getUpdates').json()
    try:
        new_chats = [x["message"]["chat"]["id"] for x in json["result"] if "unsubscribe" not in x["message"]["text"]]
        remove_chats = [x["message"]["chat"]["id"] for x in json["result"] if "unsubscribe" in x["message"]["text"]]
        new_chats = [x for x in new_chats if str(x) not in chats]
        database.add_chats(new_chats)
        database.remove_chats(remove_chats)
    except Exception as e:
        print(e)