class TodoManager:
    def __init__ (self, db):
        self.db = db
        
    def add_task (self, description):
        self.db.cursor.execute('INSERT INTO tasks (description, completed) VALUES (?, 0)', (description,))
        self.db.conn.commit()
        
    def update_task (self, task_id, description):
        self.db.cursor.execute('UPDATE tasks SET description = ? WHERE id = ?', (description, task_id))
        self.db.conn.commit()
        
    def mark_task (self, task_id):
        self.db.cursor.execute('SELECT completed FROM tasks WHERE id = ?', (task_id,))
        output = self.db.cursor.fetchone()
        self.db.cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (0 if output[0] else 1, task_id))
        self.db.conn.commit()
        
    def delete_task (self, task_id):
        self.db.cursor.execute('DELETE FROM tasks WHERE id = ?', {task_id})
        self.db.conn.commit()
        
    def display_tasks (self):
        self.db.cursor.execute('SELECT * FROM tasks')
        tasks = self.db.cursor.fetchall()
        for task in tasks:
            print(f'{task[0]}. [{task[2] and "X" or " "}] {task[1]}')
        
