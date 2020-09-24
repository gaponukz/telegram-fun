from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from emoji import emojize
import random, asyncio

app = Client(
    'my_account',
    api_id = '1144880',
    api_hash = 'd9844b8cc08b988e9e09680b10ad0b44'
)

client = TelegramClient(
    'zhenyagaponuk', 
    '1144880',
    'd9844b8cc08b988e9e09680b10ad0b44'
)
client.start()

DELETE = False
ANIMATIONS = False
INVITE = False

@app.on_message(filters.command("hack", prefixes = "/") & filters.me)
async def hack_ass_command(_, message) -> None:
    process = 0
 
    while(process < 100):
        try:
            text = f"👮‍ Взлом жопы в процессе ...{process}%"
            await message.edit(text)
 
            process += random.randint(1, 3)
            await asyncio.sleep(0.1)
 
        except FloodWait as error:
            await asyncio.sleep(error.x)
 
    await message.edit("🟢 Жопа успешно взломана!")

@app.on_message(filters.command('spam', prefixes = '/') & filters.me)
async def spam_message(_, message) -> None:
    this_message = message.text.split()
    spam_text = ' '.join(this_message[2:])
    time_to_spam = this_message[1] # spammed messages
    await message.delete()
    for _ in range(int(time_to_spam)):
        await message.reply_text(spam_text)
        await asyncio.sleep(0.05)

@app.on_message(filters.command('put', prefixes = '/') & filters.me)
async def put_text_with_animations(_, message):
    this_message = message.text.split('/put')[1]

    edit_message = ''
    for symbol in this_message:
        edit_message += symbol
        try:
            await message.edit(edit_message)
            await asyncio.sleep(0.05)
        except Exception as error:
            pass

@app.on_message(filters.command("pidor", prefixes="/") & filters.me)
async def thanos(_, message):
    chat = message.text.split("/pidor ", maxsplit = 1)[1]
 
    chats = await client.get_dialogs()
    dialog = [cht for cht in chats if chat in cht.name][0]
    members = await client.get_participants(dialog.id)
    process = 0
    eyes = emojize(":eyes:", use_aliases=True)
    exclamation = emojize(":exclamation:", use_aliases=True)
 
    while(process < 100):
        try:
            text = f"{eyes} Поиск пидора ... {process}%"
            await message.edit(text)
 
            process += random.randint(1, 3)
            await asyncio.sleep(0.1)
 
        except FloodWait as error:
            await asyncio.sleep(error.x)
    
    pidor_id = random.choice(members).id

    pidor = (await client.get_entity(PeerUser(pidor_id))).username \
        if (await client.get_entity(PeerUser(pidor_id))).username \
        else (await client.get_entity(PeerUser(pidor_id))).first_name + " " \
        + (await client.get_entity(PeerUser(pidor_id))).last_name \
            if (await client.get_entity(PeerUser(pidor_id))).last_name else ''

    if pidor:
        await message.edit(f"Пидор найден {exclamation} @{pidor}")
    else:
        await message.edit(f"Пидор не найден {exclamation}")

@app.on_message(filters.command('animation', prefixes = '/') & filters.me)
async def animation_settings(_, message) -> None:
    mode = message.text.split('/animation ', maxsplit = 1)[1]
    await message.delete()
    global ANIMATIONS
    if not mode.lower() == 'on':
        ANIMATIONS = False
    elif not mode.lower() == 'off':
        ANIMATIONS = True

@app.on_message(filters.command('delete', prefixes = '/') & filters.me)
async def delete_settings(_, message) -> None:
    mode = message.text.split('/delete ', maxsplit = 1)[1]
    await message.delete()
    global DELETE
    if not mode.lower() == 'on':
        DELETE = False
    elif not mode.lower() == 'off':
        DELETE = True

@app.on_message(filters.command('invite', prefixes = '/') & filters.me)
async def invite_settings(_, message) -> None:
    mode = message.text.split('/invite ', maxsplit = 1)[1]
    await message.delete()
    global INVITE
    if not mode.lower() == 'on':
        INVITE = False
    elif not mode.lower() == 'off':
        INVITE = True

@app.on_message()
async def all_messages_script(_, message) -> None:
    global DELETE
    global ANIMATIONS
    global INVITE

    if INVITE:
        if (user_id := message.from_user.id) != '1052311571':
            chats = await client.get_dialogs()
            dialog = [cht for cht in chats if 'Telegram Fun' in cht.name][0]
            await client(InviteToChannelRequest(dialog, [user_id]))
    
    if DELETE:
        if not str(message.from_user.id) in ['669547942', '1052311571']:
            await message.delete()
    if ANIMATIONS:
        edit_message = ''
        for symbol in message.text:
            edit_message += symbol
            try:
                await message.edit(edit_message)
                await asyncio.sleep(0.05)
            except Exception as error:
                pass

if __name__ == "__main__":
    app.run()