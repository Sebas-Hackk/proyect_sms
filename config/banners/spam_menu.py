import socket,struct,time,os,sys
from random import *
def slowprint(s):
   for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 200)



logos="""\x1b[36m
      █████████████████████
    ████▀                 ▀████
  ███▀                       ▀███
 ██▀                           ▀██
█▀                               ▀█
█                                 █
█  \x1b[31m █████\x1b[00m                \x1b[31m █████\x1b[00m   █
█  \x1b[31m██▓▓▓███\x1b[00m             \x1b[31m███▓▓▓██\x1b[00m  █
█  \x1b[31m██▓▓▓▓▓██\x1b[00m           \x1b[31m██▓▓▓▓▓██\x1b[00m  █
█  \x1b[31m██▓▓▓▓▓▓██\x1b[00m         \x1b[31m██▓▓▓▓▓▓██\x1b[00m  █
█▄  \x1b[31m████▓▓▓▓██\x1b[00m       \x1b[31m██▓▓▓▓████ \x1b[00m ▄█
▀█▄   \x1b[31m▀███▓▓▓██\x1b[00m     \x1b[31m██▓▓▓███▀\x1b[00m   ▄█▀
  █▄    \x1b[31m▀█████▀\x1b[00m     \x1b[31m▀█████▀\x1b[00m    ▄█
 ▄██           \x1b[31m▄█ █▄\x1b[00m           ██▄
 ███           \x1b[31m██ ██\x1b[00m           ███
 ███                           ███   \x1b[31m[!]\x1b[00m hack --help\x1b[36m
   ▀██  ██▀██  █  █  █  ██▀██  ██▀   \x1b[31m[!]\x1b[00m hack --pajina_h\x1b[36m
   ▀████▀ ██  █  █  █  ██ ▀████▀     \x1b[31m[!]\x1b[00m exit\x1b[36m
    ▀██▀  ██  █  █  █  ██  ▀██▀
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
          ██  █  █  █  ██
           █▄▄█▄▄█▄▄█▄▄█
\x1b[00m

"""
def showv():
        os.system('clear')
        slowprint(logos)




