import subprocess
import os
import getpass
inpass=getpass.getpass("Enter the password:")
apass="lw"
if inpass !=  apass:
    print("Password incorrct")
    exit()

cmd=input("Enter the command:")
x=subprocess.getstatusoutput(cmd)

status=x[0]
output=x[1]
if status==0:
   print(output)
else:
   print("cmd failture..")

   
   
