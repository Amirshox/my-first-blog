from telethon.sync import TelegramClient
from telethon import functions
from time import strftime, sleep

api_id = *
api_hash = '*'
name = 'Amirshox'

while True:
    with TelegramClient(name, api_id, api_hash) as client:
        current_time = strftime("%H:%M")
        result = client(functions.account.UpdateProfileRequest(
            first_name='Amirshox',
            last_name='Muxitdinov | ' + current_time,
        ))

    sleep(20)
