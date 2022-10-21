import telebot

bot = telebot.TeleBot("5123302046:AAFN1S44Mk2ZTXvWMsnATtBcfNVFQkkbtl8") # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()