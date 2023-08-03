import src.database as db_module
import src.todo_manager as manager_module

def main():
    try:
        db = db_module.Database()
        db.initialize_database()
        
        todo_manager = manager_module.TodoManager(db)
    
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
                todo_manager.add_task(description)
            elif choice == '2':
                task_id = int(input('Enter task ID: '))
                description = input ('Enter new task description: ')
                todo_manager.update_task(task_id, description)
            elif choice == '3':
                task_id = int(input('Enter task ID: '))
                todo_manager.mark_task(task_id)
            elif choice == '4':
                task_id = int(input('Enter task ID: '))
                todo_manager.delete_task(task_id)
            elif choice == '5':
                todo_manager.display_tasks()
            elif choice == '6':
                break
            
        db.conn.close()
        
    except Exception as error:
        print(f'Error: {error}')

if __name__ == '__main__':
    main()