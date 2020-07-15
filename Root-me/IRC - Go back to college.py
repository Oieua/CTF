import pyautogui
import pyperclip
import math
import time

pyautogui.click(456,1057)
pyautogui.typewrite("!ep1")
pyautogui.typewrite(["enter"])
time.sleep(0.5)
pyautogui.doubleClick(375,359)
pyautogui.hotkey('ctrl','c')
root = int(pyperclip.paste())
root = math.sqrt(root)
pyautogui.doubleClick(420,357)
pyautogui.hotkey('ctrl','c')
multiply = int(pyperclip.paste())
value = root * multiply
answer = str(round(value, 2))
pyautogui.click(456,1057)
answer = "!ep1 -rep " + str(answer)
pyautogui.typewrite(answer)
pyautogui.typewrite(["enter"])
