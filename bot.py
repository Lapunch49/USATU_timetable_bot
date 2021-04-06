import config
import telebot
# There was Alsu

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, "Привет, пользователь!")

@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, "Меня только что создали, могу ответить только на /start и /help")


@bot.message_handler(content_types=['text'])
def handle_message(message):
    bot.send_message(message.chat.id,message.text)

bot.polling()
