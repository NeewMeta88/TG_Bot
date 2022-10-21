from cgitb import text
from email import message
from itertools import count
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
import markups as nav
from db import Database
from aiogram.types import InputFile
from config import TOKEN
import os

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = Database("C:/Users/egorr/Desktop/bot/database.db")

        # СТАРТ

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Для создания анкеты напиши: /anketa")

@dp.message_handler(commands=['anketa'])
async def anketa(message: types.Message):
    if (not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        db.add_save(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваш ник:")
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегестрированы!", reply_markup=nav.mainMenu)
        db.add_save(message.from_user.id)

        # МЕНЮ

@dp.message_handler(commands=['menu'])
async def anketa(message: types.Message):
    db.set_signup(message.from_user.id, "done")
    await bot.send_message(message.from_user.id, "МЕНЮ", reply_markup=nav.mainMenu)

        # ТЕСТ

@dp.message_handler(commands=['test'])
async def anketa(message: types.Message):
    db.clear_test(message.from_user.id)
    db.clear_question(message.from_user.id)
    db.clear_test_score(message.from_user.id)
    await bot.send_message(message.from_user.id, "Суть теста - узнать ваше отношение к различным жизненным явлениям.\nНа каждый вопрос будет 3 варианта ответа, выбирайте более подходящий для вас.")
    if db.get_question(message.from_user.id) == '0':
        await bot.send_message(message.from_user.id, "Вопрос №1:\nОцените вашу степень общительности:\n1. Вы легко находите общий язык с разными людьми.\n2. Вы спокойно общаетесь только с людьми, с которыми хорошо знакомы.\n3. Вам тяжело найти общий язык с другими людьми.", reply_markup=nav.mainMenu7)

inkb = InlineKeyboardMarkup(row_width=1,).add(InlineKeyboardButton(text='Нажми меня', callback_data='izi'))

        # СОВМЕСТИМОСТЬ

@dp.callback_query_handler(Text(startswith="conn"))
async def connect(call: types.CallbackQuery):
    
    other_id = str(db.get_find_id(call.from_user.id))
    your_id = str(call.from_user.id)
    your_score = int(db.get_test_score(your_id))
    other_score = int(db.get_test_score(other_id))
    your_test = str(db.get_test(your_id))
    other_test = str(db.get_test(other_id))
    if (your_test == '0'):
        await bot.send_message(call.from_user.id, "Вы еще не прошли тест и не можете проверять совместимость, чтобы пройти тест, нажмите на кнопку\n/test")
        await call.answer()
    elif (other_test == '0'):
        await bot.send_message(call.from_user.id, "Этот пользователь еще не прошел тест и вы не можете проверять с ним совместимость.")
        if (db.get_alert(other_id) != '1'):
            await bot.send_message(other_id, "Кто-то из пользователей, хотел проверить совместимость с вами, но не смог, так как вы еще не прошли тест, чтобы пройти тест и проверять совместимость нажмите на кнопку\n/test")
            db.set_alert(other_id)
        await call.answer()
    else:
        print("====================")
        print("User 1 = " + db.get_nickname(your_id))
        print("User 2 = " + db.get_nickname(other_id))
        print("Your score: "+ str(your_score))
        print("Other score: "+ str(other_score))
        print("Your diff: "+ str(abs(your_score - other_score)))
        print("Your diff*6: "+ str(((abs(your_score - other_score)*6))))
        print("Your sovm: "+ str(100 - (abs(your_score - other_score)*6)))
        print("====================\n")
        sovm = (100 - (abs(your_score - other_score)*6))
        db.set_sovm(your_id,sovm)
        await call.answer("Ваша совместимость:" + str(sovm)+ "%", show_alert=True)
        # await bot.send_message(call.from_user.id, "Ваша совместимость " + db.get_sovm(call.from_user.id) + "%")

        # ОСНОВА

@dp.message_handler(content_types=['text','photo'])
async def regestration(message: types.Message):

    x = 0

    if message.text == 'ПРОФИЛЬ':
        profile = InlineKeyboardMarkup(resize_keyboard = True)
        btnUrl1 = InlineKeyboardButton(text = "Инстаграм", url="https://www.instagram.com/" + db.get_inst(message.from_user.id))
        profile.add(btnUrl1)
        user_photo = InputFile("C:/Users/egorr/Desktop/bot/photos/" + str(message.from_user.id) + ".jpg")
        user_nickname = "Ваш ник: " + db.get_nickname(message.from_user.id)
        user_city = "Ваш город: " + db.get_city(message.from_user.id)
        user_status = "Есть (парень/девушка): " + db.get_status(message.from_user.id)
        await bot.send_message(message.from_user.id, "Ваш профиль:", reply_markup=nav.mainMenu4)
        await bot.send_photo(chat_id=message.chat.id, photo=user_photo, caption=user_nickname + "\n" + user_city + "\n" + user_status, reply_markup=profile)
    
    elif message.text == 'НАЗАД':
        await bot.send_message(message.from_user.id,"МЕНЮ" ,reply_markup=nav.mainMenu)

    elif message.text == 'ТЕСТ':
        if (db.get_test(message.from_user.id) == '1'):
            await bot.send_message(message.from_user.id, "Вы уже проходили тест, если хотите пройти еще раз, нажмите на кнопку \n /test", reply_markup=nav.mainMenu9)
        else:
            await bot.send_message(message.from_user.id, "Чтобы проверять совместимость с другими пользователями, пройдите небольшой тест (10 вопросов), нажав на кнопку \n /test", reply_markup=nav.mainMenu9)

    # ПРОСМОТР АНКЕТ

    if message.text == 'ПРОСМОТР АНКЕТ':
        await bot.send_message(message.from_user.id, 'Вы вошли в режим поиска собеседника, чтобы начать просмотр анкет, нажмите кнопку "ДАЛЬШЕ"', reply_markup=nav.mainMenu6)

    if message.text == 'ДАЛЬШЕ':
        db.clear_find_id(message.from_user.id)
        db.clear_sovm(message.from_user.id)
        user_id = str(db.find_user())
        db.set_find_id(message.from_user.id, user_id)
        while (str(user_id) == str(message.from_user.id)):
            user_id = str(db.find_user())
        profile = InlineKeyboardMarkup(row_width=1,resize_keyboard = True)
        btnUrl1 = InlineKeyboardButton(text = "Инстаграм", url="https://www.instagram.com/" + db.get_inst(user_id))
        conn = InlineKeyboardButton('Совместимость', callback_data="conn")
        # your_score = int(db.get_test_score(message.from_user.id))
        # other_score = int(db.get_test_score(user_id))
        # your_test = str(db.get_test(message.from_user.id))
        # other_test = str(db.get_test(user_id))
        # sovm = (100 - (abs(your_score - other_score)*6))
        profile.add(btnUrl1,conn)
        user_photo = InputFile("C:/Users/egorr/Desktop/bot/photos/" + user_id + ".jpg")
        user_nickname = "Ник: " + db.get_nickname(user_id)
        user_city = "Город: " + db.get_city(user_id)
        user_status = "Есть (парень/девушка): " + db.get_status(user_id)
        await bot.send_photo(chat_id=message.chat.id, photo=user_photo, caption=user_nickname + "\n" + user_city + "\n" + user_status, reply_markup=profile)

        
        # if (your_test == '0'):
        #     await bot.send_message(message.from_user.id, "Вы еще не прошли тест и не можете проверять совместимость, чтобы пройти тест, нажмите на кнопку\n/test")
        # elif (other_test == '0'):
        #     await bot.send_message(message.from_user.id, "Этот пользователь еще не прошел тест и вы не можете проверять с ним совместимость.")
        #     if (db.get_alert(user_id) != '1'):
        #         await bot.send_message(user_id, "Кто-то из пользователей, хотел проверить совместимость с вами, но не смог, так как вы еще не прошли тест, чтобы пройти тест и проверять совместимость нажмите на кнопку\n/test")
        #         db.set_alert(user_id)
        # else:

        #     await bot.send_message(message.from_user.id, "Ваша совместимость:" + str(sovm)+ "%")

    elif message.text == 'ИЗМЕНИТЬ':
        await bot.send_message(message.from_user.id, "Чтобы вернуться в меню нажмите \n /menu")
        await bot.send_message(message.from_user.id, "Укажите ваш ник:")
        db.set_signup(message.from_user.id, "setnickname")

    # РЕГИСТРАЦИЯ

    elif db.get_signup(message.from_user.id) == "setnickname":
        if (len(message.text) > 15):
            await bot.send_message(message.from_user.id, "Никнейм не должен превышать 15 символов!")
        elif '@' in message.text or '/'  in message.text:
            await bot.send_message(message.from_user.id, "Вы ввели запрещенный символ!")
        else:
            db.set_nickname(message.from_user.id, message.text)
            db.set_signup(message.from_user.id, "setcity")
            await bot.send_message(message.from_user.id, "Укажите ваш город:")

    elif db.get_signup(message.from_user.id) == "setcity":
        if '@' in message.text or '/'  in message.text:
            await bot.send_message(message.from_user.id, "Вы ввели запрещенный символ!")
        else:
            db.set_city(message.from_user.id, message.text)
            db.set_signup(message.from_user.id, "setinst")
            await bot.send_message(message.from_user.id, "Укажите ваш instagram:")

    elif db.get_signup(message.from_user.id) == "setinst":
        if '@' in message.text or '/'  in message.text:
            await bot.send_message(message.from_user.id, "Вы ввели запрещенный символ!")
        else:
            db.set_inst(message.from_user.id, message.text)
            db.set_signup(message.from_user.id, "setphoto")
            
            await bot.send_message(message.from_user.id, "Прикрепите свою фотографию:")
                

    elif db.get_signup(message.from_user.id) == "setphoto":
            await message.photo[-1].download("C:/Users/egorr/Desktop/bot/photos/" + str(message.from_user.id) + ".jpg")
            db.set_signup(message.from_user.id, "setstatus")
            await bot.send_message(message.from_user.id, "У вас есть парень/девушка?", reply_markup=nav.mainMenu2)

    elif db.get_signup(message.from_user.id) == "setstatus":
            db.set_signup(message.from_user.id, "setgender")
            await bot.send_message(message.from_user.id, "Вы парень или девушка?", reply_markup=nav.mainMenu3)
            db.set_status(message.from_user.id, message.text)

    elif db.get_signup(message.from_user.id) == "setgender":
            db.set_gender(message.from_user.id, message.text)
            db.set_signup(message.from_user.id, "setyear")
            await bot.send_message(message.from_user.id, "Укажите ваш год рождения:")

    elif db.get_signup(message.from_user.id) == "setyear":
            db.set_year(message.from_user.id, message.text)
            db.set_signup(message.from_user.id, "setgoro")
            await bot.send_message(message.from_user.id, "Укажите ваш знак зодиака:", reply_markup=nav.mainMenu5)

    elif db.get_signup(message.from_user.id) == "setgoro":
            db.set_goro(message.from_user.id, message.text)
            db.set_signup(message.from_user.id, "done")
            await bot.send_message(message.from_user.id, "Регистрация прошла успешно!", reply_markup=nav.mainMenu)
            await bot.send_message(message.from_user.id, "Чтобы проверять совместимость с другими пользователями, пройдите небольшой тест (10 вопросов), нажав на кнопку \n /test")
            print("====================\n" + "New User Registered: \n" + "Nick: " + db.get_nickname(message.from_user.id) + "\n" + "id: " + str(message.from_user.id) + "\n" + "====================\n")

    elif message.text == '1':
        if (db.get_test_bool(message.from_user.id) == str(1)):
            await bot.send_message(message.from_user.id, "Подождите, ответ обрабатывается")
            db.clear_test_bool(message.from_user.id)
        else:
            x+=1
            db.set_test_score(message.from_user.id, x)
            db.set_question(message.from_user.id)
            db.set_test_bool(message.from_user.id)
            await bot.send_message(message.from_user.id, "Ответ принят.", reply_markup=nav.mainMenu8)
    elif message.text == '2':
        if (db.get_test_bool(message.from_user.id) == str(1)):
            await bot.send_message(message.from_user.id, "Подождите, ответ обрабатывается")
            db.clear_test_bool(message.from_user.id)
        else:
            x+=2
            db.set_test_score(message.from_user.id, x)
            db.set_question(message.from_user.id)
            db.set_test_bool(message.from_user.id)
            await bot.send_message(message.from_user.id, "Ответ принят.", reply_markup=nav.mainMenu8)
    elif message.text == '3':
        if (db.get_test_bool(message.from_user.id) == str(1)):
            await bot.send_message(message.from_user.id, "Подождите, ответ обрабатывается")
            db.clear_test_bool(message.from_user.id)
        else:
            x+=3
            db.set_test_score(message.from_user.id, x)
            db.set_question(message.from_user.id)
            db.set_test_bool(message.from_user.id)
            await bot.send_message(message.from_user.id, "Ответ принят.", reply_markup=nav.mainMenu8)

    # ВОПРОСЫ НА ТЕСТ

    elif db.get_question(message.from_user.id) == '1':
        await bot.send_message(message.from_user.id, "Вопрос №2:\nОцените ваше отношение к вечеринкам:\n1. Было бы предложение, а со спросом бед не имеется.\n2. Хорошо себя чувствую в большой компании, но иногда нету желания идти на тусовку.\n3. Не нравятся шумные мероприятия, большие компании.", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)

    elif db.get_question(message.from_user.id) == '2':
        await bot.send_message(message.from_user.id, "Вопрос №3:\nОцените ваше отношение к спорту:\n1. Занимаюсь на постоянной основе.\n2. Не запускаю с этим вопросом, но не так регулярно уделяю этому время.\n3. Главнокомандующий диванных войск.", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)

    elif db.get_question(message.from_user.id) == '3':
        await bot.send_message(message.from_user.id, "Вопрос №4:\Оцените ваше отношение к компьютерным/мобильным играм:\n1. 10k гуль 1x1 mid zxc // 3500elo king // top 5 euro genshin // top 5 euro pubg// 40к кубков бравл\n2. Могу поиграть в свободное время.\n3. Это бессмысленная трата времени.", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)

    elif db.get_question(message.from_user.id) == '4':
        await bot.send_message(message.from_user.id, "Вопрос №5:\Оцените ваше отношение к учебе:\n1. Красный диплом // Золотая медаль ждут меня.\n2. Будет 5 - круто // Будет 3 - нормально.\n3. Бывает, появляюсь на парах/уроках.", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)

    elif db.get_question(message.from_user.id) == '5':
        await bot.send_message(message.from_user.id, "Вопрос №6:\nЧто вы выбираете из одежды:\n1. Off-White, Balenciaga, Moncler.\n2. Nike, The Nort Face, Stussy.\n3. H&M, Zara, Uniqlo.\n", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)

    elif db.get_question(message.from_user.id) == '6':
        await bot.send_message(message.from_user.id, "Вопрос №7(а):\nВыберите понравившихся музыкантов:\n1. Pharaoh, Скриптонит.\n2. КОСМОНАВТОВ НЕТ, Папин Олимпос.\n3. Rocket, Obladaet.", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)

    elif db.get_question(message.from_user.id) == '7':
        await bot.send_message(message.from_user.id, "Вопрос №7(б):\nВыберите понравившихся музыкантов:\n1. Макс Корж, Macan.\n2. Пошлая Молли, НЕРВЫ.\n3. Цинк Уродов, ТЯЖЕЛАЯ АТЛЕТИКА.", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)

    elif db.get_question(message.from_user.id) == '8':
        await bot.send_message(message.from_user.id, "Вопрос №7(в):\nВыберите понравившихся музыкантов:\n1. Big Baby Tape, FACE.\n2. Feduk, Mayot.\n3. Buda, Платина.", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)

    elif db.get_question(message.from_user.id) == '9':
        await bot.send_message(message.from_user.id, "Вопрос №8:\nОцените ваше отношение к семье:\n1. Вы с радостью проводите время с семьей.\n2. Вы спокойно общаетесь с членами семьи.\n3. Вам тяжело найти общий язык с членами семьи.", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)

    elif db.get_question(message.from_user.id) == '10':
        await bot.send_message(message.from_user.id, "Вопрос №9:\nОцените ваше отношение к деньгам:\n1. Не в деньгах счастье.\n2. С деньгами спокойнее.\n3. Деньги правят миром.", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)

    elif db.get_question(message.from_user.id) == '11':
        await bot.send_message(message.from_user.id, "Вопрос №10:\nОцените ваше отношение к жилью:\n1. Соглас(ен/на) и на рай в шалаше.\n2. 2-3х комнатная квартира с хорошим ремонтом.\n3. Аппартаменты с террасой в элитном жилом комплексе.", reply_markup=nav.mainMenu7)
        db.clear_test_bool(message.from_user.id)
    
    elif db.get_question(message.from_user.id) == '12':
        await bot.send_message(message.from_user.id, "Тест окончен, теперь вы можете проверять совместимость с пользователями.", reply_markup=nav.mainMenu)
        db.clear_test_bool(message.from_user.id)
        db.set_test(message.from_user.id)
        db.set_question(message.from_user.id)

    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)