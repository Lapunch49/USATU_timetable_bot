
# @bot.message_handler(commands = ['url'])
# def url(message):
#     markup = types.InlineKeyboardMarkup()
#     btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
#     markup.add(btn_my_site)
#     bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)

# A = [''] * 3
# for i in range(3): 
#     A[i] = [''] * 4
# print(A)

# from datetime import datetime as dt
# now = dt.now()
# print(f"Текущее время {now:%d.%m.%Y %H:%M}")

# s=7
# s += 1
# print(s)

# for i in range(1,4):
#     print(i)

# a = [''] * 24
# for i in range(24): 
#     a[i] = [''] * 2

# print (a[22])

# i=0
# print(type(i))


# from parser import num_of_this_week

# print(num_of_this_week)




####################

# import telebot
# import schedule

# bot = telebot.TeleBot('1729441005:AAGacM3G6DxnuaHsBYx6LXTJZzDxKrQK0AQ')

# #a = "1093555008"
# @bot.message_handler()
# def send_message(id):
#     bot.send_message(id,"Привет!")

# schedule.every().day.at("02:30").do(send_message,"1093555008")

# bot.polling()

######################
# import telebot
# import config

# bot = telebot.TeleBot(config.TOKEN)

# @bot.message_handler(content_types=['text'])
# def handle_message(message):
#     bot.send_message(message.chat.id,message.text)
#     print(message)

# bot.polling()

# import schedule 
# import time

# def ok():
#     print('ok')

# def ok2():
#     print('ok2')

# schedule.every(0.1).minutes.do(ok)
# schedule.every(1).to(2).minutes.do(ok2)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

faculty = 'ФИРТ'
if not (faculty == 'ФИРТ' or faculty == 'АВИЭТ' or faculty == 'ИАТМ' or faculty == 'ИНЭК' or faculty == 'ОНФ' or faculty == 'УАТ' or faculty == 'ФАДЭТ' or faculty == 'ФЗЧС' or faculty == 'Аспирантура'):
    print('Нет')
 
