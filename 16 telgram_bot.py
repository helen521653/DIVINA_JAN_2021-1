import telebot
from myToken import TOKEN
from random import randint

bot = telebot.TeleBot(TOKEN)  # Создаём подключение к боту


@bot.message_handler(commands=['start'])
def komanda_start(message):
    bot.send_message(message.chat.id, "Я умею много разного, например текстовые сообщения я разворачиваю задом наперёд")

@bot.message_handler(commands=['pass'])
def komanda_start(message):
    bot.send_message(message.chat.id, "Я сгенерирую тебе пароль из 4х цифр")
    rand_number = randint(1000, 9999)
    bot.send_message(message.chat.id, str(rand_number) )





@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])
    #bot.send_message(message.chat.id, "Hello")


bot.polling()  # Забираем сообщения у бота
