# import sqlite3

# conn = sqlite3.connect("schedule_base.db")
# cursor = conn.cursor()

# # cursor.execute("""CREATE TABLE schedbase
# #                     (st_group, mon1, mon2, mon3, mon4, mon5, mon6, mon7, tue1, tue2, tue3, tue4, tue5, tue6, tue7, 
# #                     wed1, wed2, wed3, wed4, wed5, wed6, wed7, thu1, thu2, thu3, thu4, thu5, thu6, thu7,
# #                     fri1, fri2, fri3, fri4, fri5, fri6, fri7, sat1, sat2, sat3, sat4, sat5, sat5, sat6, sat7)
# #                 """)

# cursor.execute("""CREATE TABLE schedbase(st_group, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42)""")

# conn.commit()