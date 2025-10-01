import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def run_task_tracker():
    # Get the command from the entry widget
    user_command = command_entry.get().strip()  # example: add Finish Homework
    if not user_command:
        return

    # Split the command into a list for subprocess
    args = ["python", "taskpad.py"] + user_command.split()

    # Clear the text area
    text_area.delete(1.0, tk.END)

    # Run the subprocess
    process = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8'
    )

    for line in process.stdout:
        text_area.insert(tk.END, line)
        text_area.see(tk.END)

    process.wait()


# Create GUI
root = tk.Tk()
root.title("TaskPad")
root.geometry("900x600")  # starting window size

# Load the background image
original_bg = Image.open("flower1.jpg")
bg_image = ImageTk.PhotoImage(original_bg)

# Create a canvas to hold background and widgets
canvas = tk.Canvas(root, width=900, height=600)
canvas.pack(fill="both", expand=True)

# Set the background image
bg_id = canvas.create_image(0, 0, anchor="nw", image=bg_image)

# Create widgets on the canvas
command_entry = tk.Entry(root, width=80)
text_area = tk.Text(root, height=20, width=80)
run_button = tk.Button(root, text="Run TaskPad", command=run_task_tracker)

# Add widgets to canvas
entry_window = canvas.create_window(450, 30, window=command_entry) 
text_window = canvas.create_window(450, 300, window=text_area)      
button_window = canvas.create_window(450, 550, window=run_button)    

# Make the background resizable
def resize_bg(event):
    new_width = event.width
    new_height = event.height
    resized = original_bg.resize((new_width, new_height), Image.ANTIALIAS)
    new_bg = ImageTk.PhotoImage(resized)
    canvas.itemconfig(bg_id, image=new_bg)
    canvas.image = new_bg  # keep reference

canvas.bind("<Configure>", resize_bg)

# Placeholder text
command_entry.insert(0, "Type your command here, e.g., 'add Finish Homework'")

root.mainloop()






