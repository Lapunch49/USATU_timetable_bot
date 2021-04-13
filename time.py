import telebot
import schedule
import time

bot = telebot.TeleBot('1668653860:AAH61P0HXn9K5yNmYXuiqLeDcOuMdZJQXZE')

#a = "1093555008"
# @bot.message_handler()
# def send_message(a):
#     bot.send_message(a,"Привет :)")

# schedule.every().day.at("01:46").do(send_message,"1093555008")

t="14:40"
@bot.message_handler()
def send_message(a):
    bot.send_message(a,"ПРИВЕТ")

a=['177164364','514402522','1093555008']

for i in range(0,3):
    schedule.every().day.at(t).do(send_message,a[i])



while True:
    schedule.run_pending()
    time.sleep(1)

bot.polling()