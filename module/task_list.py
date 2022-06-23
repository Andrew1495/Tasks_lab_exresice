

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    unfished_tasks = []
    for task in tasks:     
        if task["completed"] == False:
            unfished_tasks.append(task)
    return unfished_tasks


## Get a list of completed tasks
def get_completed_tasks(list):
    completed_tasks = []
    for task in tasks:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    time_length_of_task = []
    for task in tasks:
        if task["time_taken"] >= time:
            time_length_of_task.append(task)
    return time_length_of_task

## Find a task with a given description
def get_task_with_description(list, description):
    for task in tasks:
        if task["description"] == description:
            return task

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    if status == True:
        completed_task = get_completed_tasks(list)
        return completed_task
    else:
        uncompleted_task = get_uncompleted_tasks(list)
        return uncompleted_task



def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)
