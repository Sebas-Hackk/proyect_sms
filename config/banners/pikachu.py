# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,time,os,sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)


logo = """\x1b[1;33m
                                                          3              
                                                       :F@@              
                                                    ,T@@@@r              
                                                  ,s7,@@@8               
                                                 Ts,  6@@                
                                              ,F; .. @@                 
                                              rF. ,, :@.                 
                                             7t  ,,.;E                   
           F@@@@#:;rrrr;:.        ,:;;;;:.  7s  ,..7F                    
           ,#@@@@r   ..:;r;r;r;rrr;;;;;;;rvHi .,.;Ci    ;7,              
              ;U@@F,,..     :rr.          .r .. vF:   :sr:7i;            
                 ,ir7Y7Yvi3T.    ........,..,,:m7    7i.   .;Y7:         
                         ;P   .,,,:,,..:. ..,,rP;  ;s;  . .   ;7l;       
                         T.tir.:::::.:r;8E ..,.,F iL   ... . ...,7Y7     
                        .vT@r8..,,:,.l8 @@r ,,, rF: . .,,...,,,,..rP;    
                        i;:@@i ;:,,,.,D@@F., ...;C ,,:::.:,:,,.;7Y;      
                       :#      7; ..,.   ;ri3;. r5 ,:,:,:,,..;L7,        
                       3Xs ..;7rrri;.,. 7U;rCP  rT ,,:,:::.:i7           
                       7@Y .,,;;;r;,,,,.;FUFXr. 5;..:,:,:.iC.            
                         ZT ..,.,...,,:,,..,;... a;.,.,.,,,;rrr:.         
                         rt;..:,,,,,,,,,,,..,,, F;777;:.,,:::;7TYr,      
                           rC;,:::::::,:,:,:,:, 7.   .7F..,;;;:;7El      
                            Zr;,;;;;;;;,:,:,:,,  L   ,7:,:;:;rT7;        
                           T;.,:.,;;;;,,,:,:,:,. 3r ir.,;;;vr:           
                           t..:.;:,:;,.r;.:,:,: 3@@rlrr;:,7C;            
                           P .,,;U ,..,Z .,:.;L.::;Y ,;rrY:;rTY7.        
                          ;@  ,.:k.., Tv .:. C7... 7    7s;;;7CX;        
                          vm. ..:6 ,,.S: ,, ;H.,,, 3v ;a7;rtL;           
                          L;s . r5.., a. ..,H;.,,,E883#6#S7,             
                         ;7 6,..7U ,.:H.  ,Pr,.:,,,.S@HF;                
                         ;Y 7ttl5;.,,,TLsLms:.:,:.. a5                   
                         ,F  ... ..,,. .:;:,,,,:.,,;U                    
                          iL. ..,::::,,,......,.,.:Z:                    
                           7#7;;;;rvTLLlvirr;::;;LP,                     
                           rvYstP#T;;,::;rivs6U5Cva                      
                         ;XY,,;ir            ,a;  ;r                     
                         5@sr;,                iLrvS                     
                                                .TFr                     
                          
\x1b[00m"""

def show():
	os.system('clear')
	slowprint(logo)

show()

