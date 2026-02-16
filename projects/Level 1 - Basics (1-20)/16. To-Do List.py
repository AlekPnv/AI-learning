def display_tasks(task_list: list):
    print("----- TASKS -----")
    if not task_list:
        print("No tasks yet")
    else:
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")
    print()

def add_task(task: str, task_list: list):
    task_list.append(task)

def remove_task(task_index: int, task_list: list):
    task_list.pop(task_index - 1)

def main():
    tasks = []
    
    while True:
        print("------- MENU -------")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        try:
            choice = int(input("\nChoose an option [1-4]: "))
        except ValueError:
            print("\nInvalid Input! Try again with a number\n")
            continue
        
        if choice in range(1,5):
            if choice == 1:
                display_tasks(tasks)
                
            elif choice == 2:
                while True:
                    user_task = input("Task: ")
                    if len(user_task) == 0 or user_task.isspace():
                        print("\nTask can't be empty")
                        continue
                    else:
                        add_task(user_task, tasks)
                        break
                
            elif choice == 3:
                display_tasks(tasks)
                if tasks:
                    while True:
                        try:
                            user_task = int(input(f"Remove Task [1-{len(tasks)}]: "))
                        except ValueError:
                            print("Try again with a number\n")
                            continue
                        
                        if user_task not in range(1, len(tasks) + 1):
                            print("Try again with a given number\n")
                            continue
                        else:
                            removed_task = tasks[user_task - 1]
                            remove_task(user_task, tasks)
                            print(f"{removed_task} was removed\n")
                            break
                else:
                    print("No tasks to remove\n")
            
            elif choice == 4:
                print("Exiting...")
                break
        
        else:
            print("Try again with a given number\n")
            continue


if __name__ == "__main__":
    main()