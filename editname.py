from telethon.sync import TelegramClient
from telethon import functions
from time import strftime, sleep

api_id = 1212804
api_hash = 'd683339603c2dd78185820dc411ba0c5'
name = 'Amirshox'

while True:
    with TelegramClient(name, api_id, api_hash) as client:
        current_time = strftime("%H:%M")
        result = client(functions.account.UpdateProfileRequest(
            first_name='Amirshox',
            last_name='Muxitdinov | ' + current_time,
        ))

    sleep(20)
