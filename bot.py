import telegram
from telegram import *
from telegram.ext import *
import S5Crypto
import socket
import os

def start_handler(update, context):
    username = update.effective_user.username
    if username == os.environ.get('administrador') :
        update.message.reply_text(text=f"Hola {username} Bienvenido a tu Bot para Buscar PROXY.\n\nUtiliza /search_proxy para buscar en las configuraciones predeterminadas\n/search_proxy (rango_min-rango_max) (ip) para buscar en tu especificaciones")
    else :
        update.message.reply_text(text="@"+username+" no tienes acceso al bot")

def filtrar_text(update, context):
    text = update.message.text
    username = update.effective_user.username
    if username == os.environ.get('administrador') :
        if '/search_proxy' in text:
            try:
                try:
                    rango_min = str(str(text).split('-')[0]).split(' ')[1]
                    rango_max = str(str(text).split('-')[1]).split(' ')[0]
                    ip = str(text).split(' ')[2]
                    msg_start = '🛰 Buscando Proxy en el Rango de Puerto : '+rango_min+' - '+rango_max+'\nIP : '+ip+'!!\n\n⏳ Por favor espere .....'
                    context.bot.sendMessage(chat_id=update.message.chat.id,text=f"{msg_start}")
                    print("Buscando proxy...")
                    for port in range(int(rango_min),int(rango_max)):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex((ip,port))

                        if result == 0:
                            print ("Puerto abierto!")
                            print (f"Puerto: {port}")
                            proxy = f'{ip}:{port}'
                            proxy_new = S5Crypto.encrypt(f'{proxy}')
                            msg = 'Su nuevo proxy es:\n\nsocks5://' + proxy_new
                            context.bot.sendMessage(chat_id=update.message.chat.id,text=f"{msg}")
                            break
                        else:
                            print ("Error...Buscando...")
                            print (f"Buscando en el puerto: {port}")
                            sock.close()
                    return
                except:
                    msg_start = '🛰 Buscando Proxy!!\n\n⏳ Por favor espere .....'
                    context.bot.sendMessage(chat_id=update.message.chat.id,text=f"{msg_start}")
                    print("Buscando proxy...")
                    for port in range(2080,2085):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex(('181.225.253.188',port))

                        if result == 0:
                            print ("Puerto abierto!")
                            print (f"Puerto: {port}")
                            proxy = f'181.225.253.188:{port}'
                            proxy_new = S5Crypto.encrypt(f'{proxy}')
                            msg = 'Su nuevo proxy es:\n\nsocks5://' + proxy_new
                            context.bot.sendMessage(chat_id=update.message.chat.id,text=f"{msg}")
                            break
                        else:
                            print ("Error...Buscando...")
                            print (f"Buscando en el puerto: {port}")
                            sock.close()
                    return
            except: context.bot.sendMessage(update.message.chat.id,"ERROR")
    else :
        update.message.reply_text(text="@"+username+" no tienes acceso al bot")

# TOKEN
if __name__ == '__main__':
    bot_token = os.environ.get('bot_token')
    bot = telegram.Bot(token=bot_token)
    updater = Updater(token=bot_token, use_context=True)

# Despachadores
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(MessageHandler(filters=Filters.text, callback=filtrar_text))

# Para Ejecutar el Bot
    updater.start_polling()
    print("Ejecutando el bot @" + bot.username)
    updater.idle()
