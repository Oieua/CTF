import pyautogui
import pyperclip
import time
import codecs

pyautogui.click(377,360)
pyautogui.typewrite("!ep3")
pyautogui.typewrite(["enter"])
time.sleep(0.5)
pyautogui.tripleClick(375,359)
pyautogui.hotkey('ctrl','c')
encoded = str(pyperclip.paste())
decoded = str(codecs.encode(encoded,'rot_13'))
pyautogui.click(456,1057)
answer = "!ep3 -rep " + str(decoded)
pyautogui.typewrite(answer)
pyautogui.typewrite(["enter"])
