import pyautogui
import time
import keyboard

screen_width, screen_height = pyautogui.size()

# Initialize the toggle state to False
toggle_state = False

while True:
    # Check if NUMPAD6 is pressed
    if keyboard.is_pressed('NUMPAD6'):
        # If the toggle state is currently False, set it to True
        if not toggle_state:
            toggle_state = True

        # Perform the action associated with NUMPAD6 (move the cursor to the middle of the screen and click)
        pyautogui.moveTo(screen_width / 2, screen_height / 2)
        pyautogui.click()
        time.sleep(1)

    # Check if NUMPAD3 is pressed
    elif keyboard.is_pressed('NUMPAD3'):
        # If the toggle state is currently False, set it to True
        if not toggle_state:
            toggle_state = True

        # Perform the action associated with NUMPAD3 (move the cursor 3 pixels to the left and right of the middle of the screen and click)
        pyautogui.moveTo(screen_width / 2 - 3, screen_height / 2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(screen_width / 2 + 3, screen_height / 2)
        pyautogui.click()
        time.sleep(1)

    # If neither key is pressed, check if the toggle state is True and set it to False if it is
    elif toggle_state:
        toggle_state = False