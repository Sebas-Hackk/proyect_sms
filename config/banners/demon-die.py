# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,time,os,sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08 / 100)


logo = """\x1b[1;31m


            .                                                      .
             .n                   .                 .                  n.
       .   .dP                  dP                   9b                 9b.    .
      4    qXb         .       dX                     Xb       .        dXp     t
      dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
     9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
      9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
       `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
         `9XXXXXXXXXXXP' `9XX'   \x1b[1;33mDIE    \x1b[1;31m`98v8P'  \x1b[1;33mHUMAN   \x1b[1;31m`XXP' `9XXXXXXXXXXXP'
             ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                             )b.  .dbo.dP'`v'`9b.odb.  .dX(
                           ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                          dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                         dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                         9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                          `'      9XXXXXX(   )XXXXXXP      `'
                                   XXXX X.`v'.X XXXX
                                   XP^X'`b   d'`X^XX
                                   X. 9  `   '  P )X
                                   `b  `       '  d'
                                    `             '

\x1b[00m"""

def show():
        os.system('clear')
        slowprint(logo)

show()
