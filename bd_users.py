import sqlite3

def users_bd_function(id):
    conn = sqlite3.connect("users_base.db ")
    cursor = conn.cursor()

    
    cursor.execute(f"SELECT * FROM usersbase WHERE user_id = {id} ;")
    being_res = cursor.fetchmany(1)
    if being_res[0][0]!='':
        cursor.execute("""INSERT INTO usersbase(user_id) VALUES(?);""",(id,))

    conn.commit()





def users_bd_f_faculty(id,faculty):
    conn = sqlite3.connect("users_base.db ")
    cursor = conn.cursor()

    #cursor.execute("""INSERT INTO usersbase(faculty) WHERE USER_ID=? VALUES(faculty);""",(id))
    cursor.execute("UPDATE usersbase SET faculty=? WHERE user_id=?;", (id,faculty))
    conn.commit()

users_bd_function('122345563')




#создание базы данных - запустить 1 раз вначале

# import sqlite3
# conn = sqlite3.connect("users_base.db")
# cursor = conn.cursor()

# cursor.execute("""CREATE TABLE usersbase
#                     (user_id, faculty, course, st_group, consent)
#                 """)

# conn.commit()
