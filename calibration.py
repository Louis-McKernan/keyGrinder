#calibration.py
import ctypes
import pyautogui
import keyboard
import time

def is_caps_lock_on():
    # Check Caps Lock state using the Windows API
    return bool(ctypes.WinDLL("user32").GetKeyState(0x14) & 0x0001)

def enable_caps_lock():
    if not is_caps_lock_on():  # If Caps Lock is off
        keyboard.press_and_release('caps lock')  # Toggle Caps Lock to enable it

if __name__ == "__main__":
    print("Ensuring Caps Lock is enabled...")
    enable_caps_lock()  # Enable Caps Lock if it's not already on

    if is_caps_lock_on():
        print("Caps Lock is ON. Script running...")
    else:
        print("Failed to enable Caps Lock. Exiting...")
        exit()

    try:
        while is_caps_lock_on():  # Run the loop while Caps Lock is ON
            x, y = pyautogui.position()
            print(f"Mouse Position: X={x}, Y={y}", end="\r")  # Overwrites the same line
            time.sleep(0.1)  # Add a small delay to reduce CPU usage
        print("\nCaps Lock is OFF. Exiting script.")
    except KeyboardInterrupt:
        print("\nProgram stopped manually.")
