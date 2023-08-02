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

def add_task (description):
    cursor.execute('INSERT INTO tasks (description, completed) VALUES (?, 0)', (description,))
    conn.commit()
    
def update_task (task_id, description):
    cursor.execute('UPDATE tasks SET description = ? WHERE id = ?', (description, task_id))
    conn.commit()
    
def mark_task (task_id):
    cursor.execute('SELECT completed FROM tasks WHERE id = ?', (task_id,))
    output = cursor.fetchone()
    cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (0 if output[0] else 1, task_id))
    
def delete_task (task_id):
    cursor.execute('DELETE FROM tasks WHERE id = ?', {task_id})
    conn.commit()
    
def display_tasks ():
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    for task in tasks:
        print(f'{task[0]}. [{task[2] and "X" or " "}] {task[1]}')
    
if __name__ == '__main__':
    while True:
        print('Todo List Manager')
        print('1. Add Task')
        print('2. Update Task')
        print('3. Complete Task')
        print('4. Delete Task')
        print('5. List Tasks')
        print('6. Exit')
        
        choice = input('Select an option: ')
        
        if choice == '1':
            description = input ('Enter task description: ')
            add_task(description)
        elif choice == '2':
            task_id = int(input('Enter task ID: '))
            description = input ('Enter new task description: ')
            update_task(task_id, description)
        elif choice == '3':
            task_id = int(input('Enter task ID: '))
            mark_task(task_id)
        elif choice == '4':
            task_id = int(input('Enter task ID: '))
            delete_task(task_id)
        elif choice == '5':
            display_tasks()
        elif choice == '6':
            break
        
    conn.close()
            
