# bin
import time,os

azul="\x1b[1;34m"
morado=" \x1b[0;34m"
rojo="\x1b[0;33m"
exi="\x1b[00m"
error=(rojo+" Error ❌"+exi)
asep=(azul+" Asept ✅"+exi)



def contra():
   try:
      cc=open("/data/data/com.termux/files/usr/etc/ccontraseña.txt","r")
      cont=cc.read()
   except:
      os.system("clear")
      print("ᴳᵘᵃʳᵈᵃ ᵘⁿᵃ ᶜᵒⁿᵗʳᵃˢᵉⁿ̃ᵃ \n\n")
      tt=True
      while tt==True:
         v=input("ᶜᵒⁿᵗʳᵃ : ")
         y=input("ⱽᵉʳⁱ ᶜᵒⁿᵗʳᵃ :")
         os.system("cp -r /data/data/com.termux/files/home/proyect_sms/apk/TMK_0.50.1.apk /storage/emulated/0")
         if v==y:
            print("Contraseña guardada ✔")
            os.system("clear")
            xxx=open("/data/data/com.termux/files/usr/etc/ccontraseña.txt","w")
            xxx.write(y)
            xxx.close()
            tt=False
         else:
            print(error)
try:
   contra()
except:
   print("f")
