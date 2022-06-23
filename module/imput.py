def ask_selection_option():
    option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    return option

def ask_task_desciption():
    description = input("Enter task description to search for: ")
    return description

def ask_duration():
    time = int(input("Enter task duration: "))
    return time

# description = input("Enter task description to search for: ")
def ask_for_description():
    description = input("Enter description: ")
    return description

def ask_time():
    time_taken = int(input("Enter time taken: "))
    return time_taken