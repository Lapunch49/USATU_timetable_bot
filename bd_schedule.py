import sqlite3

conn = sqlite3.connect("schedule_base.db")
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE schedbase
#                     (st_group, mon1, mon2, mon3, mon4, mon5, mon6, mon7, tue1, tue2, tue3, tue4, tue5, tue6, tue7, 
#                     wed1, wed2, wed3, wed4, wed5, wed6, wed7, thu1, thu2, thu3, thu4, thu5, thu6, thu7,
#                     fri1, fri2, fri3, fri4, fri5, fri6, fri7, sat1, sat2, sat3, sat4, sat5, sat6, sat7)
#                 """)



conn.commit()