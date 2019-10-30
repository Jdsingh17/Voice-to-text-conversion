#aurthor: Rishi Prajapati (leftyyyy)
#make sure to have following packages:
#1. PyAudio (conda install PyAudio)
#2. googleAPIpython (conda install -c conda-forge google-api-python-client)
#3. speech_recognition (conda install SpeechRecognition)
import speech_recognition as sr
rec=sr.Recognizer()
with sr.Microphone as source:
	print("bol bosdk")
	audio = r.listen(source)
try:
	#passing it to googleA
	txt = r.recognize_google(audio)
	arr=[str(_) for _ in txt.split()]
	return arr
except:
	print("firse bol bosdk")
