import telebot
from texts import *
from bestconfig import Config
from keyboard import *

config = Config("config.yml")
bot = telebot.TeleBot(config.get('bot_token'))


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, start_message, reply_markup=anket_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'Повар':
        mes = bot.send_message(call.message.chat.id, cook_ms)
        bot.register_next_step_handler(mes, ankets, cook=True)
    if call.data == 'Половник':
        bot.send_message(call.message.chat.id, ladle_ms[0], reply_markup=ladle_keyboard)
    if call.data == 'Ложки':
        bot.send_message(call.message.chat.id, spoons[0], reply_markup=ladle_keyboard)


def ankets(message, cook=None, ladle=None, spoons=None, knives=None, forks=None, dishes=None, cups=None,
           other_services=None, household_devices=None, parcel_from_Moscow=None, posting_on_a_channel=None,
           replica_of_dishes=None, technical_support=None, second_stage=None):
    if cook:
        bot.send_message(message.chat.id, wait_ms)
        bot.send_message(config.get('admin_chatid'),
                         q_layout('Повар', message.text, message.from_user.first_name, message.from_user.id),
                         reply_markup=admin_keyboard)


def q_layout(objec, city, username, user_id):
    anket = f'''
Объект: {objec}
Город: {city}
Юзернейм: {username}
Юзер ID: {user_id}
    '''
    return anket


bot.infinity_polling()
