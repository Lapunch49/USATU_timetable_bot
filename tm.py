import telebot
import schedule
import time
from datetime import datetime as dt


bot = telebot.TeleBot('1668653860:AAH61P0HXn9K5yNmYXuiqLeDcOuMdZJQXZE')

num_of_this_week = 33

time_of_classes=['','05:50','09:35','12:00','13:45','16:00','17:45','19:30']

@bot.message_handler()
def send_messange():
    num_day_of_week = dt.now().weekday()+1
    j=1
    now = dt.now()
    while (time_of_classes[j]!='{now: %H:%M}' and j<len(time_of_classes)):
        j += 1
   # получить все записи из таблицы c ID чатов и записать в переменную id_chat_array
    conn = sqlite3.connect("users_base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usersbase;")
    id_chat_array = cursor.fetchmany()
    conn.commit()

    for i in range(0, len(id_chat_array)):
        if id_chat_array[i] != message.chat.id:
            bot.send_message(message.chat.id,"Ты еще не ввел данные. Так вперед \start")
        else:
            conn = sqlite3.connect("schedule_base.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM schedbase WHERE st_group={id_chat_array[i][3]};")
            timetable = cursor.fetchmany(1)
            conn.commit()

            # num_day_of_week = dt.now().weekday()+1
            # j=1
            # now = dt.now()
            # while (classes[j]!='{now: %H:%M}' or j<len(classes)):
            #     j +=1
            
            if j!=len(classes) and timetable[(num_day_of_week-1)*7+j]!=None and timetable[(num_day_of_week-1)*7+j]!='':
                msg += ('\n' + str(j) + ' пара\n\n')
                msg += str(timetable[(num_day_of_week-1)*7+j])
                msg += '\n'
                bot.send_message(id_chat_array[i][0],msg)

# num_day_of_week = dt.now().weekday()+1
# j=1
# now = dt.now()
# while (time_of_classes[j]!='{now: %H:%M}' and j<len(time_of_classes)-1):
#     j += 1

# print(j)


for i in range(1,8):
    schedule.every().day.at(time_of_classes[i]).do(send_messange)

while True:
    schedule.run_pending()
    time.sleep(1)

bot.polling()    

