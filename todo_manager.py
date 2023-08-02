import sqlite3

try:
    # Connect to the database
    conn = sqlite3.connect('task.db')
    cursor = conn.cursor()

    # Create the tasks table if it doesn't exist
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            description TEXT,
            completed INTEGER
        )
        '''
    )

    conn.commit()
    
except sqlite3.Error as error:
    print('Error handler - ', error)
    
# finally:
#     if conn:
#         conn.close()
#         print('SQLite connection closed')