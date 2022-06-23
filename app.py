
from module.task_list import *
from module.output import *
from data.task_list import *
from module.imput import *


while (True):
    print_menu()
    option = ask_selection_option()
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = ask_task_desciption()
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        time = ask_duration()
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == '6':
        ask_for_description
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = ask_for_description()
        time_taken = ask_time()
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")
