import telebot
from texts import *
from keyboard import *
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BOT_TOKEN")
admin_chat_id = os.getenv("ADMIN_CHAT_ID")
bot = telebot.TeleBot(token, parse_mode='')
responders = {}
requests = {}


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, start_message[0], reply_markup=greet_kb2)


@bot.message_handler(func=lambda message: message.text == "Главное меню" or message.text == "главное меню")
def general_menu(message):
    bot.send_message(message.chat.id, start_message[1], reply_markup=user_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'Повар':
        mes = bot.send_message(call.message.chat.id, cook_ms, reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, cook=True)
    if call.data == 'Принять':
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                      reply_markup=y_keyboard)
        bot.send_message(chat_id=call.from_user.id, text="Ваша заявка принята ✅")
    if call.data == 'Отменить':
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                      reply_markup=n_keyboard)
        bot.send_message(chat_id=call.from_user.id, text="Ваша заявка отклонена ❌")
    if call.data == 'Половник':
        bot.send_message(call.message.chat.id, ladle_ms[0], reply_markup=ladle_keyboard)
    if call.data == 'Металическая ручка' or call.data == 'Деревяная ручка':
        mes = bot.send_message(call.message.chat.id, ladle_ms[1], reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, ladle=True, ladle_material=call.data)
    if call.data == 'Ложки':
        mes = bot.send_message(call.message.chat.id, spoons_ms[0], reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, spoons=True)
    if call.data == 'Вилки':
        mes = bot.send_message(call.message.chat.id, forks_ms, reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, forks=True)
    if call.data == 'Ножи':
        mes = bot.send_message(call.message.chat.id, knives_ms[1], reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, knives=True)
    if call.data == 'Тарелки':
        mes = bot.send_message(call.message.chat.id, dishes_ms, reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, dishes=True)
    if call.data == 'Чашки':
        mes = bot.send_message(call.message.chat.id, cups_ms[0], reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, cups=True)
    if call.data == 'Другие услуги':
        mes = bot.send_message(call.message.chat.id, other_services_ms[1], reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, other_services=True)
    if call.data == 'Бытовые устройства':
        mes = bot.send_message(call.message.chat.id, household_devices_ms[1], reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, household_devices=True)
    if call.data == 'Посылка с Москвы':
        mes = bot.send_message(call.message.chat.id, parcel_from_Moscow_ms[1], reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, parcel_from_Moscow=True)
    if call.data == 'Размещение поста на канале':
        mes = bot.send_message(call.message.chat.id, posting_on_a_channel_ms[1], reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, posting_on_a_channel=True)
    if call.data == 'Тех. поддержка':
        mes = bot.send_message(call.message.chat.id, technical_support_ms, reply_markup=return_button_keyboard)
        bot.register_next_step_handler(mes, ankets_creator, technical_support=True)


def ankets_creator(message, cook=None, ladle=None, spoons=None, knives=None, forks=None, dishes=None, cups=None,
                   other_services=None, household_devices=None, parcel_from_Moscow=None, posting_on_a_channel=None,
                   technical_support=None, ladle_material=None, spoons_city=None,
                   spoons_work=None, knives_city=None, cups_city=None, other_services_city=None,
                   household_devices_city=None, parcel_from_Moscow_city=None, posting_on_a_channel_city=None):
    if check_return(message):
        if cook:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Повар', "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id,
                                   cook_city=message.text),
                             reply_markup=admin_keyboard, parse_mode="Markdown")

        if ladle:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Половник', "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id,
                                   ladle_material=ladle_material, city=message.text), reply_markup=admin_keyboard,
                             parse_mode="Markdown")

        if spoons:
            mes2 = bot.send_message(message.chat.id, spoons_ms[1])
            bot.register_next_step_handler(mes2, ankets_creator, spoons_city=message.text)
        if spoons_city and not spoons_work:
            mes3 = bot.send_message(message.chat.id, spoons_ms[2])
            bot.register_next_step_handler(mes3, ankets_creator, spoons_work=message.text, spoons_city=spoons_city)
        if spoons_work and spoons_city:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Ложки', "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id,
                                   spoons_data=[spoons_work, message.text], city=spoons_city),
                             reply_markup=admin_keyboard,
                             parse_mode="Markdown")

        if forks:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Вилки', "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id,
                                   forks_znach=message.text),
                             reply_markup=admin_keyboard, parse_mode="Markdown")

        if knives:
            mes2 = bot.send_message(message.chat.id, knives_ms[0])
            bot.register_next_step_handler(mes2, ankets_creator, knives_city=message.text)
        if knives_city:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Ножи', "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id,
                                   city=knives_city,
                                   knives_set=message.text), reply_markup=admin_keyboard, parse_mode="Markdown")

        if dishes:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Тарелки', "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id, dishes_type=message.text),
                             reply_markup=admin_keyboard, parse_mode="Markdown")

        if cups:
            mes2 = bot.send_message(message.chat.id, cups_ms[1])
            bot.register_next_step_handler(mes2, ankets_creator, cups_city=message.text)
        if cups_city:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Чашки', "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id,
                                   city=cups_city,
                                   cups_set=message.text), reply_markup=admin_keyboard, parse_mode="Markdown")

        if other_services:
            mes2 = bot.send_message(message.chat.id, other_services_ms[0])
            bot.register_next_step_handler(mes2, ankets_creator, other_services_city=message.text)
        if other_services_city:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Другие услуги', "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id,
                                   city=other_services_city,
                                   other_services_set=message.text), reply_markup=admin_keyboard, parse_mode="Markdown")

        if household_devices:
            mes2 = bot.send_message(message.chat.id, household_devices_ms[0])
            bot.register_next_step_handler(mes2, ankets_creator, household_devices_city=message.text)
        if household_devices_city:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Бытовые устройства', "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id,
                                   city=household_devices_city,
                                   household_devices_set=message.text), reply_markup=admin_keyboard,
                             parse_mode="Markdown")

        if parcel_from_Moscow:
            mes2 = bot.send_message(message.chat.id, parcel_from_Moscow_ms[0])
            bot.register_next_step_handler(mes2, ankets_creator, parcel_from_Moscow_city=message.text)
        if parcel_from_Moscow_city:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Посылка с Москвы', "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id,
                                   city=parcel_from_Moscow_city,
                                   parcel_from_Moscow_set=message.text), reply_markup=admin_keyboard,
                             parse_mode="Markdown")

        if posting_on_a_channel:
            mes2 = bot.send_message(message.chat.id, parcel_from_Moscow_ms[0])
            bot.register_next_step_handler(mes2, ankets_creator, posting_on_a_channel_city=message.text)
        if posting_on_a_channel_city:
            user_id = message.from_user.id
            user_name = message.from_user.username
            bot.send_message(message.chat.id, wait_ms)
            bot.send_message(admin_chat_id,
                             anket('Размещение поста на канале',
                                   "@[" + user_name + "](tg://user?id=" + str(user_id) + ")",
                                   message.from_user.id,
                                   city=posting_on_a_channel_city,
                                   posting_on_a_channel_set=message.text)
                             , reply_markup=admin_keyboard,
                             parse_mode="Markdown")

        if technical_support:
            user_id = message.from_user.id
            request_text = message.text
            requests[user_id] = request_text
            responders[user_id] = message.chat.id
            bot.send_message(admin_chat_id, f"Получена новая заявка от пользователя {user_id}:\n{request_text}")
            bot.send_message(user_id, "Ваша заявка принята. Пожалуйста, ожидайте ответа администраторов.")


def anket(object, username, user_id, ladle_material=None, spoons_data=None, city=None, knives_set=None,
          dishes_type=None, cups_set=None, posting_on_a_channel_set=None, parcel_from_Moscow_set=None,
          household_devices_set=None, other_services_set=None, forks_znach=None, cook_city=None):
    questionnaire = f'''
        '''
    if cook_city:
        questionnaire = f'''
Объект: Повар
Город: {cook_city}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    if ladle_material:
        questionnaire = f'''
Объект: {object}
Материал: {ladle_material}
Город: {city}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    if spoons_data:
        questionnaire = f'''Объект: {object}
Город: {city}
Что должны сделать: {spoons_data[0]}
Сумма за доставку: {spoons_data[1]}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    if forks_znach:
        questionnaire = f'''
Объект: {object}
От вилок нужно: {forks_znach}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    if knives_set:
        questionnaire = f'''
Объект: {object}
Город: {city}
Интересующие ножи: {knives_set}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    if cups_set:
        questionnaire = f'''
Объект: {object}
Город: {city}
Ручка: {cups_set}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    if other_services_set:
        questionnaire = f'''
Объект: {object}
Город: {city}
Услуга: {other_services_set}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    if household_devices_set:
        questionnaire = f'''
Объект: {object}
Город: {city}
Устройство: {household_devices_set}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    if parcel_from_Moscow_set:
        questionnaire = f'''
Объект: {object}
Город: {city}
Посылка: {parcel_from_Moscow_set}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    if posting_on_a_channel_set:
        questionnaire = f'''
Объект: {object}
Город: {city}
Оказание услуги: {posting_on_a_channel_set}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    if dishes_type:
        questionnaire = f'''
Объект: {object}
Тип тарелок: {dishes_type}
Пользователь: {username}
ID пользователя: {user_id}
            '''
    return questionnaire


@bot.message_handler(
    func=lambda message: message.chat.id == int(admin_chat_id) and message.text.startswith('Админ ответ:'))
def respond_to_user(message):
    user_id = int(message.text.split(':')[1])
    message_admin = str(message.text.split(':')[2])
    if user_id in requests:
        bot.send_message(responders[user_id], f"Ответ администратора:\n{message_admin}")
        del requests[user_id]
    else:
        bot.send_message(message.chat.id, "Пользователь не найден в списке ожидания ответа.")


def check_return(message):
    if message.text == 'Отменить заявку':
        bot.send_message(message.chat.id, return_anket_ms)
        general_menu(message)
        return False
    else:
        return True


if __name__ == '__main__':
    bot.polling(none_stop=True)
