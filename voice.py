import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib,winapps
from googlesearch import search
import wolframalpha,playsound
import time



class voice:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty("rate", 150)
    r = sr.Recognizer()
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))


    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def initial(self):
        with sr.Microphone() as source:
            self.r.pause_threshold = 1
            audio = self.r.listen(source)
            try:
                query = self.r.recognize_google(audio, language="en-in")
            except Exception:
                query = ''
        return query

    def takeCommand(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.r.pause_threshold = 1
            audio = self.r.listen(source)
        try:
            print("Recognizing...")
            query = self.r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception:
            print("Say that again please...")
            return ""
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()

    def app(i):
        for app in winapps.search_installed(i):
            app = str(app)
            path = app[app.find('WindowsPath')+13:app.find('install_source')-4]
            print(path)
            return path+r'/'+i.lower()+'.exe'
    
    def wish():
        playsound.playsound("Tuturu.mp3",0)
        time.sleep(2)
        playsound.playsound("tuturu_ohayo.mp3",0)
        time.sleep(4)


    def loop(self):
        x = False
        while True:
            while x:
                query = self.takeCommand(self).lower()
                try:
                    if 'wikipedia' in query:
                        self.speak(self, 'Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        self.speak(self, "According to Wikipedia")
                        print(results)
                        self.speak(self, results)
                except Exception:
                    self.speak(self, "didn't find the page")

                if 'open youtube' in query:
                    webbrowser.get('chrome').open_new('www.youtube.com')
                    self.speak(self, 'There we go!')

                elif 'open google' in query:
                    webbrowser.get('chrome').open_new('www.google.com')
                    self.speak(self, 'There we go!')

                elif 'open' in query:
                    for i in search(query[5:]):
                        webbrowser.get('chrome').open_new(i)
                        break

                elif 'search' in query and 'on youtube' in query:
                    webbrowser.get('chrome').open_new('www.youtube.com/results?search_query='+query.replace('search ', '').replace(' on youtube', ''))
                    self.speak(self, 'There we go!')
                    break

                elif 'play' in query and 'on youtube' in query:
                    webbrowser.get('chrome').open_new('www.youtube.com/results?search_query='+query.replace('play ', '').replace(' on youtube', ''))
                    self.speak(self, 'There we go!')
                    break

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    self.speak(self, f"Sir, the time is {strTime}")
                    
                    
                    
                    
                    
                    
                    
                else:
                    self.speak(self, query)
                    try:
                        if 'bye' not in query and 'stop' not in query and 'shut' not in query and "" in query:
                            client = wolframalpha.Client('53XLPG-KV7LVP2KAU')
                            self.speak(self,next(client.query(query).results).text)
                        if 'bye' in query or 'stop' in query:
                            x = False
                            self.speak(self, 'stopping system')
                        if 'shut' in query:
                            self.speak(self, 'shutting down')
                            return
                    except Exception:
                        pass

            tell = self.initial(self).lower()
            if 'start' in tell:
                x = True
                self.wish()
                #self.speak(self, 'starting system')
            elif 'shut' in tell:
                self.speak(self, 'shutting down')
                return


