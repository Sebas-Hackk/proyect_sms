# bin
import time,os

azul="\x1b[1;34m"
morado=" \x1b[0;34m"
rojo="\x1b[0;31m"
exi="\x1b[00m"
error=(rojo+"Eʀʀᴏʀ...."+exi)
asep=(azul+" Asept.... "+exi)



def login():
   contra=open("/data/data/com.termux/files/usr/etc/ccontraseña.txt", "r")
   log=contra.read()
   contra.close()
   bo=True
   loog=log
   while bo==True:
      ff=input(str(" ᴾᵃˢˢʷᵒʳᵈ ⠘ "))
      if ff==loog:
         os.system("clear")
         bo=False
      else:
         print(error)
def loginn():
   try:
      login()
   except:
      os.system("clear")
      print("👻")








