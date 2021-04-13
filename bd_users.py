import sqlite3

# def users_bd_function(id):
#     conn = sqlite3.connect("users_base.db ")
#     cursor = conn.cursor()

#     #Создание таблицы albums
#     cursor.execute("""INSERT INTO usersbase(user_id)
# #     VALUES(id);""")

# cursor.execute("""INSERT INTO users(users)
#     VALUES('Katerrr');""")

# conn.commit()

conn = sqlite3.connect("users_base.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE usersbase
                    (user_id, faculty, course, st_group, consent)
                """)

conn.commit()




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















#создание базы данных - запустить 1 раз вначале
# import sqlite3

# conn = sqlite3.connect("users_base.db ")
# cursor = conn.cursor()

# cursor.execute("""CREATE TABLE usersbase
#                     (user_id, faculty, course, st_group)
#                     """)

# conn.commit()