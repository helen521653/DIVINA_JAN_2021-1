import telebot
from myToken1 import TOKEN
from random import randint

bot = telebot.TeleBot(TOKEN)  # Создаём подключение к боту
@bot.message_handler(commands=['start'])
def komands_start(message):
    bot.send_message(message.chat.id,'я умею много разного, разверну твои текстовы сообщения задом наперёд')
@bot.message_handler(commands=['pass'])
def komands_pass(message):
    bot.send_message(message.chat.id,'сгенерирую пароль')
    parol = randint(1000,9999)
    bot.send_message(message.chat.id, str(parol) )

bot.polling() #Забираем сообщения у бота
#He

@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])
    #bot.send_message(message.chat.id, "Hello")

