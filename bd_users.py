# import sqlite3

# conn = sqlite3.connect("mydatabase.db ")
# cursor = conn.cursor()

# #Создание таблицы albums
# cursor.execute("""CREATE TABLE usersbase
#                  (user_id, faculty, course,
#                   group, line_for_shedule)
#                 """)

# cursor.execute("""INSERT INTO usersbase(user_id, faculty) VALUES('Kate','ФИРТ');""")

# conn.commit() #завершение соединения с бд