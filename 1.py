
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


import parser

print(parser.num_of_this_week)

