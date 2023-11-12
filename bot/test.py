import telebot

# Ваш токен бота
TOKEN = ''
# Айди чата для администраторов
admin_chat_id = ''

bot = telebot.TeleBot(TOKEN)

# Словарь для хранения заявок
requests = {}
# Словарь для хранения информации о том, кто отвечает на заявку
responders = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправьте /apply, чтобы подать заявку.")


@bot.message_handler(commands=['apply'])
def apply(message):
    user_id = message.from_user.id

    # Проверяем, не подал ли пользователь уже заявку
    if user_id in requests:
        bot.send_message(user_id, "Вы уже подали заявку. Пожалуйста, подождите ответа администраторов.")
        return

    bot.send_message(user_id, "Введите ваш запрос:")
    bot.register_next_step_handler(message, process_request, user_id)


def process_request(message, user_id):
    request_text = message.text

    # Сохраняем заявку в словаре с указанием пользователя
    requests[user_id] = request_text
    responders[user_id] = message.chat.id

    # Отправляем заявку администраторам
    bot.send_message(admin_chat_id, f"Получена новая заявка от пользователя {user_id}:\n{request_text}")
    bot.send_message(user_id, "Ваша заявка принята. Пожалуйста, ожидайте ответа администраторов.")


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


if __name__ == '__main__':
    bot.polling(none_stop=True)
