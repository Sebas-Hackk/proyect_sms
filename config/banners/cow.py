#bin/python3
from random import *
import os


lista_logos=["""
_______________
< \x1b[34mhacking-etico\x1b[00m >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\>
                ||----w |
                ||     ||

\x1b[31m[!]\x1b[00m hack --pajina_h\x1b[36m
\x1b[31m[!]\x1b[00m hack --help\x1b[36m
\x1b[31m[!]\x1b[00m exit\x1b[32m
""","""
_______________
< \x1b[33mhello-hack\x1b[00m >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\>
                ||----w |
                ||     ||

\x1b[31m[!]\x1b[00m hack --pajina_h\x1b[36m
\x1b[31m[!]\x1b[00m hack --help\x1b[36m
\x1b[31m[!]\x1b[00m exit\x1b[32m
""","""
_______________
< \x1b[31msebas-hack\x1b[00m >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\>
                ||----w |
                ||     ||

\x1b[31m[!]\x1b[00m hack --pajina_h\x1b[36m
\x1b[31m[!]\x1b[00m hack --help\x1b[36m
\x1b[31m[!]\x1b[00m exit\x1b[32m
""","""
_______________
< \x1b[32mspam-hack\x1b[00m >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\>
                ||----w |
                ||     ||

\x1b[31m[!]\x1b[00m hack --pajina_h\x1b[36m
\x1b[31m[!]\x1b[00m hack --help\x1b[36m
\x1b[31m[!]\x1b[00m exit\x1b[32m
"""]


def showv():
  muu=choice(lista_logos)
  os.system("clear")
  print(muu)






