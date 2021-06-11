import os
import pyttsx3  as sp
import speech_recognition as sr
print("Enter your requirement:")
#r=input()
r=sr.Recognizer()
with sr.Microphone() as source:
    sp.speak("Welcome BOSS! What you wish to open")
    audio=r.listen(source)
    sp.speak("As you Like.. Here it is")
bh=r.recognize_google(audio)
if "date" in bh:
    os.system("date")
elif "fox" in bh:
    os.system("firefox")
elif "rome" in bh:
    print("chrome")
    os.system("google-chrome")
elif "ate" in bh:
    os.system("kate")
elif "con" in bh:
    os.system("konsole")
elif "one" in bh:
    print("1")
    
elif "one" and "num" in bh:
    
    print("1")
elif "two" in bh:
    
    print("2")
elif "three" in bh:
    print("3")
elif "four" in bh:
    print("4")
elif "five" in bh:
    print("5")
elif "six" in bh:
    print("6")
elif "seven" in bh:
    print("7")
elif "eight" in bh:

    print("8")
elif "nine" in bh:
       
    print("9")
elif "zero" in bh:
    print("0")
else:
    sp.speak("I dont understand that")
    


print("\n")




