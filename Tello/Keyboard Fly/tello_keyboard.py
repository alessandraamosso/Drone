from tello import Tello
from keyCommand import KeyCommand
from pynput import keyboard
from pynput.keyboard import Key
from datetime import datetime


def on_keypress(key):
    command = KeyCommand.get_command(key)

    if command != False or "":
        print("Key: ")
        tello.send_command(command)


start_time = str(datetime.now().strftime('%d%m%Y%H%M%S'))
print("Time: " + start_time)


tello = Tello()
tello.send_command('command')

with keyboard.Listener(
        on_press=on_keypress) as listener:
    listener.join()

listener.start()

log = tello.get_log()

out = open('log/log_' + start_time + '.txt', 'x')
for stat in log:
    stat.print_stats()
    out_str = stat.return_stats()
    out.write(out_str)
