from major import speak, wikipedia, sr, wishMe, webbrowser,datetime,os,ctypes,subprocess,pyjokes,time,ec,basicomand,terminate,json,urlopen
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
        query = r.recognize_google(audio, language='hi-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query


def hindi():
    wishMe()
    while True:
      # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'विकिपीडिया' in query:
            speak('विकिपीडिया मैं खोज रहा हूँ...')
            query = query.replace("विकिपीडिया", "")
            results = wikipedia.summary(query, sentences=3)
            speak("विकिपीडिया के अनुसार")
            print(results)
            speak(results)
            gui() 
            break
        # elif "notepad" in query:
        #     speak ("opening notepad")
        #     newNote = takeCommand().lower()
        #     now = datetime.now().strftime("%H:%M:%S")
        #     with open('note_%s.txt' % now, 'w') as newFile:
        #         newFile.write(now)
        #         newFile.write(' ')
        #         newFile.write(newNote)
        #     speak("note taken")

        elif "एक लेख लिखो" in query:
            speak("क्या लिखूं सर")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("सर, क्या मुझे तारीख और समय शामिल करना चाहिए?")
            snfm = takeCommand()
            if 'हाँ' in snfm or 'ज़रूर' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif "नोट दिखाओ" in query:
            speak("नोट्स दिखा रहा हूँ")
            file = open("jarvis.txt", "r")
            speak(file.read())
            print(file.read())
            gui() 
            break
            

###### Opening files #######
            
        elif 'यूट्यूब खोलें' in query:
            speak ("यूट्यूब खुल रहा है")
            webbrowser.open("youtube.com")
            gui() 
            break
        elif 'गूगल खोलो' in query:
            speak ("गूगल खुल रहा है")
            webbrowser.open("google.com")
            gui() 
            break
        elif 'स्टैकओवरफ़्लो खोलें' in query:
            speak ("स्टैकओवरफ़्लो खुल रहा है")
            webbrowser.open("stackoverflow.com")
            gui() 
            break
        elif 'इंस्टाग्राम खोलें' in query:
            speak ("इंस्टाग्राम खुल रहा है")
            webbrowser.open("https://www.instagram.com")
            gui() 
            break
        elif 'विकिपीडिया खोलें' in query:
            speak ("विकिपीडिया खुल रहा है")
            webbrowser.open("https://www.wikipedia.com")
            gui() 
            break
        elif 'फ़ेसबुक खोलो' in query:
            speak ("फेसबुक खुल रहा है")
            webbrowser.open("https://www.facebook.com")
            gui() 
            break
        elif 'व्हाट्सएप खोलें ' in query:
            speak ("व्हाट्सएप खुल रहा है")
            webbrowser.open("https://web.whatsapp.com")
            gui() 
            break
        elif 'ओपन डेलीहंट' in query:
            speak ("डेलीहंट खुल रहा है")
            webbrowser.open("https://www.dailyhunt.in")
            gui() 
            break
        elif 'ओपन ग्रो' in query:
            speak ("ग्रो खुल रहा है")
            webbrowser.open("https://groww.in/mutual-funds")
            gui() 
            break
        elif 'पेंशनपोर्टल खोलें' in query:
            speak ("पेंशनपोर्टल खुल रहा है")
            webbrowser.open("https://pensionersportal.gov.in/")
            gui() 
            break
        elif 'कृपया योजना ओपन करो' in query:
            speak ("योजना खुल रहा है")
            webbrowser.open("https://pmjdy.gov.in/")
            gui() 
            break
        elif 'सजग समाचार खोलें' in query:
            speak ("सजगसमाचार खुल रहा है")
            webbrowser.open("https://www.youtube.com/results?search_query=abp+news+live")
            gui() 
            break
        elif 'महा डीबीटी पोर्टल खोलें ' in query:
            speak ("महा डीबीटी पोर्टल खुल रहा है ")
            webbrowser.open("https://aaplesarkar.mahaonline.gov.in/")
            gui() 
            break
###### music #######

        elif 'कृपया संगीत बजाना' in query:
            music_dir = 'C:/Users/MY PC/Desktop/projects/ai-assistant-main/kalimba.mpeg'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            gui() 
            break
        
###### Time #######

        elif 'कृपया समय बताना' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

###### Path of code #######

        elif 'कृपया कोड खोलें' in query:
            codePath = "C:/Users/MY PC/Desktop/ai-assistant-main/major.py"
            os.startfile(codePath)

###### windows action #######
        # elif 'कृपया विंडोज लॉक करे' in query:
        #     speak("विंडोज लॉक हो रहा है")
        #     ctypes.windll.user32.LockWorkStation()
        #     break
        # elif 'शटडाउन करे' in query:
        #     speak("क्या आप वाकई सिस्टम को बंद करना चाहते हैं?")
        #     dark = takeCommand().lower()
        #     if "हाँ" in dark or "ज़रूर" in dark or "रोबोट" in dark:
        #         speak("एक सेकंड के लियॆ रोको ! आपका सिस्टम बंद होने की राह पर है")
        #         subprocess.call('shutdown / p /f')
        #         break
        #     elif "नहीं" in dark:
        #         break
        # # elif 'empty recycle bin' in query:
        # #     winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        # #     speak("Recycle Bin Recycled")
        # elif "मत सुनो" in query or "सुनना बंद करो" in query:
        #     speak("आप कितने समय तक कमांड सुनने से रोकना चाहते हैं")
        #     a = int(takeCommand())
        #     time.sleep(a)
        #     print(a)
        #     break
        # elif "पुनः आरंभ करें" or "रिस्टार्ट" in query:
        #     subprocess.call(["shutdown", "/r"])
        # elif "सीतनिद्रा " in query or "स्लीप" or "हाइबरनेट" in query:
        #     speak("सुप्तावस्था")
            
            subprocess.call("shutdown / h")
            break
        elif "लॉग ऑफ़" in query or "साइन आउट" in query:
            speak("सुनिश्चित करें कि साइन-आउट से पहले सभी एप्लिकेशन बंद हैं")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
            break

###### chat bot #######

        elif 'आप कैसे हैं' in query:
             speak("मैं ठीक हूं आपका धन्यवाद")
             speak("कैसे हो जनाब")
        elif 'अच्छा' in query or "ठीक" in query:
            speak("यह जानकर अच्छा लगा कि आप ठीक हैं")
            gui() 
            break
###### camera #######
        elif "कैमरा" in query or "एक तस्वीर लें" in query or "आईना" in query:
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
        elif 'मज़ाक' in query or 'चुटकुला' in query:
            try:
                speak(pyjokes.get_joke())
                look = takeCommand()
                if 'चुटकुला' in look or 'और एक' in look:
                    speak(pyjokes.get_joke())
                elif '' in look or 'रुकना' in look:
                    gui() 
                    break
            except Exception as e:
                print (e)
                speak('कोई आदेश नहीं')
                  
###### assistant #######
        elif "रोबोट" in query:
            wishMe()
            speak("जार्विस 1 अंक आपकी सेवा में श्रीमान")
            
###### terminating assistant #######
        elif "बर्खास्त" in query or "बंद करे" in query or 'टर्मिनेट' in query :
            speak ("सर, मैं हमेशा आपके सेवा केलिए मौजूद रहूँगा")
            gui()
            break
    
if __name__ == '__main__':
    back = basicomand()
    if "Robot" in back or "Nova" in back or "Innova" in back:
        # speak("thank you for activating me !")
        hindi()
    elif "बर्खास्त" in back or 'बंद' in back or "बंद करे" in back or 'टर्मिनेट' in back :
            speak ("सर, मैं हमेशा आपके सेवा केलिए मौजूद रहूँगा")
            gui()
            terminate()

# if __name__ == '__main__':
#     while True:
#         try:
#             # Taking input from the user
#             user_input = input("Enter something: ")
#             if "hindi" in user_input:
#                 hindi() 
#             else:
#                 break
#         except Exception as e:
#             # Handle the exception (e.g., invalid input)
#             print("Error:", e)
#             print("Please try again.")