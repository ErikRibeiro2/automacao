from time import sleep
import pyautogui as py
import pyperclip


sleep(2)
print("Oi, ", end=' ')
sleep(2)
print("não se assusta", end=' ')
sleep(2)
print("kkkk")
sleep(2)

py.press("win")
sleep(1)
py.write('chroo', interval=0.4)
sleep(0.5)
py.press("enter")
sleep(3)
pyperclip.copy("https://i.ibb.co/M7RFwry/emillay.jpg")
sleep(1.5)
py.hotkey("ctrl", "v")
py.press("enter")
