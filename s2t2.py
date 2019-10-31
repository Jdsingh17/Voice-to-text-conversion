'''
Created on 30-10-2019
@author : lucifer
Instructions
-----------------
1. sudo pip install SpeechRecognition
2. sudo apt-get install pyaudio
'''

import speech_recognition as sr
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
def LedBlinkABK():
	while True:
		GPIO.output(8,GPIO.HIGH)
		sleep(1)
		GPIO.output(8,GPIO.LOW)
		sleep(1)

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Ayy Bolo Naa : ")
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source)

	try:
		text = r.recognize_google(audio)
		print("You said : {}".format(text))
		LedBlinkABK()
	except:
		print("Ayy Phir se Bolo naa")
