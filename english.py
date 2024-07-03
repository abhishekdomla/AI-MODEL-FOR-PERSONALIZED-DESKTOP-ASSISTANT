from major import speak, wikipedia, sr,takeCommand, wishMe, webbrowser,datetime,os,ctypes,subprocess,pyjokes,time,ec,basicomand,terminate,json,urlopen,pyttsx3
from main import gui,facedetection
import fitz
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def read_pdf(pdf_path):
    try:
        # Open the PDF file
        document = fitz.open(pdf_path)
        
        # Initialize text-to-speech engine
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        # print(voices[1].id)
        engine.setProperty('voice', voices[1].id)
        
        # Read each page of the PDF
        for page_num in range(len(document)):
            # Extract text from the current page
            page = document.load_page(page_num)
            text = page.get_text()
            
            # Speak the text using text-to-speech engine
            engine.say(text)
            engine.runAndWait()

    except Exception as e:
        print("Error:", e)
        speak("Sorry, I couldn't read the PDF file.")

    except Exception as e:
        print("Error:", e)
        speak("Sorry, I couldn't read the PDF file.")

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=3)
        return results
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        print("The term you searched for is ambiguous. Please choose one of the following options:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        choice = int(input("Enter the number corresponding to your choice: "))
        selected_option = options[choice - 1]
        results = wikipedia.summary(selected_option, sentences=3)
        return results

def play_music():
    music_dir = 'C:/Users/MY PC/Desktop/projects/ai-assistant-main/'  # Update the directory path if necessary
    song_file = 'kalimba.mpeg'  # Update the song file name if necessary
    song_path = os.path.join(music_dir, song_file)

    if os.path.exists(song_path):
        try:
            os.startfile(song_path)
            print("Playing music...")
        except Exception as e:
            print(f"Error playing music: {e}")
    else:
        print("Music file not found.")


def english():
    wishMe()
    while True:
      # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = search_wikipedia(query)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                gui() 
                break
            except Exception as e:
                print("An error occurred:", str(e))
                speak("Sorry, I encountered an error while searching Wikipedia.")
                gui() 
                break
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            speak(file.read())
            print(file.read())
            gui() 
            break
###### Opening files #######
        elif 'open youtube' in query:
            search_query = query.replace("open youtube", "").strip()
            if search_query:
                speak(f"Searching YouTube for {search_query}")
                search_url = f"https://www.youtube.com/results?search_query={search_query}"
                webbrowser.open(search_url)
            else:
                speak("What do you want to search on YouTube?")
                user_query = takeCommand()
                if user_query:
                    search_url = f"https://www.youtube.com/results?search_query={user_query}"
                    webbrowser.open(search_url)
                else:
                    speak("Sorry, I didn't get that. Opening the YouTube homepage.")
                    webbrowser.open("https://www.youtube.com/")
            gui() 
            break
        elif 'open google' in query:
            search_query = query.replace("open google", "").strip()
            if search_query:
                speak(f"Searching Google for {search_query}")
                search_url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(search_url)
            else:
                speak("What do you want to search on Google?")
                user_query = takeCommand()
                if user_query:
                    search_url = f"https://www.google.com/search?q={user_query}"
                    webbrowser.open(search_url)
                else:
                    speak("Sorry, I didn't get that. Opening the Google homepage.")
                    webbrowser.open("https://www.google.com/")
            gui() 
            break
        elif 'open stackoverflow' in query:
            speak ("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
            gui() 
            break
        elif 'open instagram' in query:
            speak ("opening instagram")
            webbrowser.open("https://www.instagram.com")
            gui() 
            break
        elif 'open wikipedia' in query:
            speak ("opening wikipedia")
            webbrowser.open("https://www.wikipedia.com")
            gui() 
            break
        elif 'open facebook' in query:
            speak ("opening facebook")
            webbrowser.open("https://www.facebook.com")
            gui() 
            break
        elif 'open whatsapp ' in query:
            speak ("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com")
            gui() 
            break
        elif 'open dailyhunt' in query:
            speak ("opening dailyhunt")
            webbrowser.open("https://www.dailyhunt.in")
            gui() 
            break
        elif 'open grow' in query:
            speak ("opening grow")
            webbrowser.open("https://groww.in/mutual-funds")
            gui() 
            break
        elif 'open pensionportal' in query:
            speak ("opening grow")
            webbrowser.open("https://pensionersportal.gov.in/")
            gui() 
            break
        elif 'open yojna' in query:
            speak ("opening yojna")
            webbrowser.open("https://pmjdy.gov.in/")
            gui() 
            break
        elif 'open live news' in query:
            speak ("opening livenews")
            webbrowser.open("https://www.youtube.com/results?search_query=abp+news+live")
            gui() 
            break
        elif 'open mahadbt' in query:
            speak ("opening mahadbt")
            webbrowser.open("https://aaplesarkar.mahaonline.gov.in/")
            gui() 
            break
###### music #######
        elif 'play music' in query:
            play_music()
            gui() 
            break       
###### Time #######
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
###### Path of code #######
        elif 'open code' in query:
            codePath = "C:/Users/MY PC/Desktop/projects/ai-assistant-main/english.py"
            os.startfile(codePath)
            break
###### windows action #######
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
            break
        elif 'shutdown system' in query:
            speak("are you sure you want to shut down the system")
            dark = takeCommand().lower()
            if "yes" in dark or "sure" in dark or "robot" in dark:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                break
            elif "no" in dark:
                break
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop  from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
            break
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            
            subprocess.call("shutdown / h")
            break
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
            break
###### chat bot #######
        elif 'how are you' in query:
             speak("I am fine, Thank you")
             speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            gui() 
            break
###### camera #######
        elif "camera" in query or "take a photo" in query or "mirror" in query:
            ec.capture(0, "mirror", "img.jpg")
            gui() 
            break
# ###### jokes #######
        elif 'joke' in query:
            try:
                speak(pyjokes.get_joke())
                look = takeCommand()
                if 'joke' in look or 'one more' in look:
                    speak(pyjokes.get_joke())
                elif '' in look or 'stop' in look:
                    gui() 
                    break
            except Exception as e:
                print (e)
                speak('no command')               
###### assistant #######
        elif "robot" in query:
            wishMe()
            speak("robot 1 point o in your service Mister")            
###### terminating assistant #######
        elif "terminate" in query or 'break' in query or "band kar" in query or 'terminator' in query :
            speak ("always be there for you sir , robotic")
            terminate()
            gui()
            break
        elif 'news' in query:
            try:
                jsonObj = urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=c09536bb5d8a430cad3926ae510e447a')
                data = json.load(jsonObj)
                i = 1
                speak('Here are some top news from The Times of India')
                print('=============== TIMES OF INDIA ============' + '\n')
                for item in data['articles'][:3]:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    break
            except Exception as e:
                print(str(e))
        elif 'read pdf' in query or 'open pdf' in query:
            speak("Sure, please provide the path to the PDF file.")
            pdf_path = takeCommand() + ".pdf"
            read_pdf(pdf_path)
            gui()  # Assuming this function exists to show the graphical user interface
            break
        elif "face detection" in query:
            speak("for terminating please press q")
            facedetection()
            break

if __name__ == '__main__':
    back = basicomand()
    if "Robot" in back or "Nova" in back or "Innova" in back or "robot" in back or "nova" in back or "innova" in back:
        # speak("thank you for activating me !")
        english()
    elif "terminate" in back or 'break' in back or 'terminator' in back:
        speak("terminating the system")
        gui()
        terminate()



# if __name__ == '__main__':
#     while True:
#         try:
#             # Taking input from the user
#             user_input = input("Enter something: ")
#             if "english" in user_input:
#                 english()
#             else:
#                 break
#         except Exception as e:
#             # Handle the exception (e.g., invalid input)
#             print("Error:", e)
#             print("Please try again.")/*