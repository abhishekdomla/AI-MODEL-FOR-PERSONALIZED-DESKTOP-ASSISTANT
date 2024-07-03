from major import speak, wikipedia,sr, wishMe, webbrowser,datetime,os,ctypes,subprocess,pyjokes,time,ec,basicomand,terminate,json,urlopen
from main import gui

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='mr-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def marathi():
    # wishMe()
    while True:
      # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            gui() 
            break
        # elif "notepad" in query:
        #     speak ("उघडतोय notepad")
        #     newNote = takeCommand().lower()
        #     now = datetime.now().strftime("%H:%M:%S")
        #     with उघडा('note_%s.txt' % now, 'w') as newFile:
        #         newFile.write(now)
        #         newFile.write(' ')
        #         newFile.write(newNote)
        #     speak("note taken")

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
###### उघडतोय files #######         
        elif 'यूट्यूब उघडा' in query or 'यूट्यूब' in query:
            speak ("यूट्यूब उघडतोय")
            webbrowser.open("youtube.com")
            gui() 
            break
        elif 'गुगल उघडा' in query or 'गुगल' in query:
            speak ("गुगल उघडतोय")
            webbrowser.open("google.com")
            gui() 
            break
        elif 'स्टॅकओव्हरफ्लो उघडा' in query or 'स्टॅकओव्हरफ्लो' in query:
            speak ("स्टॅकओव्हरफ्लो उघडतोय")
            webbrowser.open("stackoverflow.com")
            gui() 
            break
        elif 'इन्स्टाग्राम उघडा' in query or 'इन्स्टाग्राम' in query:
            speak ("इन्स्टाग्राम उघडतोय")
            webbrowser.open("https://www.instagram.com")
            gui() 
            break
        elif 'विकिपीडिया उघडा' in query or 'विकिपीडिया' in query:
            speak ("विकिपीडिया उघडतोय")
            webbrowser.open("https://www.wikipedia.com")
            gui() 
            break
        elif 'फेसबुक उघडा' in query or 'फेसबुक' in query:
            speak ("फेसबुक उघडतोय")
            webbrowser.open("https://www.facebook.com")
            gui() 
            break
        elif 'व्हॉट्सॲप उघडा' in query or 'व्हॉट्सॲप' in query:
            speak ("व्हॉट्सॲप उघडतोय")
            webbrowser.open("https://web.whatsapp.com")
            gui() 
            break
        elif 'डेलीहंट उघडा' in query or 'डेलीहंट' in query:
            speak ("डेलीहंट उघडतोय")
            webbrowser.open("https://www.dailyhunt.in")
            gui() 
            break
        elif 'ग्रोव उघडा' in query or 'ग्रोव' in query:
            speak ("ग्रोव उघडतोय")
            webbrowser.open("https://groww.in/mutual-funds")
            gui() 
            break
        elif 'उघडा पेन्शन पोर्टल' in query or 'पेन्शन पोर्टल' in query:
            speak ("पेन्शन पोर्टल उघडतोय")
            webbrowser.open("https://pensionersportal.gov.in/")
            gui() 
            break
        elif 'योजना उघडा' in query or 'योजना' in query:
            speak ("योजना उघडतोय")
            webbrowser.open("https://pmjdy.gov.in/")
            gui() 
            break
        elif 'लाइव न्यूज उघडा' in query or 'लाइव न्यूज' in query:
            speak ("लाइव न्यूज उघडतोय")
            webbrowser.open("https://www.youtube.com/results?search_query=abp+news+live")
            gui() 
            break
        elif 'महाडीबीटी उघडा' in query or 'महाडीबीटी' in query:
            speak ("महाडीबीटी उघडतोय")
            webbrowser.open("https://aaplesarkar.mahaonline.gov.in/")
            gui() 
            break
###### music #######

        elif 'संगीत' in query:
            music_dir = 'C:\\Users\\MY PC\\Desktop\\kalimba.mpeg'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            gui() 
            break
        
###### Time #######

        elif 'वेळ सांगा' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"सर , वेळ आहे {strTime}")

###### Path of code #######

        elif 'कोड उघडा' in query:
            codePath = "C:/Users/MY PC/Desktop/ai-assistant-main/major.py"
            os.startfile(codePath)

###### windows action #######
        elif 'लॉक विंडोज' in query:
            speak("डिव्हाइस लॉक करत आहे")
            ctypes.windll.user32.LockWorkStation()
            break
        elif 'प्रणाली बंद करा' in query:
            speak("तुम्हाला खात्री आहे की तुम्ही सिस्टम बंद करू इच्छिता")
            dark = takeCommand().lower()
            if "हो" in dark or "खात्रीने" in dark or "रोबोट" in dark:
                speak("एक सेकंद थांबा! तुमची प्रणाली बंद होण्याच्या मार्गावर आहे")
                subprocess.call('shutdown / p /f')
                break
            elif "नाही" in dark:
                break
        # elif 'empty recycle bin' in query:
        #     winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        #     speak("Recycle Bin Recycled")
        elif "ऐकू नये" in query or "stop listening" in query:
            speak("तुम्हाला आज्ञा ऐकण्यापासून किती वेळ थांबवायचे आहे")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
            break
        elif "पुन्हा सुरू करा" in query:
            subprocess.call(["shutdown", "/r"])
        elif "हायबरनेट" in query or "sleep" in query:
            speak("हायबरनेटिंग")
            subprocess.call("shutdown / h")
            break
        elif "लॉग ऑफ करा" in query or "साइन-आउट" in query:
            speak("साइन-आउट करण्यापूर्वी सर्व अनुप्रयोग बंद असल्याची खात्री करा")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
            break

###### chat bot #######

        elif 'तूम्ही कसे आहात' in query:
             speak("मी ठीक आहे धन्यवाद")
             speak("कसे आहात, सर")
        elif 'ठीक' in query or "चांगले" in query:
            speak("हे जाणून घेणे चांगले आहे की तुम्ही खुशाल आहात")
            gui() 
            break
###### camera #######
        elif "कॅमेरा" in query or "फोटो काढ" in query or "आरसा" in query:
            ec.capture(0, "mirror", "img.jpg")
            gui() 
            break
###### email #######
        # elif 'email to rohan' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "abhishekdomala2000@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend rohan bhai. I am not able to send this email")
        #         gui() 
        #         break
###### jokes #######
        elif 'विनोद' in query or 'chutkule' in query:
            try:
                speak(pyjokes.get_joke())
                look = takeCommand()
                if 'विनोद' in look or 'आणखी एक' in look:
                    speak(pyjokes.get_joke())
                elif '' in look or 'थांबा' in look:
                    gui() 
                    break
                else:
                    break
            except Exception as e:
                print (e)
                speak('आदेश नाही')
                  
###### assistant #######
        elif "रोबोट" in query:
            # wishMe()
            speak("Jarvis 1 point o in your service Mister")
            
###### terminating assistant #######
        elif "समाप्त करणे" in query or 'बंद' in query or "बंद करा" in query or 'समाप' in query :
            speak ("सर मी तुमच्या सेवेसाठी सदैव उपस्थित राहील")
            gui()
            break

if __name__ == '__main__':
    back = basicomand()
    if "Robot" in back or "Nova" in back or "Innova" in back:
        # speak("thank you for activating me !")
        marathi
    elif "समाप्त करणे" in back or 'बंद' in back or "बंद करा" in back or 'समाप' in back :
            speak ("सर मी तुमच्या सेवेसाठी सदैव उपस्थित राहील")
            gui()
            terminate()

# if __name__ == '__main__':
#     while True:
#         try:
#             # Taking input from the user
#             user_input = input("Enter something: ")
#             if "marathi" in user_input:
#                 marathi() 
#             else:
#                 break
#         except Exception as e:
#             # Handle the exception (e.g., invalid input)
#             print("Error:", e)
#             print("Please try again.")