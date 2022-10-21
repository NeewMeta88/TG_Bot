"""
Этот бот принимает сообщение и пересылает в телеграм канал
"""
import os
import logging
import config
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
PHOTOS_ID = []

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(content_types=["photo"])
async def send_photo(message: types.Message):
    """Переслать фото в канал"""
    photo_id = message.photo[-1].file_id
    file_photo = bot.get_file(photo_id)
    print(file_photo)
    filename, file_extension = os.path.splitext(file_photo.file_path)
    print(file_extension)
    # downloaded_file_photo = bot.download_file(file_photo.file_path)

    # src = 'C:/Users/egorr/Desktop/bot/photos/' + photo_id + file_extension
    # with open(src,'wb') as new_file:
    #     new_file.write(downloaded_file_photo)
    #await bot.send_photo(message.from_user.id, photo_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)