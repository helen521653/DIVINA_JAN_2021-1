import telebot
from myToken import TOKEN

<<<<<<< Updated upstream

bot = telebot.TeleBot(TOKEN)  #Создаём подключение к боту
=======
bot = telebot.TeleBot('1514078312:AAHnVy-JhsMTGx9o3KtoikgXpAyeZoGrXDc')  #Создаём подключение к боту
>>>>>>> Stashed changes


@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])




bot.polling() #Забираем сообщения у бота



