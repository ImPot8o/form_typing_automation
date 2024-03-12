#  dev.pot8o
#  V1.0
#  3/11/24

import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time
import threading
import customtkinter as ctk

pyautogui.FAILSAFE = False
is_running = False
typing_thread = None
paused = False
current_line_index = 0
typing_position = None
found_typing_position = False
click_every_time = False


def read_file_and_type(filename, cooldown):
    global is_running, paused, current_line_index, found_typing_position
    is_running = True
    launch_button.config(text="Stop")
    pause_button.pack()  # Show the pause button
    with open(filename, 'r', encoding='utf-8', errors='replace') as file:
        lines = file.readlines()
        while current_line_index < len(lines):
            if not is_running:
                break
            if not paused:
                if found_typing_position and typing_position:
                    pyautogui.click(typing_position[0], typing_position[1])  # Move mouse to typing position
                if not click_every_time:
                    found_typing_position = False
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete')
                line = lines[current_line_index]
                pyautogui.typewrite(line.strip())
                pyautogui.press('enter')
                current_line_index += 1
            time.sleep(cooldown)
    is_running = False
    launch_button.config(text="Launch")
    pause_button.pack_forget()  # Hide the pause button


def launch_typing_process():
    global typing_thread, is_running
    if not is_running:
        filename = file_path_var.get()
        cooldown = float(cooldown_entry.get())
        typing_thread = threading.Thread(target=read_file_and_type, args=(filename, cooldown))
        typing_thread.start()
        launch_button.config(text="Stop")
        check_process_status()
    else:
        stop_typing()


def pause_typing():
    global paused, found_typing_position
    paused = True
    pause_button.config(text="Resume", command=resume_typing)


def resume_typing():
    global paused, found_typing_position
    found_typing_position = True
    paused = False
    pause_button.config(text="Pause", command=pause_typing)


def stop_typing():
    global is_running, found_typing_position
    is_running = False
    found_typing_position = True
    launch_button.config(text="Launch")
    result = messagebox.askyesno("Done testing?", "Do you want to close window?")
    if result:
        root.destroy()


def check_process_status():
    global typing_thread
    while typing_thread.is_alive():
        root.update()
        time.sleep(0.1)


def select_file():
    filename = filedialog.askopenfilename(initialdir="C:/Downloads", title="Select a Text File",
                                          filetypes=(("Text files", "*.txt"),))
    file_path_var.set(filename)


def dark_screen():
    root.withdraw()  # Hide the root window temporarily
    img = pyautogui.screenshot()  # Capture the screen
    overlay = tk.Toplevel(root)  # Create a top-level window for the overlay
    overlay.attributes("-fullscreen", True)  # Make the overlay cover the entire screen
    overlay.attributes("-topmost", True)  # Ensure the overlay stays on top
    overlay.configure(bg="black")  # Set the background color to black
    overlay.attributes("-alpha", 0.75)  # Set the transparency level
    overlay.bind("<Button-1>", lambda event: get_click_position(event, overlay))


def get_click_position(event, overlay):
    global typing_position, found_typing_position
    x, y = event.x_root, event.y_root  # Get the mouse click position
    typing_position = (x, y)  # Save the typing position
    found_typing_position = True
    overlay.destroy()  # Destroy the overlay window
    root.deiconify()  # Restore the root window
    node_button.config(text="Position Set", command=dark_screen, bg='#242424')


def toggle_click_every_time():  # Step 2: Create a function to toggle click_every_time variable
    global click_every_time
    click_every_time = not click_every_time


root = ctk.CTk()
root.title("Form Typing Automation")
root.attributes("-topmost", True)
root.iconbitmap('images.ico')

file_path_var = tk.StringVar()

file_label = tk.Label(root, text="Select a Text File:", fg='white', bg='#242424')
file_label.pack()

file_entry = tk.Entry(root, textvariable=file_path_var, width=50, bg='#363636', fg='white')
file_entry.pack()

select_button = tk.Button(root, text="Browse", command=select_file, bg='#363636', fg='white')
select_button.pack()

cooldown_label = tk.Label(root, text="Cooldown between submits (seconds):", fg='white', bg='#242424')
cooldown_label.pack()

cooldown_entry = tk.Entry(root, bg='#363636', fg='white')
cooldown_entry.pack()

launch_button = tk.Button(root, text="Launch", command=launch_typing_process, bg='#363636', fg='white')
launch_button.pack(pady=5)

pause_button = tk.Button(root, text="Pause", command=pause_typing, bg='#363636', fg='white')
node_button = tk.Button(root, text="Select Typing Position", command=dark_screen, bg='#363636', fg='white')
node_button.pack()

on = tk.PhotoImage(file="on.png")
off = tk.PhotoImage(file="off.png")


def switch():
    global click_every_time
    # Determine is on or off
    if click_every_time:
        on_button.config(image=off)
        click_every_time = False
    else:
        on_button.config(image=on)
        click_every_time = True


on_button = tk.Button(root, image=off, bd=0,
                      command=switch, bg='#242424', activebackground='#242424', activeforeground='white')
on_button.pack()
check_label = tk.Label(root, text='Click typing position every submit', bg='#242424', fg='white')
check_label.pack()

root.mainloop()
