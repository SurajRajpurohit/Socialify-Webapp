from tkinter import *
import tkinter as tk
import speech_recognition as sr
from PIL import ImageTk,Image
from tkinter import messagebox
from googletrans import Translator
from datetime import datetime 
root = tk.Tk()
root.geometry('500x400')
root.resizable(False,False)
root.title('SOCIALIFY     just speak it !!!')
root.configure(bg='white')
icon = PhotoImage(file=r'C:\Users\Satish\Downloads\speaker.png')
root.iconphoto(False,icon)


   

def mainexit():
    ex = messagebox.askyesnocancel('notification','do you want to exit',parent=root)
    if (ex==True):
        root.destroy()



def st():
    import pyaudio
    import time
    import pyttsx3
    import speech_recognition as sr
    import pywhatkit


    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)

    def speak(audio):
            engine.say(audio)
            engine.runAndWait()

    def takeaudio(ques):
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("listening")
                r.pause_threshold = 1
                # audio = r.record(source)
                audio = r.listen(source,timeout=6,phrase_time_limit=10)

            try:
                speak("recognizing")
                query = r.recognize_google(audio,language='en-in')
                speak(f"did you said : {query}")
                
                speak("yes or no ")
                r2 = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("listening")
                    r2.pause_threshold = 1
                    # audio2 = r2.record(source)
                    audio2 = r2.listen(source,timeout=6,phrase_time_limit=4)
                    query2 = r2.recognize_google(audio2,language='en-in')
                    if query2 in ["yes","yeah","yes i said that"]:
                        return query.lower()
                    speak("then please say again")
                    speak(ques)
            except Exception as e:
                print(e)
                speak("unable to recognize")
                speak("please say again")
                speak(ques)
        
    def t(wmssg):
        di = {'zulu': 'zu', 'yoruba': 'yo', 'yiddish': 'yi', 'xhosa': 'xh', 'welsh': 'cy', 'vietnamese': 'vi', 'uzbek': 'uz', 'uyghur': 'ug', 'urdu': 'ur', 'ukrainian': 'uk', 
    'turkish': 'tr', 'thai': 'th', 'telugu': 'te', 'tamil': 'ta', 'tajik': 'tg', 'swedish': 'sv', 'swahili': 'sw', 'sundanese': 'su', 'spanish': 'es', 'somali': 'so', 'slovenian': 'sl', 'slovak': 'sk', 'sinhala': 'si', 'sindhi': 'sd', 'shona': 'sn', 'sesotho': 'st', 'serbian': 'sr', 'scots gaelic': 'gd', 'samoan': 'sm', 'russian': 'ru', 'romanian': 'ro', 'punjabi': 'pa', 'portuguese': 'pt', 'polish': 'pl', 'persian': 'fa', 'pashto': 'ps', 'odia': 'or', 'norwegian': 'no', 'nepali': 'ne', 'myanmar (burmese)': 'my', 'mongolian': 'mn', 'marathi': 'mr', 'maori': 'mi', 'maltese': 'mt', 'malayalam': 'ml', 'malay': 'ms', 'malagasy': 'mg', 'macedonian': 'mk', 'luxembourgish': 'lb', 'lithuanian': 'lt', 'latvian': 'lv', 'latin': 'la', 'lao': 'lo', 'kyrgyz': 'ky', 'kurdish (kurmanji)': 'ku', 'korean': 'ko', 'khmer': 'km', 'kazakh': 'kk', 'kannada': 'kn', 'javanese': 'jw', 'japanese': 'ja', 'italian': 'it', 'irish': 'ga', 'indonesian': 'id', 'igbo': 'ig', 'icelandic': 'is', 
    'hungarian': 'hu', 'hmong': 'hmn', 'hindi': 'hi', 'hebrew': 'iw', 'hawaiian': 'haw', 'hausa': 'ha', 'haitian creole': 'ht', 'gujarati': 'gu', 'greek': 'el', 'german': 'de', 'georgian': 'ka', 'galician': 'gl', 'frisian': 'fy', 'french': 'fr', 'finnish': 'fi', 'filipino': 'tl', 'estonian': 'et', 'esperanto': 'eo', 'english': 'en', 'dutch': 'nl', 'danish': 'da', 'czech': 'cs', 'croatian': 'hr', 'corsican': 'co', 'chinese (traditional)': 'zh-tw', 'chinese (simplified)': 'zh-cn', 'chichewa': 'ny', 'cebuano': 'ceb', 'catalan': 'ca', 'bulgarian': 'bg', 'bosnian': 'bs', 'bengali': 'bn', 'belarusian': 'be', 'basque': 'eu', 'azerbaijani': 'az', 'armenian': 'hy', 'arabic': 'ar', 'amharic': 'am', 'albanian': 'sq', 'afrikaans': 'af'}
        speak('in which language do you want to translate the text')
        q5 = 'speak the name of language'
        speak(q5)
        d = takeaudio(q5)
        if d in di:
            dd = di.get(d,'Absent')
            # print(dd)
            translater = Translator()
            out = translater.translate(wmssg,dest=dd)
            speak('your translated message is ')
            speak(out.pronunciation)
            # print(out.text)
            # pyperclip.copy(out.text)
            return out.text 
        else:
            speak('no such language speak clearly ')
            t()
    def endingbot(text):
        # print(text)
        if text=="switch off":
            return True
      
           


    if __name__  == '__main__':
        phonebook = {"harshada":"+919136029000","rishi":"+917715918054","smita":"+919226753777","renuka mam":"+919702664520","sujata mam":"+917021835071","vaishali mam":"+919920184138"}
        currtime = datetime.now()
        reqformathour = int(currtime.strftime("%H"))
        if reqformathour<12 and reqformathour>0:
            speak("Good Morning")
        elif reqformathour>12 and reqformathour<18:
            speak("Good Afternoon")
        else:
            speak("Good Evening")
        askforrepeat = False
        while askforrepeat!=True:
            q1 = "Whom should i text"
            speak(q1)
            
            while True:
                takecontactname = takeaudio(q1)
                print(takecontactname)
                if endingbot(takecontactname):
                    break
                contactnumber = phonebook.get(takecontactname,False)
                if contactnumber==False:
                    speak("No Such Contact Sir!")
                    speak("Give another name")
                else:
                    break
            if endingbot(takecontactname):
                break 
            print(contactnumber)
            q2 = "Say your message"
            speak(q2)
            takemssg = takeaudio(q2)
            if endingbot(takemssg):
                break
            q3 = 'should I translate your message'
            speak(q3)
            asktranslation = takeaudio(q3)
            if endingbot(asktranslation):
                break
            
            if asktranslation in ["yes","you can","do it","yes you can"] :
                translatedmssg = t(takemssg)
                speak("sending message")
                reqformatmin = int(currtime.strftime("%M"))+3
                print(reqformathour,reqformatmin)
                pywhatkit.sendwhatmsg(contactnumber,translatedmssg,reqformathour,reqformatmin)
            else:
                speak("sending message")
                reqformatmin = int(currtime.strftime("%M"))+3
                print(reqformathour,reqformatmin)
                pywhatkit.sendwhatmsg(contactnumber,takemssg,reqformathour,reqformatmin)
            q4 = "should i send message to others"
            speak(q4)
            askforrepeat = takeaudio(q4)
            if askforrepeat not in ["yes repeat","yes","repeat"]:
                if endingbot(askforrepeat):
                    break
                break
        speak("switching off")
        root.destroy()

    
        # if 1:

        #     query = takeaudio().lower()
            


        #     if 'whatsapp' in query:
        #         speak("to whom sholud i send message")
        #         wname = takeaudio().lower()
        #         speak("speak your message")
        #         wmssg = takeaudio().lower()
        #         speak('do you want to translate your message')
        #         speak(' say yes or no')
        #         yn = takeaudio()
        #         if 'yes' in yn:
        #             tt = t(wmssg)
        #             print(tt)
        #             webbrowser.open('https://web.whatsapp.com/')             
        #             time.sleep(25) 
        #             pyautogui.click(354,270) 
        #             pyautogui.typewrite(wname) 
        #             time.sleep(4)
        #             pyautogui.click(351,501)
        #             time.sleep(3)
        #             pyautogui.click(1024,1024)
        #             time.sleep(3)
        #             pyautogui.hotkey('ctrl','v' )
        #             time.sleep(3)
        #             pyautogui.click(1873,1022)
        #         else:
        #             webbrowser.open('https://web.whatsapp.com/')             
        #             time.sleep(25) 
        #             pyautogui.click(354,270) 
        #             pyautogui.typewrite(wname) 
        #             time.sleep(4)
        #             pyautogui.click(351,501)
        #             time.sleep(3)
        #             pyautogui.typewrite(wmssg)
        #             time.sleep(2)
        #             pyautogui.click(1870,980)




        #     elif 'instagram' in query :
        #         speak("to whom should i send message")
        #         speak("please say account name clear and loud")
        #         iname = takeaudio().lower()
        #         speak("speak your message")
        #         imssg = takeaudio().lower()
        #         speak("sending message please dont disturb")
        #         webbrowser.open('https://www.instagram.com/')
        #         time.sleep(17)
        #         #print(pyautogui.position())
        #         pyautogui.click(832,199)
        #         time.sleep(5)
        #         pyautogui.typewrite(iname)
        #         time.sleep(6)
        #         pyautogui.click(860,292)
        #         time.sleep(7)
        #         pyautogui.click(998,331)
        #         time.sleep(7)
        #         pyautogui.typewrite(imssg)
        #         time.sleep(2)
        #         pyautogui.click(1628,915)

        #     elif 'facebook' in  query:
        #         speak("to whom should i send message")
        #         fname = takeaudio().lower()
        #         speak("say your message")
        #         fmssg = takeaudio().lower()     
        #         speak("sending message dont disturb")
        #         webbrowser.open('https://www.facebook.com/')
        #         #time.sleep(7)
        #         #print(pyautogui.position())
        #         time.sleep(20)
        #         pyautogui.click(1695,193)
        #         time.sleep(7)
        #         pyautogui.click(1610,350)
        #         time.sleep(5)
        #         pyautogui.typewrite(fname)
        #         time.sleep(5)
        #         pyautogui.click(1506,464)
        #         time.sleep(8)
        #         pyautogui.typewrite(fmssg)
        #         time.sleep(2)
        #         pyautogui.click(1727,973)

        #     else:
        #         pass    


ax = PhotoImage(file =r"C:\Users\Satish\Downloads\socialify.png")
canvas1 = Canvas(root,width=300,height=200)
canvas1.pack(fill = "both",expand = True)
canvas1.create_image(0,0,image=ax,anchor="nw")
#   canvas1.create_text(300,250,text="Just Speak")
def resize_bg(event):
    global bgg, resized, bg2
    
    bgg = Image.open(r"C:\Users\Satish\Downloads\socialify.png")
    
    resized = bgg.resize((500,400),Image.ANTIALIAS)
    
    bg2 = ImageTk.PhotoImage(resized)
    canvas1.create_image(0, 0, image=bg2, anchor='nw')
# bind resized function with root window
root.bind("<Configure>", resize_bg)

imagebutton1 = PhotoImage(file=r'C:\Users\Satish\Downloads\microphone.png')
photoimage = imagebutton1.subsample(20,20)

imagebutton2 = PhotoImage(file=r'C:\Users\Satish\Downloads\pause-button.png')
photoimage1 = imagebutton2.subsample(20,20)

button1 = Button(root,text='START',bd=10,bg='yellow',activebackground='red',font=('times',15,'italic bold'),image=photoimage,compound=RIGHT,command=st)
button1.place(x=50,y=290)
button1.configure(width=80,height=40)

button2 = Button(root,text='EXIT',bd=10,bg='red',activebackground='red',font=('times',15,'italic bold'),image=photoimage1,compound=RIGHT,command=mainexit)
button2.place(x=350,y=290)
button2.configure(width=80,height=40)

root.mainloop()