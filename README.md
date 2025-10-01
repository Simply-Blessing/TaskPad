🌸 TaskPad

A minimal, cute, and practical way to track tasks right from your terminal.

📖 What is TaskPad?

TaskPad is a command-line productivity buddy that helps you keep track of tasks without the clutter.
Whether you want to jot down a quick reminder, manage your daily work, or just have a to-do list that actually feels simple, TaskPad has you covered.

It’s clean, lightweight, and all your tasks live in a simple JSON file.

✨ Features 

🌟 Add Tasks → Write down tasks quickly without quotes or fuss.

🖊 Update Tasks → Edit descriptions anytime.

⏳ In-Progress → Track what you’re currently working on.

✅ Done → Celebrate finished work.

🗑 Delete → Remove tasks you don’t need anymore.

📋 List Everything → Show tasks in a neat table, or filter by:

Status → Todo, In-Progress, Done

Created / Updated Date → Filter by YYYY or exact YYYY-MM-DD

🗂 How It’s Built

TaskPad is split into a few simple files:

taskpad.py → The CLI (where you type your commands).

taskpad_func.py → The engine that powers everything:

Loading & saving tasks

Adding, updating, marking done/in-progress

Deleting and filtering tasks

test_taskpad.py → Unit tests powered by pytest 🧪

taskpad_widget.py → A small GUI window to run TaskPad if you don’t want to stay in the terminal.

⚙️ Installation

Install TaskPad directly from GitHub:

pip install git+https://github.com/simply-blessing/taskpad.git


Or clone the repo manually:

git clone https://github.com/simply-blessing/taskpad.git
cd taskpad

🚀 Usage 

Add a task:
$ python taskpad.py add Finish homework

Update a task:
$ python taskpad.py upadte 1 Finish Molecular Biology Report

Mark as in progress:
$ python taskpad.py mark-in-progress 1 

Mark as done:
$ python taskpad.py mark-done 1 

Delete a task
$ python taskpad.py delete 1 

List tasks:
$ python taskpad.py list 

List with filters applied:
$python taskpad.py list -s/--status Done 
$python taskpad.py list -c/--created 2025 
$python taskpad.py list -u/--updated 2025-09-30

🧪 Testing
pytest test_taskpad.py 




