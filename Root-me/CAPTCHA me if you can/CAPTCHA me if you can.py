import pytesseract
from PIL import Image
import numpy
import pyautogui
import time



pyautogui.click(387,350)

time.sleep(0.1)

screenshot = pyautogui.screenshot('image.png',region=(111,250,250,150)) #Make a screenshot



#Screenshot coloring
im = numpy.array(Image.open('image.png'))
for i in range (0,len(im),1):
	for j in range (0,len(im[i]),1):
		for k in range (0,3,1):
			if im[i][j][k]==0:
				im[i][j][k]=255
gr_im= Image.fromarray(im).save('image2.png')


#Colored screenshot analise
img = Image.open('image2.png')
text = pytesseract.image_to_string(img) 

#Submit text
pyautogui.click(201,350)
pyautogui.typewrite(str(text))
pyautogui.click(387,350)
