import pyttsx3
import os
pyttsx3.speak("Good Morning BOSS")
print("\n")
print("Press 1 : open chrome")
print("Press 2 : open vlc")
print("\n")
print("Enter the choice:",end="")
p=input()
print(p)
if int(p)==2:
    print("VLC")
    os.system("vlc")
if int(p)==1:
    print("CHROME")
    os.system("google-chrome")
else:
    print("Not supported")

#os.system(p)
