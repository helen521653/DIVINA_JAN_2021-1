import telebot


bot = telebot.TeleBot('1470110849:AAEK5skHRPMBB-X1pSUDiNFq1K3gusdR8hY')  #Создаём подключение к боту


@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])




bot.polling() #Забираем сообщения у бота



