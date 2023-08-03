import sqlite3

class Database:
    def __init__(self):
            # Connect to the database
            self.conn = sqlite3.connect('./db/task.db') 
            self.cursor = self.conn.cursor()


    def initialize_database(self):
            # Create the tasks table if it doesn't exist
            self.cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    description TEXT,
                    completed INTEGER
                )
                '''
            )
            
            self.conn.commit()
   