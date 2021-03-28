from pynput import keyboard
from pynput.keyboard import Key

class KeyCommand:

    def get_command(key):

        key_command = ""

        if key == Key.left:
            key_command = 'left 20'

        if key == Key.right:
            key_command = 'right 20'

        if key == Key.space:
            key_command = 'takeoff'

        if key == Key.enter:
            key_command = 'land'

        if key == keyboard.Key.esc:
            # Stop listener
            key_command = False

        return key_command























