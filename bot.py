import telegram
from telegram import *
from telegram.ext import *
import S5Crypto
import socket
import time
import os

permitidos = ["AresDza"]

def start_handler(update, context):
    username = update.effective_user.username
    if username == administrador and administrador in permitidos:
        update.message.reply_text(text=f"Bienvenido al BOT PR_Finder V1 🛰\n\n👤 USUARIO : @{username}\n\n/search_proxy - para buscar en las configuraciones predeterminadas\n/search_proxy (rango_min-rango_max) (ip) - para buscar en tu especificaciones")
    elif username in permitidos and administrador in permitidos:
        update.message.reply_text(text=f"Bienvenido al BOT PR_Finder V1 🛰\n\n👤 USUARIO : @{username}\n\n/search_proxy - para buscar en las configuraciones predeterminadas\n/search_proxy (rango_min-rango_max) (ip) - para buscar en tu especificaciones")
    else:
        update.message.reply_text(text="@"+username+" no tienes acceso al bot")

def filtrar_text(update, context):
    text = update.message.text
    username = update.effective_user.username
    if username == administrador :
        if '/search_proxy' in text:
            try:
                try:
                    try:id_msg = int(update.message.message_id) + 1
                    except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                    rango_min = str(str(text).split('-')[0]).split(' ')[1]
                    rango_max = str(str(text).split('-')[1]).split(' ')[0]
                    ip = str(text).split(' ')[2]
                    msg_start = '🛰 Buscando Proxy en el Rango de Puerto : '+rango_min+' - '+rango_max+'\nIP : '+ip+'!!\n\n⏳ Por favor espere .....'
                    print("Buscando proxy...")
                    bot.sendMessage(update.message.chat.id,msg_start)
                    time.sleep(1.5)
                    try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nBuscando proxy...\n\n➖➖➖➖➖➖➖")
                    except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                    for port in range(int(rango_min),int(rango_max)):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex((ip,port))

                        if result == 0:
                            print ("Puerto abierto!")
                            print (f"Puerto: {port}")
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nPuerto abierto!\nPuerto: {port}\n➖➖➖➖➖➖➖")
                            except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                            proxy = f'{ip}:{port}'
                            proxy_new = S5Crypto.encrypt(f'{proxy}')
                            time.sleep(5)
                            msg = 'Su nuevo proxy es:\n\nsocks5://' + proxy_new
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg}")
                            except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                            break
                        else:
                            print ("Error...Buscando...")
                            print (f"Buscando en el puerto: {port}")
                            sock.close()
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nError...Buscando...\nBuscando en el Puerto: {port}\n➖➖➖➖➖➖➖")
                            except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                    try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"🛰 No Hubo Éxito Buscando Proxy!!\n\n❌ IP : {ip}\n\n❌ PUERTOS : {rango_min}-{rango_max}")
                    except Exception as ex:print(str(ex))
                    return
                except:
                    range_min = "2080"
                    range_max = "2085"
                    ip_default = "181.225.253.188"
                    try:id_msg = int(update.message.message_id) + 1
                    except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                    msg_start = '🛰 Buscando Proxy!!\n\n⏳ Por favor espere .....'
                    print("Buscando proxy...")
                    bot.sendMessage(update.message.chat.id,msg_start)
                    time.sleep(1.5)
                    try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nBuscando proxy...\n\n➖➖➖➖➖➖➖")
                    except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                    for port in range(2080,2085):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex(('181.225.253.188',port))

                        if result == 0:
                            print ("Puerto abierto!")
                            print (f"Puerto: {port}")
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nPuerto abierto!\nPuerto: {port}\n➖➖➖➖➖➖➖")
                            except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                            proxy = f'{ip}:{port}'
                            proxy_new = S5Crypto.encrypt(f'{proxy}')
                            time.sleep(5)
                            msg = 'Su nuevo proxy es:\n\nsocks5://' + proxy_new
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg}")
                            except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                            break
                        else:
                            print ("Error...Buscando...")
                            print (f"Buscando en el puerto: {port}")
                            sock.close()
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nError...Buscando...\nBuscando en el Puerto: {port}\n➖➖➖➖➖➖➖")
                            except Exception as ex:print(str(ex))
                    try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"🛰 No Hubo Éxito Buscando Proxy!!\n\n❌ IP : {ip_default}\n\n❌ PUERTOS : {range_min}-{range_max}")
                    except Exception as ex:print(str(ex))
                    return
            except: bot.sendMessage(update.message.chat.id,"ERROR")
    else :
        update.message.reply_text(text="@"+username+" no tienes acceso al bot")

# TOKEN
if __name__ == '__main__':
    administrador = os.environ.get('administrador')
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
