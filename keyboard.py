from telebot import types

anket_keyboard = types.InlineKeyboardMarkup()
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

anket_keyboard.row(ladle_btn, spoons_btn, knives_btn)
anket_keyboard.row(forks_btn, dishes_btn, cups_btn)
anket_keyboard.row(cook_btn, parcel_from_Moscow_btn, replica_of_dishes_btn)
anket_keyboard.row(posting_on_a_channel_btn, household_devices_btn)
anket_keyboard.add(other_services_btn)
anket_keyboard.add(technical_support_btn)
