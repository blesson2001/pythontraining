import pyttsx3
import os
pyttsx3.speak("Good Morning BOSS")
print("\n")
#print("Press 1 : open chrome")
#print("Press 2 : open vlc")
print("\n")
print("Chat me the requirement:",end="")
p=input()
print(p)
#if int(p)==2:
#    print("VLC")
#    os.system("vlc")
#if int(p)==1:
#    print("CHROME")
#    os.system("google-chrome")
#else:
#    print("Not supported")

#os.system(p)
#if "launch" in  p and "vlc" in p:
#    os.system("vlc")
#if "launch" in  p and "chrome" in  p:
#    os.system("google-chrome")
if (("run" in p) or ("launch" in p)) and (("player" in p) or ("vlc" in p)):
    os.system("vlc")
if (("run" in p) or ("launch" in p)) and (("firefox" in p) or ("fox" in p)):
    os.system("firefox")
else:
    print("Not supported")


