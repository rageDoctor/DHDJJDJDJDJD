import asyncio
from os import system, name, path
import os
from time import sleep
from random import choice
from base64 import b64decode
from kvsqlite.sync import Client
try:
    import aiohttp
except:
    system('pip install aiohttp')
    import aiohttp
try:
    from telebot import TeleBot
    from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
except:
    system('pip install telebot')
    from telebot import TeleBot
    from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
try:
    from telethon import TelegramClient, errors, functions
    from telethon.tl.functions.account import CheckUsernameRequest
    from telethon.sessions import StringSession
except:
    system('pip install telethon')
    from telethon import TelegramClient, errors, functions
    from telethon.tl.functions.account import CheckUsernameRequest
    from telethon.sessions import StringSession
try:
    from bs4 import BeautifulSoup as S
except:
    system('pip install beautifulsoup')
    from bs4 import BeautifulSoup as S
try:
    from fake_useragent import UserAgent
except:
    system('pip install fake_useragent')
    from fake_useragent import UserAgent
try:
    from datetime import datetime
except:
    system('pip install datetime')
    from datetime import datetime

token = os.environ.get('token')
chat_id = os.environ.get('id')

bot = TeleBot(token=token)
session = os.environ.get('session')

db = Client(f"users.bot")
db.set("session",session)
async def fragment(username):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f'https://fragment.com/username/{username}', headers={'Cookie': 'stel_ssid=105b9e3f8fc71d3078_18338999148668777485;','Pragma': 'no-cache','Sec-Ch-Ua': '"Not-A.Brand";v="99", "Chromium";v="124"','Sec-Ch-Ua-Mobile': '?1','Sec-Ch-Ua-Platform': '"Android"','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': str(UserAgent())}) as response:
                text = await response.text()
                soup = S(text, 'html.parser')
                ok = soup.find("meta", property="og:description").get("content")
                if "An auction to get the Telegram" in ok or "Telegram and secure your ownership" in ok or "Check the current availability of" in ok or "Secure your name with blockchain in an ecosystem of 700+ million users" in ok:return True
                elif "is taken" in ok:return "is taken"
                else:return False
        except:return 
from user_agent import generate_user_agent
# async def tele(username):
#     url = "https://t.me/"+str(username)
#     headers = {
#         "User-Agent": generate_user_agent(),
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

#     async with aiohttp.ClientSession() as session:
#         try:
#             async with session.get(url, headers=headers) as response:
#                 text = await response.text()
#                 soup = S(text, 'html.parser')
#                 ok = soup.find("meta", property="og:description").get("content")
#                 if 'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"' in ok:return True
#                 elif '<div class="tgme_page_title">' in ok:return "is taken"
#                 else:return False
#         except:return 
async def channels2(client, username):
    di = await client.get_dialogs()
    for chat in di:
        if chat.name == f'[ {username} ]' and not chat.entity.username:
            client(functions.channels.DeleteChannelRequest(channel=chat.entity))
            print('- Flood : '+username+' .')
            return False
    return True

async def checks(username, client):
    return await client(CheckUsernameRequest(username))

async def claimer(client,username):
    result = await client(functions.channels.CreateChannelRequest(title=f'{username}',about=f"",megagroup=False))
    try:
        await client(functions.channels.UpdateUsernameRequest(channel=result.chats[0],username=username))
        await client.send_message(username,f'New UserName @{username}')
        bot.send_message(chat_id,f'⌯ Done Save UserName .\n⌯ UserName : @{username} .\n⌯ Date : {datetime.now().strftime("%H:%M:%S")} .')
        return True
    except Exception as e: bot.send_message(chat_id,f'⌯ Error Message .\nMessage : {e} .\nUserName : @'+str(username));return False

async def checker(username, client,type):
    try:
        check = await checks(username, client)
        if check:
            print('- Available : '+username+' .')
            claim = await claimer(client,username)
            if claim and fragment(username) == "is taken":claim = True
            else:claim = False
            flood = await channels2(client,username)
            if not flood:
                with open('flood.txt', 'a') as floodX:
                    floodX.write(username + "\n")
                if claim:
                    if type == "c" or type == "fl":
                        return
                if "flood" in type:
                    bot.send_message(chat_id=chat_id, text="Hi New Flood Username\n" + str(username))
        else:
            print('- Taken : ' + username + ' .')
    except errors.rpcbaseerrors.BadRequestError:
        print('- Banned : ' + username + ' .')
        with open("banned4.txt", "a") as banned:
            banned.write(username + '\n')
    except errors.FloodWaitError as timer:
        print('- Flood Account [ ' + str(timer.seconds) + ' Seconds ] .')
    except errors.UsernameInvalidError:
        print('- Error : ' + username + ' .')

def usernameG():
    k = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
    n = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    c = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    z = ''.join(choice('1234567890') for i in range(1))
    g = ''.join(choice('1234567890') for i in range(1))
    kk = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
    nn = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    cc = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    v = ''.join(choice('_') for i in range(1))
    ee = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
    bot = ''.join("bot")
    try:type = db.get("type")
    except: return False
    if type == "se7":
        u1 = k + n + k + n + k + n
        u2 = k + k + n + n + k + n
        u3 = k + n + k + n + k + n 
        u4 = k + n + n + n + k + k
        u5 = k + k + k + n + n + n
        u6 = k + n + k + n + n + k
        u7 = k + n + k + n + k + k
        u8 = k + n + n + k + k + k
        u9 = k + n + k + k + n + k
        u10 = k + n + k + k + k + n
        u11 = k + k + n + n + k + k
        u12 = k + k + n + k + n + k
        u13 = k + k + n + k + k + n
        u14 = k + k + k + n + n + k 
        u15 = k + k + k + n + k + n
        s = u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u15
        return choice(s)
    elif type == "th3":
         u1 = k + v + n + n + n
         u2 = k + n + v + n + n
         u3 = k + n + n + v + n
         u4 = k + k + v + k + n
         u5 = k + v + k + k + n
         u5 = k + k + k + v + n
         u6 = k + n + v + k + k
         u7 = k + n + k + v + k
         u8 = k + k + n + v + k
         u9 = k + v + n + k + k
         u10 = k + k + v + n + k
         u11 = k + v + k + n + k
         s = u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11
        return choice(s)
    elif type == "f5":
        u1 = k + n + c + bot
        u2 = k + n + c + bot
        u3 = k + n + c + bot
        u4 = k + n + n + n + bot
        u5 = k + n + k + k + bot
        u6 = k + k + n + k + bot
        u7 = k + k + k + n + bot
        s = u1, u2, u3, u4, u5, u6, u7
        return choice(s)
    elif type == "f5i":
        u1 = kk + cc + ee + ee + ee
        u2 = kk + cc + cc + cc + nn
        u3 = kk + kk + kk + nn + cc
        s = u1, u2, u3
        return choice(s)
    elif type == "fi5":
        u1 = k + n + z + z + z + z + z
        u2 = k + n + z + z + z + z
        s = u1, u2
        return choice(s)

async def start(client, username,type):
    try:
        ok = await fragment(username)
    except:
        return
    try:
        if not ok:
            if type == "f": type = "flood"
            elif type == "c": type = "claim"
            elif type == "fl": type = "floods"
            await checker(username, client,type)
        elif ok == "is taken":
            print('- Taken : ' + username + ' .')
        else:
            print('- Fragment.com : ' + username + ' .')
            open("fragment.txt", "a").write(username + '\n')
    except Exception as e:
        print(e)

async def clientX():
    global session
    try:
        client = TelegramClient(StringSession(session),b64decode("MjUzMjQ1ODE=").decode(), b64decode("MDhmZWVlNWVlYjZmYzBmMzFkNWYyZDIzYmIyYzMxZDA=").decode())
        await client.start()
    except:pass
    system('cls' if name == 'nt' else 'clear')
    return client

flag = False
async def work(message):
    global flag
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    de = bot.edit_message_text(chat_id=chat_id, message_id=message.message_id,text="تم بدأ فحص اليوزرات لجلب الخاصية لك\n\nاذا كنت تريد توقف الفحص اضغط ادناه", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    while not flag:
        if flag:
            break
        username = usernameG()
        if not username:
            de = bot.edit_message_text(chat_id=chat_id, message_id=de.message_id,text="الرجاء اختر نوع من الاشكال لكي افحص",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="اختيار", callback_data="type")]]))
            return 
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('- Banned : ' + username + ' .')
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('- Fragment.com : ' + username + ' .')
            continue
        type = "f"
        await asyncio.sleep(0.1)
        await start(session, username,type)

async def us5(message,username):
    global flag
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    de = bot.send_message(chat_id=chat_id,text="تم بدأ فحص اليوزر و صيدة\n\nاذا كنت تريد توقف الفحص اضغط ادناه", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    while not flag:
        if flag:
            break
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('- Banned : ' + username + ' .')
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('- Fragment.com : ' + username + ' .')
            continue
        type = "c"
        await asyncio.sleep(0.1)
        await start(session, username,type)


async def us3(message,username):
    global flag
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    de = bot.send_message(chat_id=chat_id,text="تم بدأ فحص اليوزر لجلب اذا كان خاصية\n\nاذا كنت تريد توقف الفحص اضغط ادناه", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    while not flag:
        if flag:
            break
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('- Banned : ' + username + ' .')
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('- Fragment.com : ' + username + ' .')
            continue
        type = "fl"
        await asyncio.sleep(0.1)
        await start(session, username,type)

async def checkCombo(message):
    global flag
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    try:de = bot.edit_message_text(chat_id=chat_id, message_id=message.message_id,text="تم بدأ فحص اليوزرات لجلب الخاصية لك\n\nاذا كنت تريد توقف الفحص اضغط ادناه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    except:de = bot.send_message(chat_id=chat_id,text="تم بدأ فحص اليوزرات لجلب الخاصية لك\n\nاذا كنت تريد توقف الفحص اضغط ادناه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    with open(message.document.file_name, 'r') as file:
        usernames = file.readlines()
    for username in usernames:
        if '@' in username:
            username = username.split('@')[1]
        if flag:
            break
        username = username.strip()
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('- Banned : ' + username + ' .')
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('- Fragment.com : ' + username + ' .')
            continue
        type = "f"
        await asyncio.sleep(0.1)
        await start(session, username,type)
    bot.delete_message(chat_id=chat_id, message_id=de.message_id)
    bot.send_message(chat_id=chat_id,text="انتهى الفحص",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))

@bot.callback_query_handler(func=lambda call: True)
def callB(call):
    global flag
    if call.data == "type":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="اختر النوع من احدى الازرار", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="رباعي", callback_data="th3"), InlineKeyboardButton(text="ab6666", callback_data="fi5")], [InlineKeyboardButton(text="بوتات", callback_data="f5"), InlineKeyboardButton(text="سداسي حرفين", callback_data="se7")],[InlineKeyboardButton(text="خماسي حرفين عشوائي", callback_data="f5i")]]))
    elif call.data in ["th3", "fi5", "f5", "se7","f5i"]:
        db.set("type", call.data)
        de = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"تم اختيار النوع الذي اخترته")
        sleep(2)
        bot.delete_message(chat_id=chat_id, message_id=de.message_id)
        reset(msg=call.message)
    elif call.data == "start":
        flag = False
        asyncio.run(work(message=call.message))
    elif call.data == "stop":
        flag = True
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        reset(msg=call.message)
    elif call.data == "stopp":
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        reset(msg=call.message)
    elif call.data == "us1":
        flag = False
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="اختر من احدى الازرار ادناه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="تثبيت لجلب خاصية", callback_data="po"),InlineKeyboardButton(text="تثبيت خاصية", callback_data="pi")]]))
    elif call.data == "pi":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان اليوزر للتثبيت عليه و صيدة\nارسل بهذا الشكل :\n.تثبيت xxMxx",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
    elif call.data == "po":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان اليوزر للتثبيت عليه حتى يصبح خاصية\nارسل بهذا الشكل : \n.جلب xxMxx",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
    elif call.data == "combo":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان الملف المراد فحصه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))

@bot.message_handler(content_types=["document"])
def fromCombo(message):
    file = bot.download_file(bot.get_file(message.document.file_id).file_path)
    open(file=message.document.file_name, mode="wb").write(file)
    asyncio.run(checkCombo(message=message))

def reset(msg):
    bot.send_message(chat_id, text="@F_9_5", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="فحص عشوائي", callback_data="start")],[InlineKeyboardButton(text="من ملف", callback_data="combo"),InlineKeyboardButton(text="تثبيت", callback_data="us1")],[InlineKeyboardButton(text="اختيار نوع", callback_data="type"),]]))

@bot.message_handler(func=lambda msg: True)
def startB(msg):
    if msg.chat.id != int(chat_id): return
    elif msg.text == "/start":
        bot.send_message(chat_id, text="اهلا بك عزيزي\nبوت متخصص لجلب خاصيات\n– – – – –\nمطوره : @F_9_5", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="فحص عشوائي", callback_data="start")],[InlineKeyboardButton(text="من ملف", callback_data="combo"),InlineKeyboardButton(text="تثبيت", callback_data="us1")],[InlineKeyboardButton(text="اختيار نوع", callback_data="type"),]]))
    elif ".فحص" in msg.text:
        bot.send_message(chat_id=chat_id,text="الفحص شغال طاب يومك")
    elif '.تثبيت ' in msg.text:
        username = msg.text.split('.تثبيت ')[1]
        if '@' in username:username = username.split('@')[1]
        asyncio.run(us5(message=msg,username=username))
    elif ".جلب " in msg.text:
        username = msg.text.split('.جلب ')[1]
        if '@' in username:username = username.split('@')[1]
        asyncio.run(us3(message=msg,username=username))

def polling(bot, interval=5):
    import time ; from requests import exceptions
    while True:
        try:
            bot.polling()
            print('- New Session Bot .')
        except exceptions.ConnectionError:
            print('- New Session Bot .')
            time.sleep(interval)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(interval)
polling(bot=bot)