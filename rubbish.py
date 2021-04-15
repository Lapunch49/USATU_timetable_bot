
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
# print(f"Текущее время {now: %H:%M}")
# print(now.today().weekday()+1)
# print(dt.now().weekday()+1)

# import schedule
# import time
# from datetime import datetime as dt

# time_of_classes=['','05:25','09:35','12:00','13:45','16:00','17:45','19:30']

# num_day_of_week = dt.now().weekday()+1
# j=1
# now = dt.now()
# print(now: '{%H:%M}')
# t='{now: %H:%M}'
# print(t)
# if t in time_of_classes:
#     print('gj')
# else:
#     print('fgh')
#     #print('{now: %H:%M}')
import time
import schedule
from datetime import datetime as dt
print( today.strftime("%Y-%m-%d-%H.%M.%S") )





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

# faculty = 'ФИРТ'
# if not (faculty == 'ФИРТ' or faculty == 'АВИЭТ' or faculty == 'ИАТМ' or faculty == 'ИНЭК' or faculty == 'ОНФ' or faculty == 'УАТ' or faculty == 'ФАДЭТ' or faculty == 'ФЗЧС' or faculty == 'Аспирантура'):
#     print('Нет')

#b = driver.find_elements_by_css_selector(f'#schedule > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')[0].text
# a[5][0]=driver.find_elements_by_css_selector('#schedule > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(3)')[0].text
# print(a[1][0])

# if a[1][0] != '':
#     a[1][1] = a[1][0].split('\n')
#     print(a[1][1])
#     # for i in a[1][1]:
#     #     print(i)
#     print(a[1][1][2])

# a3=driver.find_elements_by_css_selector('#schedule > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2)')[0].text

# if a3 != 0:
#     print('да')



#cursor.execute("""INSERT INTO usersbase(user_id, faculty) VALUES('Kate','ФИРТ');""")

#cursor.execute("""ALTER TABLE usersbase ADD COLUMN consent BIT""")

# cursor.execute("""INSERT INTO users(users, passwords)
#     VALUES('Kate','1234');""")

#cursor.execute("""INSERT INTO users(users)
 #    VALUES('Katerrr');""")

#cursor.execute("UPDATE users SET users=? WHERE users=? WHERE passwords=?;", ("Kate2","Kate","null"))

#cursor.execute("DELETE FROM users WHERE users=?;", ("Katerrr",))

# cursor.execute("SELECT * FROM users WHERE passwords='1234';") #  * - все

# result = cursor.fetchmany(8)
# print(result)

#conn.commit() #завершение соединения с бд
 
#b = input()
# while b!='dfg':
#     try:
#         print('Попробуйте еще раз')
#         b=input() 
#     except: 
#         pass


# week = ['','mon','tue','wed','thu','fri','sat']
    
# b = [''] * 44
# for j in range(44): 
#         b[j] = [''] * 2

# for j in range(1,43):
#     b[j][0]= str(j % 7)
#     if b[j][0]=='0':
#         b[j][0]='7'
#     b[j][1] = week[(j-1) // 7+1] + str(b[j][0])
# print (b,'\n\n')
# print (b[13])

# print(int('5')+1)

# import sqlite3

# conn = sqlite3.connect("users_base.db")
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM usersbase;")
# id_chat_array = cursor.fetchmany()
# conn.commit()
# print(id_chat_array[0][0])