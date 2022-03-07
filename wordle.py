from pynput import keyboard
import os
import keyboard as kb

while True:
    apple = kb.read_key()
    if kb.read_key() != False:
        print("You pressed " + apple)
        break

while True:
    if kb.is_pressed("q"):
        print("You pressed q")
        break
        


"""
def on_press(key):
    try:
        print('{0}'.format(key.char), end="")
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

os.system("cls")
"""