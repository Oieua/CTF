import pyautogui
import pyperclip
import math
import time


#Find position of the cursor (x and y coordinates)
#while True:
#	print(pyautogui.position())

pyautogui.click(456,1057) #Position of the chat bar on the sceen
pyautogui.typewrite("!ep1")
pyautogui.typewrite(["enter"])
time.sleep(0.5)
pyautogui.doubleClick(375,359) #Position of the received text (n1) on the sceen
pyautogui.hotkey('ctrl','c')
root = int(pyperclip.paste())
root = math.sqrt(root)
pyautogui.doubleClick(420,357) #Position of the received text (n2) on the sceen
pyautogui.hotkey('ctrl','c')
multiply = int(pyperclip.paste())
value = root * multiply
answer = str(round(value, 2))
pyautogui.click(456,1057)
answer = "!ep1 -rep " + str(answer)
pyautogui.typewrite(answer)
pyautogui.typewrite(["enter"])
