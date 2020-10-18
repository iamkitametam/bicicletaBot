import telebot
import os
TOKEN = os.environ["TOKEN"]


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])  # отбивка функции в две строчки
def send_welcome(message):
    bot.send_message("Привет! Я учу людей испанскому!")
    bot.send_message("Наши курсы состоят из 10 уроков, которые приходят каждый день")
    bot.send_message("https://m.youtube.com/watch?v=Cn-q-04L1ZE")
    bot.reply_to(message, "Поехали!")


bot.polling()


# $ heroku login
# $ heroku create
# $ git push heroku master
# $ heroku ps:scale bot=1
# $ heroku open