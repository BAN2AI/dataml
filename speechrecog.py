import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
	print('Speek something')
	audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		print('tu a dit : {}'.format(text))
	except:
		print('desole, t as une trop moche voies')