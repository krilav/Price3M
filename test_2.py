import os
import sqlite3


path_db_users = f'..{os.sep}Price3M{os.sep}db{os.sep}price3m.db'
conn = sqlite3.connect(path_db_users)
cursor = conn.cursor()
cursor.execute("SELECT count_request FROM users where id=415061327")
users_id = cursor.fetchall()

print(users_id)