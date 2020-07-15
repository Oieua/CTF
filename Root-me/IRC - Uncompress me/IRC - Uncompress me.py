import pyautogui
import pyperclip
import base64
import time
import zlib

#Find position of the cursor
#while True:
#	print(pyautogui.position())

pyautogui.click(377,360) #Position of the chat bar on the screen
pyautogui.typewrite("!ep4")
pyautogui.typewrite(["enter"])
time.sleep(0.5)
pyautogui.tripleClick(375,359) #Position of the received text on the sceen
pyautogui.hotkey('ctrl','c')
text = pyperclip.paste()
text = base64.b64decode(text)
text = str(zlib.decompress(text))
pyautogui.click(456,1057)
answer = "!ep4 -rep " + str(text[2:len(text)-1])
pyautogui.typewrite(answer)
pyautogui.typewrite(["enter"])
