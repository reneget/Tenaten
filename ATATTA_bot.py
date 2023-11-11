import telebot
from texts import *
from bestconfig import Config
from keyboard import *

config = Config("config.yml")
bot = telebot.TeleBot(config.get('bot_token'))


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, start_message, reply_markup=user_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'Повар':
        mes = bot.send_message(call.message.chat.id, cook_ms)
        bot.register_next_step_handler(mes, ankets_creator, cook=True)
    if call.data == 'Принять':
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id, reply_markup=y_keyboard)
    if call.data == 'Отменить':
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id, reply_markup=n_keyboard)
    if call.data == 'Половник':
        bot.send_message(call.message.chat.id, ladle_ms[0], reply_markup=ladle_keyboard)
    if call.data == 'Металическая ручка' or call.data == 'Деревяная ручка':
        mes = bot.send_message(call.message.chat.id, ladle_ms[1])
        bot.register_next_step_handler(mes, ankets_creator, ladle=True, ladle_material=call.data)
    if call.data == 'Ложки':
        mes = bot.send_message(call.message.chat.id, spoons_ms[0])
        bot.register_next_step_handler(mes, ankets_creator, spoons=True)
    if call.data == 'Вилки':
        mes = bot.send_message(call.message.chat.id, forks_ms)
        bot.register_next_step_handler(mes, ankets_creator, forks=True)
    if call.data == 'Ножи':
        mes = bot.send_message(call.message.chat.id, knives_ms[1])
        bot.register_next_step_handler(mes, ankets_creator, knives=True)
    if call.data == 'Тарелки':
        mes = bot.send_message(call.message.chat.id, dishes_ms)
        bot.register_next_step_handler(mes, ankets_creator, dishes=True)
    if call.data == 'Тех. поддержка':
        mes = bot.send_message(call.message.chat.id, technical_support_ms)
        bot.register_next_step_handler(mes, ankets_creator, technical_support=True)
def ankets_creator(message, cook=None, ladle=None, spoons=None, knives=None, forks=None, dishes=None, cups=None, other_services=None, household_devices=None, parcel_from_Moscow=None, posting_on_a_channel=None, replica_of_dishes=None, technical_support=None, ladle_material=None, spoons_city=None, spoons_work=None, knives_city=None):
    if cook:
        bot.send_message(message.chat.id, wait_ms)
        bot.send_message(config.get('admin_group_chat_id'), anket('Повар', message.from_user.first_name, message.from_user.id, city=message.text), reply_markup=admin_keyboard)
    if ladle:
        bot.send_message(message.chat.id, wait_ms)
        bot.send_message(config.get('admin_group_chat_id'), anket('Половник', message.from_user.first_name, message.from_user.id, ladle_material=ladle_material, city=message.text), reply_markup=admin_keyboard)
    if spoons:
        mes2 = bot.send_message(message.chat.id, spoons_ms[1])
        bot.register_next_step_handler(mes2, ankets_creator, spoons_city=message.text)
    if spoons_city and not spoons_work:
        mes3 = bot.send_message(message.chat.id, spoons_ms[2])
        bot.register_next_step_handler(mes3, ankets_creator, spoons_work=message.text, spoons_cit=spoons_city)
    if spoons_work and spoons_city:
        bot.send_message(message.chat.id, wait_ms)
        bot.send_message(config.get('admin_group_chat_id'), anket('Ложки', message.from_user.first_name, message.from_user.id, spoons_data=[spoons_work, message.text], city=spoons_city), reply_markup=admin_keyboard)
    if forks:
        bot.send_message(message.chat.id, wait_ms)
        bot.send_message(config.get('admin_group_chat_id'), anket('Вилки', message.from_user.first_name, message.from_user.id), reply_markup=admin_keyboard)
    if knives:
        mes2 = bot.send_message(message.chat.id, spoons[0])
        bot.register_next_step_handler(mes2, ankets_creator, knives_city=message.text)
    if knives_city:
        bot.send_message(message.chat.id, wait_ms)
        bot.send_message(config.get('admin_group_chat_id'), anket('Ножи', message.from_user.first_name, message.from_user.id, city=knives_city, knives_set=message.text), reply_markup=admin_keyboard)
    if dishes:
        bot.send_message(message.chat.id, wait_ms)
        bot.send_message(config.get('admin_group_chat_id'), anket('Тарелки', message.from_user.first_name, message.from_user.id, dishes_type=message.text), reply_markup=admin_keyboard)
    if technical_support:
        bot.send_message(message.chat.id, technical_support_wait_ms)
        bot.send_message(config.get('admin_group_chat_id'), tech_support_report(message.from_user.first_name, message.from_user.id, message.text))


def anket(objec, username, user_id, ladle_material=None, spoons_data=None, city=None, forks=None, knives_set=None, dishes_type=None):
    anketa = f'''
        Объект: {objec}
        Город: {city}
        Юзернейм: {username}
        Юзер ID: {user_id}
        '''

    if ladle_material:
        anketa = f'''Объект: {objec}
            Материал {ladle_material}
            Город: {city}
            Юзернейм: {username}
            Юзер ID: {user_id}
            '''
    if spoons_data:
        anketa = f'''Объект: {objec}
            Город: {city}
            Что должны сделать {spoons_data[0]}
            Сумма за доставку {spoons_data[1]}
            Юзернейм: {username}
            Юзер ID: {user_id}
            '''
    if forks:
        anketa = f'''
            Объект: {objec}
            От вилок нужно: {forks}
            Юзернейм: {username}
            Юзер ID: {user_id}
            '''
    if knives_set:
        anketa = f'''
            Объект: {objec}
            Город: {city}
            Интересующие ножи: {knives_set}
            Юзернейм: {username}
            Юзер ID: {user_id}
            '''
    if dishes_type:
        anketa = f'''
            Объект: {objec}
            Тип тарелок: {dishes_type}
            Юзернейм: {username}
            Юзер ID: {user_id}
            '''
    return anketa

def tech_support_report(username, user_id, message):
    text = f'''
    ❗ПОСТУПИЛА ЗАЯВКА В ТЕХ. ПОДДЕРЖКУ❗
    От {username} (id {user_id})
    "{message}" 
    '''
    return text

bot.infinity_polling()
