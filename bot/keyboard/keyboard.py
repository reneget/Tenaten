from telebot import types

user_keyboard = types.InlineKeyboardMarkup()
general_menu_btn = types.InlineKeyboardButton(text='Главное меню', callback_data='Главное меню')
cook_btn = types.InlineKeyboardButton(text='Повар', callback_data='Повар')
ladle_btn = types.InlineKeyboardButton(text='Половник', callback_data='Половник')
spoons_btn = types.InlineKeyboardButton(text='Ложки', callback_data='Ложки')
knives_btn = types.InlineKeyboardButton(text='Ножи', callback_data='Ножи')
forks_btn = types.InlineKeyboardButton(text='Вилки', callback_data='Вилки')
dishes_btn = types.InlineKeyboardButton(text='Тарелки', callback_data='Тарелки')
cups_btn = types.InlineKeyboardButton(text='Чашки', callback_data='Чашки')
other_services_btn = types.InlineKeyboardButton(text='Другие услуги', callback_data='Другие услуги')
household_devices_btn = types.InlineKeyboardButton(text='Бытовые устройства', callback_data='Бытовые устройства')
parcel_from_Moscow_btn = types.InlineKeyboardButton(text='Посылка с Москвы', callback_data='Посылка с Москвы')
posting_on_a_channel_btn = types.InlineKeyboardButton(text='Размещение поста на канале',
                                                      callback_data='Размещение поста на канале')
replica_of_dishes_btn = types.InlineKeyboardButton(text='Копия посуды', callback_data='Копия посуды')
technical_support_btn = types.InlineKeyboardButton(text='Тех. поддержка', callback_data='Тех. поддержка')

user_keyboard.row(general_menu_btn)
user_keyboard.row(ladle_btn, spoons_btn, knives_btn)
user_keyboard.row(forks_btn, dishes_btn, cups_btn)
user_keyboard.row(cook_btn, parcel_from_Moscow_btn, replica_of_dishes_btn)
user_keyboard.row(posting_on_a_channel_btn, household_devices_btn)
user_keyboard.add(other_services_btn)
user_keyboard.add(technical_support_btn)

admin_keyboard = types.InlineKeyboardMarkup()
y_btn = types.InlineKeyboardButton(text='✅ Принять', callback_data='Принять')
n_btn = types.InlineKeyboardButton(text='❌ Отменить', callback_data='Отменить')
admin_keyboard.row(y_btn, n_btn)

y_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='✅ВЫ ПРИНЯЛИ ЗАЯВКУ✅', callback_data='8==D'))
n_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='❌ВЫ ОТМЕНИЛИ ЗАЯВКУ❌', callback_data='8==D'))

ladle_keyboard = types.InlineKeyboardMarkup()
m_button = types.InlineKeyboardButton(text='⛓ Металическая ручка', callback_data='Металическая ручка')
t_button = types.InlineKeyboardButton(text='🌳 Деревянная ручка', callback_data='Деревяная ручка')
ladle_keyboard.row(m_button, t_button)
