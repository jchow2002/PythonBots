import pyautogui
import time

text = "Chupapi Munyanyo"
flag = True
count = 5
for x in range(50):
    pyautogui.typewrite(text)
    pyautogui.press("enter")
