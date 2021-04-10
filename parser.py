from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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

#num_of_week = driver.find_element_by_class_name('div.row:nth-child(3) > p:nth-child(4) > font:nth-child(1)').text

name_of_faculty = Select(driver.find_element_by_id('id_faculty'))
name_of_faculty.select_by_visible_text('ФИРТ')

#name_of_faculty = Select(driver.find_element_by_id('id_faculty').text)
#name_of_faculty.select_by_value('ФИРТ')

num_of_course = Select(driver.find_element_by_id('id_klass'))
num_of_course.select_by_value('1')

name_of_group = Select(driver.find_element_by_id('id_group'))
name_of_group.select_by_visible_text('ПРО-127Б')

# name_of_group = Select(driver.find_element_by_id('id_group'))
# name_of_group.select_by_value('3717')

driver.find_element_by_css_selector('.centered-horizontal > div:nth-child(1) > input:nth-child(1)').click()

#######

num_of_this_week = driver.find_elements_by_css_selector('div.row:nth-child(3) > p:nth-child(4) > font:nth-child(1)')[0].text

# print(num_of_this_week)



for num_of_day_of_week in range(2,8):
    #print('\n\n\n',days_of_week[num_of_day_of_week-1])
    for num_of_lesson in range(1,5):
        i += 1
        a[i][0]=driver.find_elements_by_css_selector(f'#schedule > tbody:nth-child(2) > tr:nth-child({num_of_lesson}) > td:nth-child({num_of_day_of_week})')[0].text
        if a[i][0] != '':
            #print(num_of_lesson, 'пара')
            a[i][1] = a[i][0].split('\n')
            #print(a[i][1])

i=0

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

# print(a3)
#driver.close()