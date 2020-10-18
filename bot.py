import telebot

try:
    import credentials
except ImportError:
    raise ImportError('ImportError import credentials')

bot = telebot.TeleBot(credentials.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я учу людей испанскому!")


bot.polling()
