import telebot
import os
TOKEN = os.environ["TOKEN"]


bot = telebot.TeleBot(TOKEN)

bot.send_message("Привет! Я учу людей испанскому!")
bot.send_message("Наши курсы состоят из 10 уроков, которые приходят каждый день")
bot.send_message("https://m.youtube.com/watch?v=Cn-q-04L1ZE")


@bot.message_handler(commands=['start', 'help'])  # отбивка функции в две строчки
def send_welcome(message):
    bot.reply_to(message, "Поехали!")


bot.polling()
