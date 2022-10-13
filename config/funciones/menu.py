#v/home/bin

#File: spam-sms
#Author: sebas-hack
#Description: Simple code python
import os,time
def usoo():
   os.system("clear")
   uso="""

usage:

          hack--spam [spam]
          hack--list [Numeros a los que as echo spam]
          hack--help [Usage]
          hack--nk [pajina de ayuda]
          hack--ch [guarda numeros]
          hack--hc [muestra numeros guardados]
          hack--spamtt [spam mas de un numero]


"""
   print(uso)

#ffejjejdbdbdbsnwnwsjjxbdbwbwvwvbwbsbsvdvwvwbwjs



azul="\x1b[1;34m"
morado=" \x1b[0;34m"
rojo="\x1b[0;31m"
exi="\x1b[00m"
error=(rojo+"Eʀʀᴏʀ...."+exi)
asep=(azul+" Asept.... "+exi)


menu=["[¡] ᴹᵉⁿᵘ ","[¡]","[¡]","[¡]"]

def menuu():
   logo="""
        7/1/2022
\x1b[0;31m	█▀ █▀█ ▄▀█ █▀▄▀█ ▄▄ █▀ █▀▄▀█ █▀
	▄█ █▀▀ █▀█ █░▀░█ ░░ ▄█ █░▀░█ ▄█\x1b[00m

  ⁾‧‧‧‧‧‧‧‧ ⁽⁺⁾ ᴬᵘᵗʰᵒʳ⠘ \x1b[1;34mˢᵉᵇᵃˢ⁻ʰᵃᶜᵏ\x1b[00m ⁽⁺⁾‧‧‧‧‧‧‧‧⁽
      ⁾‧‧‧‧‧⁽⁺⁾ ᶠⁱˡᵉ⠘   \x1b[1;34mˢᵖᵃᵐ⁻ˢᵐˢ\x1b[00m   ⁽⁺⁾‧‧‧‧‧‧⁽


\x1b[0;31m[!]\x1b[00m hack--help
\x1b[0;31m[!]\x1b[00m hack--ch

"""
   print(logo)




def funcioness():

   xc=True
   while xc==True:


      menf=input("""\x1b[1;35m┌──⁽\x1b[00m\x1b[0;35mᶜᵃᶻᵃᵖᵘᵗᵃˢ\x1b[00m㉿\x1b[0;35mˡᵒᶜᵃˡʰᵒˢᵗ\x1b[00m\x1b[1;35m⁾⁻[~]
└─>\x1b[00m """)
      #ayudaa

      if menf=="hack--help":
         usoo()




      #ayudaaa

      elif menf=="hack--ch":
         os.system("clear")
         os.system("termux-open-url https://www.facebook.com/profile.php?id=100083158914028")
         menuu()

      # spamᴺᵘᵐᵉʳᵒ
      elif menf=='hack--spam':
         xc=False
         os.system('clear')

         try:
            num=input('ᴺᵘᵐᵉʳᵒ : ')
         except:
            print("Error, Ingresa numero entero /n/n")
            num=input('ᴺᵘᵐᵉʳᵒ : ')

            men=input('ᴹᵉⁿˢᵃʲᵉ : ')
            mkk='''

    INFORMATION
   ---------------------
   Mensaje: {}
   Numero: {}
   ---------------------

\x1b[1;32m[¡]\x1b[00m ᴿᵘⁿ
\x1b[1;32m[¡]\x1b[00m ᶜᵃⁿˢᵉˡᵃʳ

    \n'''.format(men,num)

         os.system('clear')
         print(mkk)
         xxcc=True
         while xxcc==True:
            iniciar=input("""\x1b[1;35m┌──⁽\x1b[00m\x1b[0;35mᶜᵃᶻᵃᵖᵘᵗᵃˢ\x1b[00m㉿\x1b[0;35mˡᵒᶜᵃˡʰᵒˢᵗ\x1b[00m\x1b[1;35m⁾⁻[~]
└─>\x1b[00m """)
            if "canselar" in iniciar:
               xxcc+=False
               os.system('python3  /storage/emulated/0/proyect_sms/config/funciones/menu2.py')

            elif iniciar=="run":
               xxcc+=False
               guardar_num=open("/data/data/com.termux/files/home/proyect_sms/config/ppfff.txt", "w")
               guardar_num.write(num)
               guardar_num.close()
               tech="termux-sms-send -n "+num+" " +men
               cantidad=int(input("ᶜᵃⁿᵗⁱᵈᵃᵈ ᵈᵉ ᵐᵉⁿˢᵃʲᵉˢ : "))
               os.system("clear")
               for x in range(cantidad):
                  print("\x1b[0;34m[\x1b[00m"+str(x)+"\x1b[0;34m]\x1b[00m enviado con exito ........................")
                  os.system(tech)
                  time.sleep(1)
                  os.system("clear")
                  print('ˢᵖᵃᵐ ᵗᵉʳᵐⁱⁿᵃᵈᵒ')



      else:
         print(rojo,"[!!]\x1b[00m ᴬʳᵍᵘᵐᵉⁿᵗᵒ ⁿᵒ ᵛᵃˡⁱᵈᵒ")
         time.sleep(1)
         os.system("clear")
         menuu()




