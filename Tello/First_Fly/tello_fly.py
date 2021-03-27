from tello import Tello
from datetime import datetime
import time

start_time = str(datetime.now().strftime('%d%m%Y%H%M%S'))
print("Time: " + start_time)


file_name: str = './command.txt'

print(file_name)
f = open(file_name, "r")
commands = f.readlines()


tello = Tello()
for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()

        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print ('delay %s' % sec)
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)

log = tello.get_log()

out = open('log/log_' + start_time + '.txt', 'x')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)
