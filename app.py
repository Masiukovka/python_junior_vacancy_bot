TOKEN = "5315636355:AAHdCLMTtf6ndLs9WFP8WFQcjlAkYWR0QkU"

import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
