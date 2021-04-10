import config
import parser
import telebot

from parser import *

bot = telebot.TeleBot(config.TOKEN)

faculty=''
course=''
group=''


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, '''Привет, пользователь USATU_timetable_bot!
Чтобы бот смог вам помочь, ответьте на следующие вопросы:''')
    bot.send_message(message.from_user.id, "На каком факультете вы учитесь?")
    bot.register_next_step_handler(message, get_faculty) #следующий шаг – функция get_faculty

def get_faculty(message):
    global faculty
    faculty=message.text
    bot.send_message (message.chat.id,"На каком курсе вы учитесь? (введите число)")
    bot.register_next_step_handler(message, get_course)

def get_course(message):
    global course
    course=message.text
    bot.send_message (message.chat.id,"В какой группе вы учитесь? (например ПРО-127Б)")
    bot.register_next_step_handler(message, get_group)

def get_group(message):
    global group
    group=message.text
    bot.send_message (message.chat.id,"Я сохранил эту информацию, сейчас найду ваше расписание.")

@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, "Какие команды я умею выполнять:")

@bot.message_handler(commands=['shedule'])
def shedule_handler(message):
    for num_of_day_of_week in range(2,8):
        bot.send_message(message.from_user.id, days_of_week[num_of_day_of_week-1])
        for num_of_lesson in range(1,5):
            i+=1
            if a[i][0] != '':
                for j in range(0,4):
                    bot.send_message(message.from_user.id, a[i][1][j])

# @bot.message_handler(content_types=['text'])
# def handle_message(message):
#     try: 
#         bot.send_message(message.chat.id,message.text)
#     except: 
#         pass


bot.polling()
