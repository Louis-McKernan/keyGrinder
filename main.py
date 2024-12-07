#main.py
# Import all the functions from KeyGrinder
from keyGrinder import click, keys, sleep, is_caps_lock_on, enable_caps

def automation_loop():    
    bool_caps_enabled = enable_caps()
    while bool_caps_enabled:
        automation_sequence
        bool_caps_enabled = is_caps_lock_on()
        print("Ran Sequence.")
        sleep(0.1)
    print("Ended Program")



#---------START: Main Automation Code :START---------
def automation_sequence():

    # Click at screen coordinates (300, 300)
    click(300,300)

    # Wait for 3 seconds
    sleep(3.0)

    # Open the "File" menu using Alt + O
    keys('alt', 'o')

    # Wait for 0.2 seconds
    sleep(0.2)

    # Redo an action using Ctrl + Y
    keys('ctrl', 'y')

    # Wait for 1 second
    sleep(0.2)

    # Click at screen coordinates (800, 100)
    click(800, 100)
#---------END: Main Automation Code :END---------



#This runs the code; no need to modify this portion below.
if __name__ == "__main__":
    # Switch to the next window using Alt + Tab
    keys('alt', 'tab')
    
    # Wait for 0.1 seconds
    sleep(0.1)

    #Run Sequence Above    
    automation_loop()
