import sqlite3

# try:
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
# except sqlite3.DatadaseError:
#     print('ДА ИДИ НАХУЙ')
# finally:
#     connection.close
with sqlite3.connect('data.db') as connection:
    cursor = connection.cursor()
    command = '''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY 
     )
'''