# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,time,os,sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)


logo = """\x1b[0m
                           
                            .:::!~!!!!!:.
                        .xUHWH!! !!?M88WHX:.
                      .X*#M@$!!  !X!M$$$$$$WWx:.
                     :!!!!!!?H! :!$!$$$$$$$$$$8X:
                    !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                   :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                   ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                     !:~~~ .:!MST#$$$$WX??#MRRMMM!
                     ~?WuxiW*`   `√#$$$$8!!!!??!!!
                   :X- M$$$$       `rT#$T~!8$WUXU~
                  :%`  ~#$$$m:   \x1b[91m o \x1b[00m  ~!~ ?$$$$$$
                :!`.-   ~T$$$$8xx.  .xWW- ~x$$$$$
     .......   -~~:<` !    ~?T#$$@@W@*?$$ \x1b[91m  o \x1b[00m /`
    C |W$@@M!!! .!~~ !!     .:XUW$W!~ `$~:    :
    Y |#$~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
    B |:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
    E |.~~   :X@!.-~   ?@WTWo(`*$$$W$TH$! `
    R |Wi.~!X$?!-~    : ?$$$B$Wu(`**$RM!
       .......         :   ~$$$$$B$$en:``
                          ~`##*$$$$M~
                          "
\x1b[00m"""

def show():
	os.system('clear')
	slowprint(logo)

show()



