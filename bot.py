import config
import telebot
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def parser_function():
    num_of_week = ''
    # num_of_lesson = 1 #1 пара
    # num_of_day_of_week = 2 #понедельник
    days_of_week = ['','ПН','ВТ','СР','ЧТ','ПТ','СБ']
    a = [''] * 26
    for i in range(26): 
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
        for num_of_lesson in range(1,5):
            i += 1
            a[i][0]=driver.find_elements_by_css_selector(f'#schedule > tbody:nth-child(2) > tr:nth-child({num_of_lesson}) > td:nth-child({num_of_day_of_week})')[0].text
            if a[i][0] != '':
                #print(num_of_lesson, 'пара')
                a[i][1] = a[i][0].split('\n')
                #print(a[i][1])
    
    #driver.close()

    return a, num_of_this_week

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
    str="Какие команды я умею выполнять:\n"
    str += "/start - дать боту информацию о себе\n"
    str += "/shedule - показать актуальное расписание на эту неделю\n"

    bot.send_message(message.from_user.id, str)

@bot.message_handler(commands=['shedule']) #показать актуальное расписание на эту неделю
def shedule_handler(message):
    bot.send_message(message.from_user.id, 'Пожалуйста, подождите несколько секунд')
    i=0
    days_of_week = ['','ПН','ВТ','СР','ЧТ','ПТ','СБ']
    a,num_of_this_week=parser_function()
    b=('\nРасписание на '+num_of_this_week+' неделю')
    bot.send_message(message.from_user.id, b)
    for num_of_day_of_week in range(2,8):
        b=''
        #bot.send_message(message.from_user.id, days_of_week[num_of_day_of_week-1])
        #print(days_of_week[num_of_day_of_week-1])
        b += ('*'+days_of_week[num_of_day_of_week-1]+'*')

        for num_of_lesson in range(1,5):
            i+=1
            if a[i][0] != '':
                #bot.send_message(message.from_user.id, num_of_lesson, 'пара')
                #print(num_of_lesson, 'пара')
                b += '\n' 
                b += (str(num_of_lesson) + ' пара')
                b += '\n' 

                for j in range(0,len(a[i][1])):
                    if a[i][1][j] != ',' and a[i][1][j] !='':
                        #bot.send_message(message.from_user.id, a[i][1][j])
                        #print(a[i][1][j])
                        b += '\n'
                        b += a[i][1][j]

                b += '\n'
    
        bot.send_message(message.from_user.id, b)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    try: 
        bot.send_message(message.chat.id,message.text)
    except: 
        pass

bot.polling()
