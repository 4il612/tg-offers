import telebot

def sendMessage(token, chatid, message):
    bot = telebot.TeleBot(token)
    bot.send_message(chatid, message, parse_mode='html')