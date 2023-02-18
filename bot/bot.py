import telebot
import json
import time
from datetime import datetime
import re


#token = open("token.txt", "r")
#bot = telebot.TeleBot(str(token.read()))
#token.close()
token = "6158741407:AAHWQPeAhCJIfI31JNtqPYX6Nlh5VTo7cjU"
bot = telebot.TeleBot(token)

#bot = telebot.TeleBot(str(token.read()))

frequency = 200


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    data = call.data
    cid = str(call.message.chat.id)
    bot.edit_message_reply_markup(cid, call.message.message_id)
    bot.send_message(message.chat.id, data, reply_markup=markup)
    return


@bot.message_handler(commands=['frequency'])
def frequency(message):
    cid = str(message.chat.id)
    markup = telebot.types.InlineKeyboardMarkup()
    path = 1
    frequency_low = {"frequency": 200}
    frequency_med = {"frequency": 100}
    frequency_hi =  {"frequency": 50}
    text_data = """Set mayo frequency:\nLow - every 200 messages\n
    Medium - every 100 messages
    High - every 50 messages"""
    markup.row(telebot.types.InlineKeyboardButton(text="Low", callback_data=frequency_low))
    markup.row(telebot.types.InlineKeyboardButton(text="Medium", callback_data=frequency_med))
    markup.row(telebot.types.InlineKeyboardButton(text="High", callback_data=frequency_hi))
    return bot.send_message(message.chat.id, text_data, reply_markup=markup)
    

@bot.message_handler(commands=['roll'])
def roll(message):
    return


@bot.message_handler(commands=['get_mayo'])
def get_mayo(message):
    return


bot.polling(none_stop=True, interval=0)