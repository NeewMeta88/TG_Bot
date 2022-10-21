from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


    


btnProfile = KeyboardButton('ПРОФИЛЬ')
btnSub = KeyboardButton('ПОДПИСКА')
btnGo = KeyboardButton('ПРОСМОТР АНКЕТ')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnProfile,btnSub)
# mainMenu.add(btnProfile)
mainMenu.add(btnGo)

Yes = KeyboardButton('ДА')
No = KeyboardButton('НЕТ')

mainMenu2 = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu2.add(Yes,No)

Man = KeyboardButton('ПАРЕНЬ')
Woman = KeyboardButton('ДЕВУШКА')

mainMenu3 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
mainMenu3.add(Man,Woman)

changeProfile = KeyboardButton('ИЗМЕНИТЬ')
Test = KeyboardButton('ТЕСТ')
Back = KeyboardButton('НАЗАД')

mainMenu4 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
mainMenu4.add(changeProfile,Test,Back)

znak1 = KeyboardButton('ОВЕН')
znak2 = KeyboardButton('ТЕЛЕЦ')
znak3 = KeyboardButton('БЛИЗНЕЦЫ')
znak4 = KeyboardButton('РАК')
znak5 = KeyboardButton('ЛЕВ')
znak6 = KeyboardButton('ДЕВА')
znak7 = KeyboardButton('ВЕСЫ')
znak8 = KeyboardButton('СКОРПИОН')
znak9 = KeyboardButton('СТРЕЛЕЦ')
znak10 = KeyboardButton('КОЗЕРОГ')
znak11 = KeyboardButton('ВОДОЛЕЙ')
znak12 = KeyboardButton('РЫБЫ')

mainMenu5 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
mainMenu5.add(znak1, znak2, znak3, znak4, znak5, znak6, znak7, znak8, znak9, znak10, znak11, znak12)

Next = KeyboardButton('ДАЛЬШЕ')

mainMenu6 = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu6.add(Next,Back)

One = KeyboardButton('1')
Two = KeyboardButton('2')
Three = KeyboardButton('3')

mainMenu7 = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu7.add(One,Two,Three)
Continue = KeyboardButton('ПРОДОЛЖИТЬ')

mainMenu8 = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu8.add(Continue)

mainMenu9 = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu9.add(Back)