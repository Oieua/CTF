import pyautogui
import pyperclip
import base64
import time


pyautogui.click(377,360)
pyautogui.typewrite("!ep2")
pyautogui.typewrite(["enter"])
time.sleep(0.5)
pyautogui.tripleClick(375,359)
pyautogui.hotkey('ctrl','c')
encoded = str(pyperclip.paste())
decoded = str(base64.b64decode(encoded))
pyautogui.click(456,1057)
answer = "!ep2 -rep " + str(decoded[2:len(decoded)-1])
pyautogui.typewrite(answer)
pyautogui.typewrite(["enter"])
