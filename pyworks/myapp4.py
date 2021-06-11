import speech_recognition as sr
import os
print("welcome to the tools")
import webbrowser
print("enter your requirement:", end='')
#ch=input()
r=sr.Recognizer()
with sr.Microphone() as source:
    print("start say!!")
    audio=r.listen(source)
    print("speech Done")
ch=r.recognize_google(audio)
if "date" in ch:
    print("date")
    os.system("date")
    webbrowser.open("http://54.169.27.197/cgi-bin/me.py?c=date")
elif "calendar" in ch:
    print("cal")
    webbrowser.open("http://54.169.27.197/cgi-bin/me.py?c=cal")
elif "list" in ch:
    print("ls")
    webbrowser.open("http://54.169.27.197/cgi-bin/me.py?c=ls")    
else:
    print("not understand")

