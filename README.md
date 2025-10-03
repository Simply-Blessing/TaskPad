## 🌸 TaskPad

A minimal, cute, and practical way to track tasks right from your terminal.

---

## 📖 What is TaskPad?

TaskPad is a command-line productivity buddy that helps you keep track of tasks without the clutter.
Whether you want to jot down a quick reminder, manage your daily work, or just have a to-do list that actually feels simple, TaskPad has you covered.
It’s clean, lightweight, and all your tasks live in a simple JSON file.

---

## ✨ Features 

🌟 add Tasks → Write down tasks quickly without quotes or fuss.

🖊 update Tasks → Edit descriptions anytime.

⏳ mark-in-progress → Track what you’re currently working on.

✅ mark-done → Celebrate finished work.

🗑 delete → Remove tasks you don’t need anymore.

📋 list Everything → Show tasks in a neat table, or filter by:
  * status → todo, in-progress, done
  * created / updated Date → Filter by YYYY or exact YYYY-MM-DD

---

## 🗂 How It’s Built

TaskPad is split into a few simple files:

* taskpad.py → The CLI (where you type your commands).
* taskpad_func.py → The engine that powers everything:
  * Loading & saving tasks
  * Adding, updating, marking done/in-progress
  * Deleting and filtering tasks
* test_taskpad.py → Unit tests powered by pytest 🧪
* taskpad_widget.py → A small GUI window to run TaskPad if you don’t want to stay in the terminal.

---

## ⚙️ Installation

Install TaskPad directly from GitHub:
```bash
pip install git+https://github.com/simply-blessing/taskpad.git
```
Or clone the repo manually:
```bash
git clone https://github.com/simply-blessing/taskpad.git
cd taskpad
```

---

## 🚀 Usage 

Add a task:
```bash
python taskpad.py add Finish homework
```
Update a task:
```bash
python taskpad.py update 1 Finish Molecular Biology Report
```
Mark as in progress:
```bash
python taskpad.py mark-in-progress 1 
```
Mark as done:
```bash
python taskpad.py mark-done 1 
```
Delete a task:
```bash
python taskpad.py delete 1 
```
List tasks:
```bash
python taskpad.py list 
```
List with filters applied:
```bash
python taskpad.py list -s/--status done 
python taskpad.py list -c/--created 2025 
python taskpad.py list -u/--updated 2025-09-30
```

---

## 🧪 Testing
```bash
pytest test_taskpad.py 
```

---

## Project URL
https://roadmap.sh/projects/task-tracker

