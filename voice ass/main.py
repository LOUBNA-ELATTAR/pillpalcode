# importing_libraries
import cgitb 
cgitb.enable()
import subprocess
import pyttsx3
import wolframalpha
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import time
import requests
import shutil
from ecapture import ecapture as ec

# set engine to pyttsx3 for text to speech in Python
# and sapi5 in Microsoft speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# voice[1] - female
# voice[0] - male


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Bonjour !")

	elif hour>= 12 and hour<18:
		speak("Bon après-midi !")

	else:
		speak("Bonsoir !")

	assname =("Pilly")
	speak("i am your assistant")
	speak(assname)


def username():
	speak("heard you study math tools have fun with rachid tomorow ")
	uname = takeCommand()
	speak("Merci")
	speak(uname)
	columns = shutil.get_terminal_size().columns

	print("Merci ", uname)

	speak("Comment puis-je vous aider ?")

def takeCommand():

	r = sr.Recognizer()

	with sr.Microphone() as source:

		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='fr-FR')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Echec d'écoute.")
		return "None"

	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()

	# Enable low security in gmail
	server.login('email', 'mot de passe')
	server.sendmail('email', to, content)
	server.close()


# main function
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()
	username()

	while True:

		query = takeCommand().lower()

		# All the commands said by user will be
		# stored here in 'query' and will be
		# converted to lower case for easily
		# recognition of command
		if 'wikipedia' in query:
			speak('Cherchez dans Wikipedia ...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("Selon Wikipedia")
			print(results)
			speak(results)

		elif 'Accedez à youtube' in query:
			speak("Voici Youtube\n")
			webbrowser.open("youtube.com")

		elif 'Accedez à google' in query:
			speak("Voici Google\n")
			webbrowser.open("google.com")

		elif 'fais jouer de la musique' in query :
			speak("Voici votre musique")
			# music_dir = "G:\\Song"
			music_dir = "C:\\Users\\samar\\Music"
			songs = os.listdir(music_dir)
			print(songs)
			random = os.startfile(os.path.join(music_dir, songs[1]))

		elif 'Quelle heure est-il' in query:
			strTime = datetime.datetime.now().strftime("% H:% M:% S")
			speak(f" C'est : {strTime}")


		elif 'Envoyez un email' in query:
			try:
				speak("Que devrais-je dire?")
				content = takeCommand()
				to = "Destinataire"
				sendEmail(to, content)
				speak("Email envoyé !")
			except Exception as e:
				print(e)
				speak("Echec d'envoie")

		elif 'Envoyez un email' in query:
			try:
				speak("Que devrais-je dire?")
				content = takeCommand()
				speak("à qui devrais-je l'envoyer ?")
				to = input()
				sendEmail(to, content)
				speak("Email envoyé !")
			except Exception as e:
				print(e)
				speak("Echec d'envoie")

		elif 'Comment ca va' in query:
			speak("Ca va bien, merci")
			speak("Et vous ?")

		elif 'Ca va' in query or "bien" in query:
			speak("It's good to know that your fine")

		elif "changez mon nom à" in query:
			query = query.replace("changez mon nom ", "")
			assname = query

		elif "changez nom" in query:
			speak("Comment voudriez m'appeler ")
			assname = takeCommand()
			speak("Merci pour ce joli nom")

		elif "Comment tu t'appelles" in query or "C'est quoi votre nom" in query:
			speak("Mes amis m'appelle ")
			speak(assname)
			print("Mes amis m'appelle", assname , "Ravie de faire votre connaissance")

		elif 'sortir' in query:
			speak("Merci pour votre temps")
			exit()

		elif "Qui t'a crée" in query :
			speak("Je pense que j'ai vu le jour suite à une soudaine inspiration durant une longue et féconde promenade")

		elif 'blague' in query:
			speak(pyjokes.get_joke())

		elif "calculez" in query:

			app_id = "Wolframalpha api id"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate')
			query = query.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			print("Resultat: " + answer)
			speak("La réponse est est " + answer)

		elif 'cherchez' in query or 'fais jouer' in query:

			query = query.replace("cherchez", "")
			query = query.replace("fais jouer", "")
			webbrowser.open(query)

		elif "qui suis-je" in query:
			speak("Si vous pouvez parler donc vous étes un étre humain")

		elif "Pourquoi tu étais crée" in query:
			speak("C'est tout grace à PillPal, le reste est confidentiel")


		elif "T'es qui" in query:
			speak("Je suis Pilly, à votre service")

		elif 'reason for you' in query:
			speak(" Pour t'aider à completer votre traitement medical ")


		elif "arretez l'écoute" in query :
			speak("pendant combien de temps vous voulez empêcher Pilly d'écouter les commandes")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "Ou est" in query:
			query = query.replace("Ou est", "")
			location = query
			speak("L'utilisateur a demandé de localiser")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")

		elif "camera" in query or "prendre une photo" in query:
			ec.capture(0, "Pilly Camera ", "img.jpg")

		elif "redémarrez" in query:
			subprocess.call(["shutdown", "/r"])

		elif "Activez la mise en veille" in query or "mode hibernation" in query:
			speak("Activation du mode hibernation")
			subprocess.call("shutdown / h")

		elif "Déconnexion" in query :
			speak("Assurez-vous que toutes les applications sont fermées avant que vous déconnecter")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "écrire une note" in query:
			speak("Que voulez-vous qu'elle dise ?")
			note = takeCommand()
			file = open('Pilly.txt', 'w')
			speak("Dois-je inclure la date et l'heure ?")
			snfm = takeCommand()
			if 'oui' in snfm :
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)

		elif "affichez la note" in query:
			speak("Affichage des notes")
			file = open("Pilly.txt", "r")
			print(file.read())
			speak(file.read(6))


		elif "Pilly" in query:

			wishMe()
			speak("Pilly à votre écoute. Que puis-je faire pour vous ")
			speak(assname)

		elif "La météo" in query:

			# Google Open weather website
			# to get API of Open weather

			api_key = "Api key"
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			speak(" Nommer la ville ")
			print("Ville : ")
			city_name = takeCommand()
			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
			response = requests.get(complete_url)
			x = response.json()

			if x["cod"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (en kelvin) = " +str(current_temperature)+"\n Pression (en hPa) ="+str(current_pressure) +"\n humidité (en %) = " +str(current_humidiy) +"\n description = " +str(weather_description))

			else:
				speak(" Ville introuvable ")


		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Bonjour !" in query:
			speak("Bonjour")
			speak("Comment allez-vous aujourd'hui ?")
			speak(assname)

		elif "Veux-tu étre ma copine" in query or "veux-tu étre mon copin" in query:
			speak("Non ce n'est pas possible. En revanche si je peux vous aider pour autre chose, n'hesitez pas")

		elif "Comment ca va" in query:
			speak("Je suis contente d'étre en votre compagnie")

		elif "Comment allez-vous" in query :
			speak("Je vais bien. C'est gentil de votre part de demander")

		elif "je t'aime" in query:
			speak(" Moi aussi je vous trouve super")


		
		