import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui

#pyautogui.MINIMUM_DURATION = 0
#pyautogui.MINIMUM_SLEEP = 0
#pyautogui.PAUSE = 0.01

def draw(x1, y1, x2, y2):
	originalImage = cv2.imread('./ang.png')
	grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
	(thresh, bawImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
	
	h, w = bawImage.shape
	
	for i in range(0, min(h, y2-y1)):
		abscissa = 0
		for j in range(1, min(w, x2-x1)):
			if(bawImage[i][j] == 0):
				if(bawImage[i][j-1] == 255):
					abscissa = j
				
				if(bawImage[i][j+1] == 255):
					pyautogui.moveTo(x1 + abscissa + 10, y1 + i + 10, duration=0.01)
					pyautogui.drag(j-abscissa, 0, duration=0.125, button = 'left')
					
	#cv2.imshow('B&W image', bawImage)
	#cv2.imshow('Original image',originalImage)
	#cv2.imshow('Gray image', grayImage)
	  
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
