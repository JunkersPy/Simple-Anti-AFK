import pyautogui
import tkinter as tk
from threading import Thread

def move_and_click_center():
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width / 2, screen_height / 2)
    pyautogui.click()

def move_and_click_leftright():
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width / 2 - 3, screen_height / 2)
    pyautogui.click()
    pyautogui.moveTo(screen_width / 2 + 3, screen_height / 2)
    pyautogui.click()

def start_action(func):
    if toggle_state.get():
        action_thread = Thread(target=func)
        action_thread.start()

root = tk.Tk()
root.title("PyAutoGUI Controller")

toggle_state = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Enable", variable=toggle_state).pack()
tk.Button(root, text="Move & Click at Center", command=lambda: start_action(move_and_click_center)).pack()
tk.Button(root, text="Move & Click Left-Right", command=lambda: start_action(move_and_click_leftright)).pack()

root.mainloop()
