import telebot
from texts import *
from bestconfig import Config

config = Config("config.yml")
bot = telebot.TeleBot(config.get('bot_token'))

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.from_user.id, start_message)