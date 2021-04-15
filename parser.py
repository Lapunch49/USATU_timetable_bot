import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import sqlite3

# conn = sqlite3.connect("schedule_base.db")
# cursor = conn.cursor()
#conn.commit()
faculty = 'ФИРТ'
course = 1
group = 'ПРО-127Б'

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

parser_for_bd(faculty, course, group)
