#keyugrinder.py
# Import necessary libraries
import pyautogui as p
import time as t
import keyboard as k
import ctypes

# Rename functions to make them more descriptive and user-friendly
sleep = p.sleep         # Pause the code for a specific amount of time
mouse_move = p.moveTo   # Move the mouse to specific screen coordinates
mouse_click = p.click   # Simulate a mouse click
key_down = p.keyDown    # Hold down a keyboard key
key_press = p.press     # Press and release a keyboard key
key_up = p.keyUp        # Release a keyboard key

# Define a function to click at a specific location
def click(x: int, y: int):
    """
    Moves the mouse to (x, y) on the screen and clicks.
    :param x: Horizontal position on the screen.
    :param y: Vertical position on the screen.
    """
    mouse_move(x, y)  # Move mouse to (x, y)
    mouse_click()  # Perform a click

# Define a function to perform a key combination
def keys(key_to_hold, key_to_press, seconds=0.1):
    """
    Holds down one key and presses another key.
    :param key_to_hold: The key to hold down (e.g., 'alt').
    :param key_to_press: The key to press while holding the other key (e.g., 'tab').
    :param seconds: How long to hold the key (in seconds).
    """
    key_down(key_to_hold)  # Hold down the first key
    sleep(seconds)  # Wait for a short time
    key_press(key_to_press)  # Press the second key
    sleep(seconds)  # Wait again
    key_up(key_to_hold)  # Release the first key

# Checks if caps lock is enabled on my computer or not
def is_caps_lock_on():
    # Query the state of Caps Lock using the GetKeyState function from user32.dll
    return bool(ctypes.WinDLL("user32").GetKeyState(0x14) & 0x0001)

def enable_caps():
    if not is_caps_lock_on():
        k.press_and_release('caps lock');
        return True
    else:
        return False
