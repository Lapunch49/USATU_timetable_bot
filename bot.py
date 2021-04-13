import config
import telebot
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import schedule
import time


import sqlite3

def users_bd_function(id):
    conn = sqlite3.connect("users_base.db ")
    cursor = conn.cursor()

    #Создание таблицы albums
    cursor.execute("""INSERT INTO usersbase(user_id) VALUES(?);""",(id,))

    conn.commit()

def parser_function():
    num_of_week = ''
    # num_of_lesson = 1 #1 пара
    # num_of_day_of_week = 2 #понедельник
    days_of_week = ['','ПН','ВТ','СР','ЧТ','ПТ','СБ']
    a = [''] * 44
    for i in range(44): 
        a[i] = [''] * 2

    i=0

    driver = webdriver.Firefox()
    driver.get("https://lk.ugatu.su/raspisanie/#timetable")

    name_of_faculty = Select(driver.find_element_by_id('id_faculty'))
    name_of_faculty.select_by_visible_text('ФИРТ')

    num_of_course = Select(driver.find_element_by_id('id_klass'))
    num_of_course.select_by_value('1')

    time.sleep(2)

    name_of_group = Select(driver.find_element_by_id('id_group'))
    name_of_group.select_by_visible_text('ПРО-127Б')

    driver.find_element_by_css_selector('.centered-horizontal > div:nth-child(1) > input:nth-child(1)').click()

    #######

    num_of_this_week = driver.find_elements_by_css_selector('div.row:nth-child(3) > p:nth-child(4) > font:nth-child(1)')[0].text

    for num_of_day_of_week in range(2,8):
        #print('\n\n\n',days_of_week[num_of_day_of_week-1])
        for num_of_lesson in range(1,8):
            i += 1
            a[i][0]=driver.find_elements_by_css_selector(f'#schedule > tbody:nth-child(2) > tr:nth-child({num_of_lesson}) > td:nth-child({num_of_day_of_week})')[0].text
            if a[i][0] != '':
                #print(num_of_lesson, 'пара')
                a[i][1] = a[i][0].split('\n')
                #print(a[i][1])
    
    driver.close()

    return a, num_of_this_week

bot = telebot.TeleBot(config.TOKEN)

faculty=''
course=0
group=''

@bot.message_handler(commands=['start'])
def start_handler(message):
    users_bd_function(message.chat.id)
    bot.send_message(message.from_user.id, '''Привет, пользователь USATU_timetable_bot!
Чтобы бот смог вам помочь, ответьте на следующие вопросы:''')
    bot.send_message(message.from_user.id, "На каком факультете вы учитесь?\n(Введите название факультета, например, ФИРТ или введите Аспирантура)")
    bot.register_next_step_handler(message, get_faculty) #следующий шаг – функция get_faculty

def get_faculty(message):
    global faculty
    faculty=message.text
    # while not (faculty == 'ФИРТ' or faculty == 'АВИЭТ' or faculty == 'ИАТМ' or faculty == 'ИНЭК' or faculty == 'ОНФ' or faculty == 'УАТ' or faculty == 'ФАДЭТ' or faculty == 'ФЗЧС' or faculty == 'Аспирантура'):
    #     try:
    #         faculty=message.text
    #     except:
    #         bot.send_message(message.from_user.id, 'Что-то пошло не так, попробуйте ввести заново')
    bot.send_message (message.chat.id,"На каком курсе вы учитесь? (введите число)")
    bot.register_next_step_handler(message, get_course)

def get_course(message):
    global course
    #course=int(message.text)
    course=message.text
    # while not(course >= 1 and course <=6):
    #     bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    #     course=int(message.text)
    #     if True:
    #         course = int(message.text) 
    #     else:
    #         bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    # if (course >= 1 and course <=6):
    #     1
    # else:
    #     bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        
    bot.send_message (message.chat.id,"В какой группе вы учитесь? (например ПРО-127Б)")
    bot.register_next_step_handler(message, get_group)

def get_group(message):
    global group
    group=message.text
    bot.send_message (message.chat.id,"Я сохранил эту информацию, сейчас найду ваше расписание.")
    # можно ли далее   help_handler(message)

@bot.message_handler(commands=['help'])
def help_handler(message):
    str="Какие команды я умею выполнять:\n"
    str += "/help - показать, какие команды я умею выполнять\n"
    str += "/start - дать боту информацию о себе\n"
  #  str += "/restart - дать боту новую информацию о себе\n"
    str += "/schedule - показать актуальное расписание на эту неделю\n"
#    str += "/deactivate - запретить отправлять сообщения о парах\n"
       
    bot.send_message(message.from_user.id, str)

@bot.message_handler(commands=['schedule']) #показать актуальное расписание на эту неделю
def schedule_handler(message):
    #bot.send_message(message.from_user.id, 'Пожалуйста, подождите несколько секунд')
    i=0
    days_of_week = ['','✔️ПН','✔️ВТ','✔️СР','✔️ЧТ','✔️ПТ','✔️СБ']
    try:
        a,num_of_this_week=parser_function()
        msg=('\n📎Расписание на '+num_of_this_week+' неделю📎')
        bot.send_message(message.from_user.id,text = msg, parse_mode = "Markdown")
        for num_of_day_of_week in range(2,8):
            msg=''
            #bot.send_message(message.from_user.id, days_of_week[num_of_day_of_week-1])
            #print(days_of_week[num_of_day_of_week-1])
            msg += ('*'+days_of_week[num_of_day_of_week-1]+'*')

            for num_of_lesson in range(1,8):
                i+=1
                if a[i][0] != '':
                    #bot.send_message(message.from_user.id, num_of_lesson, 'пара')
                    #print(num_of_lesson, 'пара')
                    msg += '\n' 
                    msg += (str(num_of_lesson) + ' пара')
                    msg += '\n' 

                    for j in range(0,len(a[i][1])):
                        if a[i][1][j] != ',' and a[i][1][j] !='':
                            #bot.send_message(message.from_user.id, a[i][1][j])
                            #print(a[i][1][j])
                            msg += '\n'
                            msg += a[i][1][j]

                    msg += '\n'
        
            bot.send_message(message.from_user.id, text = msg,parse_mode = "Markdown")
    except:
        bot.send_message(message.from_user.id, "Не удалось загрузить расписание, попробуйте ввести другие данные о себе или попробуйте позже")

@bot.message_handler(content_types=['text'])
def handle_message(message): 
    bot.send_message(message.chat.id,'Я вас не понял(\nВоспользуйтесь командой /help')

# @bot.message_handler(content_types=['voice'])
# def handle_message(message):
#     bot.send_message(message.chat.id,'Я вас не понял(\nВоспользуйтесь командой /help')
    

bot.polling()
