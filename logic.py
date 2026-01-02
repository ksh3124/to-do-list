def add_tasks(tasks,task_name):
    if task_name in tasks:
        return False
    else:
        tasks[task_name] = False
        return True

def view_task(tasks):
    if not tasks:
        return None
    else:
        return [(task, status) for task, status in tasks.items()]

def edit_tasks(tasks,task_name,new_status):
    if task_name in tasks:
        tasks[task_name] = new_status
        return True
    else:
        return False

def delete_tasks(tasks,task_name):
    if task_name in tasks:
        del tasks[task_name]
        return True
    else:
        return False
