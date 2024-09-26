import config
import telebot
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import schedule
import sqlite3
from datetime import datetime as dt

def users_bd_function(id):
    conn = sqlite3.connect("users_base.db ")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM usersbase WHERE user_id = {id} ;")
    being_res = cursor.fetchmany(1)
    try:
        if being_res[0][0] != id:
            cursor.execute("""INSERT INTO usersbase(user_id) VALUES(?);""",(id,))
    except:
        cursor.execute("""INSERT INTO usersbase(user_id) VALUES(?);""",(id,))
    conn.commit()

def users_bd_f_faculty(id,faculty):
    conn = sqlite3.connect("users_base.db ")
    cursor = conn.cursor()

    cursor.execute("UPDATE usersbase SET faculty=? WHERE user_id=?;", (faculty,id))
    conn.commit()

def users_bd_f_course(id,course):
    conn = sqlite3.connect("users_base.db ")
    cursor = conn.cursor()

    cursor.execute("UPDATE usersbase SET course=? WHERE user_id=?;", (course,id))
    conn.commit()

def users_bd_f_group(id,group):
    conn = sqlite3.connect("users_base.db ")
    cursor = conn.cursor()

    cursor.execute("UPDATE usersbase SET st_group=? WHERE user_id=?;", (group,id))
    conn.commit()

def parser_function(num_of_next_week):
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

    num_week = Select(driver.find_element_by_id('WeekSchedule'))
    num_week.select_by_value(str(num_of_next_week))
    
    driver.find_element_by_css_selector('.centered-horizontal > div:nth-child(1) > input:nth-child(1)').click()

    #######

    #num_of_this_week = driver.find_elements_by_css_selector('div.row:nth-child(3) > p:nth-child(4) > font:nth-child(1)')[0].text

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

    #return a, num_of_this_week
    return a

def sched_bd_group(group_v):
    conn = sqlite3.connect("schedule_base.db ")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM schedbase WHERE st_group = '{group_v}' ;")
    being_res = cursor.fetchmany(1)
    try:
        if being_res[0][0] != group_v:
            cursor.execute("""INSERT INTO schedbase(st_group) VALUES(?);""",(group_v,))
    except:
        cursor.execute("""INSERT INTO schedbase(st_group) VALUES(?);""",(group_v,))
    conn.commit()

def parser_for_bd(faculty_v, course_v, group_v):
    num_of_week = ''
    # num_of_lesson = 1 #1 пара
    # num_of_day_of_week = 2 #понедельник
    days_of_week = ['','ПН','ВТ','СР','ЧТ','ПТ','СБ']
    week = ['','mon','tue','wed','thu','fri','sat']
    a = [''] * 44
    for i in range(44): 
        a[i] = [''] * 2

    i=0
    b = [''] * 44
    for j in range(44): 
        b[j] = [''] * 2

    for j in range(1,43):
        b[j][0]= str(j % 7)
        if b[j][0]=='0':
            b[j][0]='7'
        b[j][1] = week[(j-1) // 7+1] + str(b[j][0])


    driver = webdriver.Firefox()
    driver.get("https://lk.ugatu.su/raspisanie/#timetable")

    #num_of_week = driver.find_element_by_class_name('div.row:nth-child(3) > p:nth-child(4) > font:nth-child(1)').text

    name_of_faculty = Select(driver.find_element_by_id('id_faculty'))
    name_of_faculty.select_by_visible_text(faculty_v)

    num_of_course = Select(driver.find_element_by_id('id_klass'))
    num_of_course.select_by_value(str(course_v))

    time.sleep(2)

    name_of_group = Select(driver.find_element_by_id('id_group'))
    name_of_group.select_by_visible_text(group_v)

    driver.find_element_by_css_selector('.centered-horizontal > div:nth-child(1) > input:nth-child(1)').click()

    #######

    sched_bd_group(group_v)

    # cursor.execute(f"""INSERT INTO schedbase(st_group) VALUES({group});""")

    num_of_this_week = driver.find_elements_by_css_selector('div.row:nth-child(3) > p:nth-child(4) > font:nth-child(1)')[0].text

    conn = sqlite3.connect("schedule_base.db")
    cursor = conn.cursor()

    for num_of_day_of_week in range(2,8):
        for num_of_lesson in range(1,8):
            i += 1
            a[i][0]=driver.find_elements_by_css_selector(f'#schedule > tbody:nth-child(2) > tr:nth-child({num_of_lesson}) > td:nth-child({num_of_day_of_week})')[0].text
            cursor.execute(f"UPDATE schedbase SET {b[i][1]}=? WHERE st_group=?;", (a[i][0],group_v))
    
    conn.commit()

    i=0

    driver.close()

bot = telebot.TeleBot(config.TOKEN)

faculty=''
course=0
group=''
week = ['','mon','tue','wed','thu','fri','sat']
num_of_this_week = '33'
days_of_week = ['','✔️ПН','✔️ВТ','✔️СР','✔️ЧТ','✔️ПТ','✔️СБ']

@bot.message_handler(commands=['start']) #ndnncndsncjscfdn
def start_handler(message):
    users_bd_function(message.chat.id)
    bot.send_message(message.from_user.id, '''Привет, пользователь USATU_timetable_bot!
Чтобы бот смог вам помочь, ответьте на следующие вопросы:''')
    bot.send_message(message.from_user.id, "На каком факультете вы учитесь?\n(Введите название факультета, например, ФИРТ или введите Аспирантура)")
    bot.register_next_step_handler(message, get_faculty) #следующий шаг – функция get_faculty

def get_faculty(message):
    global faculty
    faculty=message.text
    available_faculties = ['ФИРТ', 'АВИЭТ', 'ИАТМ', 'ИНЭК', 'ОНФ', 'УАТ', 'ФАДЭТ', 'ФЗЧС', 'АСПИРАНТУРА']
    if faculty not in available_faculties:
        bot.send_message(message.from_user.id, f'Неверный факультет. Вот список доступных: {available_faculties}')
        return
    # while not (faculty == 'ФИРТ' or faculty == 'АВИЭТ' or faculty == 'ИАТМ' or faculty == 'ИНЭК' or faculty == 'ОНФ' or faculty == 'УАТ' or faculty == 'ФАДЭТ' or faculty == 'ФЗЧС' or faculty == 'Аспирантура'):
    #     bot.send_message(message.from_user.id, 'Что-то пошло не так, попробуйте ввести заново')
    #     get_faculty(message)
    #     try:
    #         faculty=message.text
    #     except:
    #         bot.send_message(message.from_user.id, 'Что-то пошло не так, попробуйте ввести заново')
    users_bd_f_faculty(message.chat.id, faculty)
    bot.send_message (message.chat.id,"На каком курсе вы учитесь? (введите число)")
    bot.register_next_step_handler(message, get_course)

def get_course(message):
    global course
    #course=int(message.text)
    course=message.text
    if not all(map(lambda x: x.isdigit(), course)):
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        return
    else:
        course = int(course)
        if course < 1 or course > 7:
            bot.send_message(message.from_user.id, 'Неверный значение курса. Курс должен быть в диапазон [1, 6].')
            return
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
    users_bd_f_course(message.chat.id,course)    
    bot.send_message (message.chat.id,"В какой группе вы учитесь? (например ПРО-127Б)")
    bot.register_next_step_handler(message, get_group)

def get_group(message):
    global group
    group=message.text
    users_bd_f_group(message.chat.id,group)
    bot.send_message (message.chat.id,"Я сохранил эту информацию. Можете узнать свое расписание на эту неделю с помощью команды /schedule")
    parser_for_bd(faculty, course, group)
    # можно ли далее   help_handler(message)

@bot.message_handler(commands=['help'])
def help_handler(message):
    str="Какие команды я умею выполнять:\n"
    str += "/help - показать, какие команды я умею выполнять\n"
    str += "/start - дать боту информацию о себе\n"
  #  str += "/restart - дать боту новую информацию о себе\n"
    str += "/schedule - показать актуальное расписание на эту неделю\n"
    str += "/schedule_next_week - показать расписание на следующую неделю\n"
    str += "/today - показать расписание на сегодня\n"
    str += "/next_day - показать расписание на завтра\n"
#    str += "/deactivate - запретить отправлять сообщения о парах\n"
       
    bot.send_message(message.from_user.id, str)

@bot.message_handler(commands=['schedule_next_week']) #показать расписание на следующую неделю
def schedule_handler(message):

    bot.send_message(message.from_user.id, 'Пожалуйста, подождите несколько секунд')
    i=0
    try:
        a=parser_function(int(num_of_this_week)+1)
        msg=('\n📎Расписание на '+str(int(num_of_this_week)+1)+' неделю📎')
        bot.send_message(message.from_user.id,text = msg, parse_mode = "Markdown")
        for num_of_day_of_week in range(2,8):
            msg=''
            msg += ('*'+days_of_week[num_of_day_of_week-1]+'*')

            for num_of_lesson in range(1,8):
                i+=1
                if a[i][0] != '':
                    msg += '\n' 
                    msg += (str(num_of_lesson) + ' пара')
                    msg += '\n' 

                    for j in range(0,len(a[i][1])):
                        if a[i][1][j] != ',' and a[i][1][j] !='':
                            msg += '\n'
                            msg += a[i][1][j]

                    msg += '\n'
        
        bot.send_message(message.from_user.id, text = msg,parse_mode = "Markdown")
    except:
        bot.send_message(message.from_user.id, "Не удалось загрузить расписание, попробуйте ввести другие данные о себе или попробуйте позже")


@bot.message_handler(commands=['schedule']) #показать актуальное расписание на эту неделю
def schedule_handler(message):
    #bot.send_message(message.from_user.id, 'Пожалуйста, подождите несколько секунд')
    i=0
    try:
        conn = sqlite3.connect("users_base.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT st_group FROM usersbase WHERE user_id = {message.chat.id} ;")
        group_res = cursor.fetchmany(1)[0][0]
        conn.commit()

        conn = sqlite3.connect("schedule_base.db")
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM schedbase WHERE st_group = ? ;",(group_res,))
        a = cursor.fetchmany(1)[0]
        cursor = conn.cursor()
        msg=('\n📎Расписание на '+num_of_this_week+' неделю📎')
        bot.send_message(message.from_user.id,text = msg, parse_mode = "Markdown")
        for num_of_day_of_week in range(2,8):
            msg=''
            msg += ('*'+days_of_week[num_of_day_of_week-1]+'*')

            for num_of_lesson in range(1,8):
                i+=1
                
                if a[i] != None and a[i] != '':
                    msg += ('\n' + str(num_of_lesson) + ' пара\n\n')
                    msg += str(a[i])
                    msg += '\n'

            bot.send_message(message.from_user.id, text = msg,parse_mode = "Markdown")
    
    except:
        bot.send_message(message.from_user.id, "Не удалось загрузить расписание, попробуйте ввести другие данные о себе или попробуйте позже")

@bot.message_handler(commands=['today']) #показать актуальное расписание на сегодня
def schedule_handler(message):
    i=0
    num_day_of_week = dt.now().weekday()+1
    try:
        conn = sqlite3.connect("users_base.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT st_group FROM usersbase WHERE user_id = {message.chat.id} ;")
        group_res = cursor.fetchmany(1)[0][0]
        conn.commit()

        conn = sqlite3.connect("schedule_base.db")
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM schedbase WHERE st_group = ? ;",(group_res,))
        a = cursor.fetchmany(1)[0]
        cursor = conn.cursor()

        msg=''
        msg += ('*'+str(days_of_week[num_day_of_week])+'*')
        i=(num_day_of_week-1)*7
        for num_of_lesson in range(1,8):
            i+=1
            if a[i] != None and a[i] != '':
                msg += ('\n' + str(num_of_lesson) + ' пара\n\n')
                msg += str(a[i])
                msg += '\n'

        bot.send_message(message.from_user.id, text = msg,parse_mode = "Markdown")
    
    except:
        bot.send_message(message.from_user.id, "Не удалось загрузить расписание, попробуйте ввести другие данные о себе или попробуйте позже")

@bot.message_handler(commands=['next_day']) #показать актуальное расписание на сегодня
def schedule_handler(message):
    i=0
    num_day_of_week = dt.now().weekday()+2
    try:
        if num_day_of_week==6:
            bot.send_message(message.from_user.id, "Завтра не учимся!")
        else:
            conn = sqlite3.connect("users_base.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT st_group FROM usersbase WHERE user_id = {message.chat.id} ;")
            group_res = cursor.fetchmany(1)[0][0]
            conn.commit()

            conn = sqlite3.connect("schedule_base.db")
            cursor = conn.cursor()
            
            cursor.execute(f"SELECT * FROM schedbase WHERE st_group = ? ;",(group_res,))
            a = cursor.fetchmany(1)[0]
            cursor = conn.cursor()

            msg=''
            msg += ('*'+str(days_of_week[num_day_of_week])+'*')
            i=(num_day_of_week-1)*7
            for num_of_lesson in range(1,8):
                i+=1
                if a[i] != None and a[i] != '':
                    msg += ('\n' + str(num_of_lesson) + ' пара\n\n')
                    msg += str(a[i])
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
