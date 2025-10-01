import json
import datetime
import os 
from tabulate import tabulate

# first let create a json file or if it is already created we use it 
TASKS_FILE = "tasks.json" #this is where our JSON task file will be stored 

#first load task file if it exists 
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE,"r") as file:
            try:
                return json.load(file) #return a Python list 
            except json.JSONDecodeError:
                return [] 
    return [] # else return an empty list 

#here we write the list of tasks into the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE,"w") as file:
        json.dump(tasks,file,indent=4)

#adding the task information that will be displayed in a table format using the tabulate foramt:
def tabulate_task(tasks_list):
    columns = ["ID","Task","Status","Created At","Updated At"] # the columns heading 
    rows = [] # a list of empty rows where the task information will be stored
    for task in tasks_list: # for each task that will be inputted by the user this is how it be stored in the row
        rows.append([
            task["id"], 
            task["description"], 
            task["status"], 
            task["createdAt"], 
            task["updatedAt"]
        ])
    return tabulate(rows, headers=columns,tablefmt="grid", maxcolwidths=[None,25,None,None,None]) # neater table look 

#automatically creating ID's for each task by looking is there already a task in there if not then the first task gets 1 else previous_task_id + 1 = new_task_id
#if there are any task in the list then we just do +1 of the previous task id else we just start from 1 
def create_id(tasks):
    max_id = 0 #our current id is 0 
    for task in tasks: #for each task in the tasks file or tasks wthat is added
        if task["id"] > max_id: # we check if the id is 0 or there is already something in there then we create the next id 
            max_id = task["id"] #now the final/max id will be the current task_id 
    new_id=max_id+1 #create the next id by doing + 1
    return new_id # we always return the new_id so that it will be stored in the table 

'''
Logic follows: for each command:
We load our JSON
Check the ID or create the new ID 
Add, delete the ID
Update our task 
Save the task 
Either return new added task or print the list based on the applied filter
'''

# now after we calculate the new_id, we we want to create the new_dictionary with all the required positions
def add_task(description):
    tasks = load_tasks() #check if the file exists if it does, append the new task in there else, create file 
    new_id = create_id(tasks)
    new_task = {
        "id": new_id,
        "description": description,
        "status": "Todo",
        "createdAt": str(datetime.date.today()),
        "updatedAt": str(datetime.date.today())
    }
    tasks.append(new_task) # add the new task into the tasks list
    save_tasks(tasks) #remember to save the task
    return tabulate_task([new_task]) # produce the table format of the dictionary

#now let's work on the update logic statment 

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description 
            task["updatedAt"] = str(datetime.date.today())
            save_tasks(tasks)
            return tabulate_task([task])
    print("Task not found")

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "In-Progress"
            task["updatedAt"] = str(datetime.date.today())
            save_tasks(tasks)
            return tabulate_task([task])
    print("Task not found")

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Done"
            task["updatedAt"] =str(datetime.date.today())
            save_tasks(tasks)
            return tabulate_task([task])
    print("Task not found")

def delete_task(task_id):
    tasks = load_tasks()
    if len(tasks) == 0:
        return "Empty task list nothing to delete"
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task) #we want to remove the task dictionary from the list 
            save_tasks(tasks)
            if tasks:
                return f"Task {task_id} has been removed.\n" + tabulate_task(tasks)
            else:
                return f"Task {task_id} has been removed. No tasks left."
    return "Please check the task Id again"

''' 
In the list function we want to filter based on different requirements or not. 
If filter then we create a new empty list that stores the filtered task and return it to us else just return the entire list
For the date/year filter we use the datetime module and I used strptime which takes in a string and format it to the datetime object
Handling errors incase the user types invalid dates.
'''

def list_tasks(status=None, created=None, updated=None):
    tasks = load_tasks()
    filtered_task = []

    created_filter = None
    if created:
        try:
            # Try the full date for filtering
            datetime.datetime.strptime(created, "%Y-%m-%d")
            created_filter = created
        except ValueError:
            try:
                # Only year filter
                datetime.datetime.strptime(created, "%Y")
                created_filter = created[:4]  # first 4 chars = year
            except ValueError:
                print("Invalid --created date format. Use YYYY or YYYY-MM-DD, thank you")
                return
            
    updated_filter = None
    if updated:
        try:
            datetime.datetime.strptime(updated, "%Y-%m-%d")
            updated_filter = updated
        except ValueError:
            try:
                datetime.datetime.strptime(updated, "%Y")
                updated_filter = updated[:4]
            except ValueError:
                print("Invalid --updated date format. Use YYYY or YYYY-MM-DD, thank you")
                return

    for task in tasks:
        match = False
        if status and task["status"] == status:
            match = True
        if created_filter:
            # Compare full date or year
            if len(created_filter) == 4 and task["createdAt"][:4] == created_filter: #year check
                match = True
            elif task["createdAt"] == created_filter: #full date check
                match = True
        if updated_filter:
            if len(updated_filter) == 4 and task["updatedAt"][:4] == updated_filter:
                match = True
            elif task["updatedAt"] == updated_filter:
                match = True

        if match:
            filtered_task.append(task)
    #if filtered task is true then return the filtered table else just return the full list
    if filtered_task:
        return tabulate_task(filtered_task)
    else:
        return tabulate_task(tasks)

          