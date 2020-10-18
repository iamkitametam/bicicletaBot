import telebot
import os
TOKEN = os.environ["TOKEN"]


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я учу людей испанскому!")


bot.polling()
