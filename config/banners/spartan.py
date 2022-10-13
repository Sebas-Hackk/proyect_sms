# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,time,os,sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)


logo = """\x1b[1;31m
                                     
\x1b[1;31m                                        ;;r7U8 ;X:\x1b[00m                           
\x1b[1;31m                                 ;rTS#8 a@#b@@ r@8DPEi\x1b[00m                       
\x1b[1;31m                            rU@# @@@@@@ r@8#@Z T@b@@@:,@@t:\x1b[00m                  
\x1b[1;31m                        , H@@@@@ ,@8D8@  @##@Y 5@#D@E S@@@@@E\x1b[00m                
\x1b[1;31m                     ,S@@. @@#b@3 k@##@  @@#@, C@H8@  @8##@@  @;\x1b[00m             
\x1b[1;31m                   U@@@@@@  @@#@@  @88@. H@@@  X@b@s :@bH@@  @@@8;\x1b[00m           
\x1b[1;31m                ra ;@@@Db@E  @@#@i v@b@: T@@@  E@@@  a@#@@  H@88@@S\x1b[00m          
\x1b[1;31m              :#@@8  s@@#8@r  @@@@  @@@r :@@6  #@@;  @@@@  3@8b@@; Ss\x1b[00m        
\x1b[1;31m            :D@@8#@@,  @@8@@   @@@r ;@@v  @@Y  @@#  7@@@  r@@@@S  P@@E\x1b[00m       
\x1b[1;31m          ,m@@@8D#H@@L  L@@@@  .@@@  :;             s@@  ,@@@@. .@@@@@@\x1b[00m      
\x1b[1;31m            rF@@@@8#@@6  .@@@b   ;  \x1b[1;33m:rsm@@@8@@@6Ftv:     \x1b[1;31m@@@3  L@@@@@i ,, \x1b[00m   
\x1b[1;31m               ,L8@@@@@@.  5@@   \x1b[1;33m;U@@@@@@@8@8@@@@@@@@kY,  \x1b[1;31mt:  @@@@#;  v@@. \x1b[00m   
\x1b[1;31m                   7H@@@@L    \x1b[1;33mr@@@@@@8@@@@@@@@@@@@8#8@@@@;   \x1b[1;31m@@@E   l@@@@@,\x1b[00m  
\x1b[1;31m                      ;P@@:\x1b[00m \x1b[1;33mrHkl;r3DbPv;,.   .,;iU8@@8#b@@@Y  \x1b[1;31m5   s@@@@@8Z,\x1b[00m  
                          \x1b[1;31m;;\x1b[00m       \x1b[1;33m:rrLFakPkaCi;. ,s@@8b#@@8\x1b[00m   \x1b[1;31mE@@@@a;   7U\x1b[00m
                                \x1b[1;33m:3b@@@@88#8b@@@@@Dv  ;8@8D#@@;\x1b[00m \x1b[1;31m5@L    :X@@@\x1b[00m 
                              \x1b[1;33mT@@@@8D#HD6DHHHD6#D8@@m, r@@D#8@;\x1b[00m   \x1b[1;31m ;6@@@@@@7\x1b[00m
                            \x1b[1;33m,6@@@@@@@#D6H6HkHkHkD6D#@@6  m@##@@.\x1b[00m \x1b[1;31m7@@@bFr:\x1b[00m   
                           \x1b[1;33m,Yr:    ;58@@@DDkDkHkHkHkHH#@@; s@##@@\x1b[00m  \x1b[1;31m;     :vZ#\x1b[00m
                          \x1b[1;33m;@@@@@#ar    T@@8#HDkD6D6HkHk##@l 3@##@7\x1b[00m  \x1b[1;31mC#@@@@@@@\x1b[00m
                         \x1b[1;33m7@@@b8b8@@@@a,  ;@@8DH6HkHk66D6##@r @@#@@\x1b[00m  \x1b[1;31m@@@@@D#mE\x1b[00m
                        \x1b[1;33ma@@@@@@@8bD#b@@@r  v@@HDkH6H6HkHk#8@ .@@@@\x1b[00m           
                       \x1b[1;33m@@U; .,rC@@b6DH#8@@:  @@DH6HkD66kH6#@r  r@@r\x1b[00m \x1b[1;31m.PEP#8@@#\x1b[00m
                     \x1b[1;33m,@m\x1b[00m \x1b[91m   o \x1b[00m \x1b[1;33m ;##kH6DD@@F  #@DHkHkDkDkHH@v    @s\x1b[00m \x1b[1;31m;@@@@@@@Y\x1b[00m
                    \x1b[1;33mY@;          ,k#DkH6DHb@@  X@##6HkH66k#@7    @;\x1b[00m      \x1b[1;31m.;s\x1b[00m 
                   \x1b[1;33mD@  @@@#6EP#@@@bHk6k6kHH#@@  s@8#kH6H6D8@     l\x1b[00m  \x1b[1;31m@@@@6k85\x1b[00m 
                  \x1b[1;33mb6  @@@8@@@@@88DD6666kD6H6#@@r :@@#HH6D#@a\x1b[00m         \x1b[1;31mr#@@@@,\x1b[00m 
                     \x1b[1;33mD@#6HHDHDHH6H6H6HkH6H6H6#b@P  5@@###@8\x1b[00m        \x1b[1;31m7    ;8U\x1b[00m  
                    \x1b[1;33mt@#kH6HkH6HkHkH66kDkHkHkH6DD@@v  78@@@\x1b[00m        \x1b[1;31m;@@@8Fsr\x1b[00m   
                   \x1b[1;33m;@8HHkHkH6Hk6k6kHkHk6kHk66H6DH8@@s. ;Z\x1b[00m         \x1b[1;31mS@#8@@@;\x1b[00m   
                   \x1b[1;33m@@HH6HkHk6kHkHk66H6H6DH###6HkD6##@@8X;\x1b[00m         \x1b[1;31m#@#H8@;\x1b[00m    
                  \x1b[1;33m@@HDkH6HkHkHkHkHkD6HH#b@@@@8##666DH##@6\x1b[00m         \x1b[1;31m@@H#@l\x1b[00m     
                 \x1b[1;33mZ@DHkH6Hk6kD6H6HkH6##@@@k; C@@@bHD6H6D#@;\x1b[00m        \x1b[1;31m@8#8@\x1b[00m      
                \x1b[1;33m7@##kH6HkDkH6H6D6##@@@8T      T@@@@8D#H#@@.\x1b[00m       \x1b[1;31m@@H@C\x1b[00m      
               \x1b[1;33m:@bD6H6HkDkH6HH##@@@@C,          ;C@@@@@@@@@;\x1b[00m      \x1b[1;31m@@#@s\x1b[00m      
               \x1b[1;33m@@#6H6D6#HDDbb@@@@Z;                .rFD@@@@@P.\x1b[00m    \x1b[1;31m;@@@E\x1b[00m      
             \x1b[1;33m.@@8#b#b#@@@@@@@8C;                         .;iPF,\x1b[00m    \x1b[1;31mr@@@.\x1b[00m     
             \x1b[1;33m@bXFFSS33sTr;.                                          \x1b[1;31m78@\x1b[00m                                        
                                     
\x1b[00m"""

def show():
	os.system('clear')
	slowprint(logo)

show()

