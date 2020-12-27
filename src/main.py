import Upload
import pyttsx3
import datetime
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
import speech_recognition as sr
if __name__ == "__main__":
	the_hour=int(datetime.datetime.now().hour)
	if the_hour>=0 and the_hour<12:
		engine.say("Bonjour")					    
		engine.runAndWait()
	if the_hour>=12 and the_hour<18:
		engine.say("Bonne après-midi")					    
		engine.runAndWait()
	if the_hour>=18 and the_hour<0:
		engine.say("Bonsoir")					    
		engine.runAndWait()
	r = sr.Recognizer()
	while(True):
		with sr.Microphone() as source:
			try:
				audio = r.listen(source)
				data = r.recognize_google(audio)
				print(data)
				if data!=0:
					if "upload" in data:
						phrases=["Le titre s'il vous plaît","La description s'il vous plaît","Est-ce-que le contenu est-il désigné aux enfants?"]
						responses=[]
						for a in phrases:
							if a!="Le titre s'il vous plaît" or a!="La description s'il vous plaît":
							    engine.say(a)
							    engine.runAndWait()
							    audio = r.listen(source)
							    answer = r.recognize_google(audio)
							    responses.append(answer)
							    print(answer)
							    if answer=="Yes":
								    answer=True
								    responses.append(answer)
							    if answer=="No":
								    answer=False
								    responses.append(answer)
							else:
							    engine.say(a)
							    engine.runAndWait()
							    audio = r.listen(source)
							    answer = r.recognize_google(audio)
							    responses.append(answer)
						title=responses[0]
						description=responses[1]
						Kids=responses[2]
						print(responses)
						Upload.Upload_Video(title,description,Kids)
					elif "thanks" in data:
						engine.say("Je vous en prie !")
						engine.runAndWait()
					elif "hi" in data or "hello" in data:
						if "hi" in data:
							engine.say("Salut")
							engine.runAndWait()
						if "hello" in data:
								if the_hour>=0 and the_hour<12:
									engine.say("Bonjour")					    
									engine.runAndWait()
								if the_hour>=12 and the_hour<18:
									engine.say("Bonne après-midi")					    
									engine.runAndWait()
								if the_hour>=18 and the_hour<0:
									engine.say("Bonsoir")					    
									engine.runAndWait()
			except:
				print("Retry")


