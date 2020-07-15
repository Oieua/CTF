import pyautogui
import pyperclip
import base64
import time


#Find position of the cursor (x and y coordinates)
#while True:
#	print(pyautogui.position())


pyautogui.click(377,360) #Position of the chat bar on the screen
pyautogui.typewrite("!ep2")
pyautogui.typewrite(["enter"])
time.sleep(0.5)
pyautogui.tripleClick(375,359) #Position of the received text on the sceen
pyautogui.hotkey('ctrl','c')
encoded = str(pyperclip.paste())
decoded = str(base64.b64decode(encoded))
pyautogui.click(456,1057)
answer = "!ep2 -rep " + str(decoded[2:len(decoded)-1])
pyautogui.typewrite(answer)
pyautogui.typewrite(["enter"])
