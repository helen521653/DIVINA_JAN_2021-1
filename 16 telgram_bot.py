import telebot
from myToken1 import TOKEN


bot = telebot.TeleBot(TOKEN)  #Создаём подключение к боту

@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])

bot.polling() #Забираем сообщения у бота



