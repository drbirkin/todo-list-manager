import sqlite3

class Database:
    def __init__(self):
        # try:
            # Connect to the database
            self.conn = sqlite3.connect('./db/task.db') 
            self.cursor = self.conn.cursor()
        # except:
        #     raise sqlite3.Error

    def initialize_database(self):
        try:       
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
        except:
            raise sqlite3.Error