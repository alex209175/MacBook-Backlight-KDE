import os
import keyboard

while True:
	if keyboard.is_pressed('f1'):
		os.system('xbacklight -10')
	if keyboard.is_pressed('f2'):
		os.system('xbacklight +10')
