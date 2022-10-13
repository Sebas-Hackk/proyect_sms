# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,time,os,sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 30)
logo ="""\x1b[1;31m


		        ▄▄▄▄▄▄▄▄
		  █   ▄██████████▄
		 █▐   ████████████
		 ▌▐  ██▄▀██████▀▄██
		▐┼▐  ██▄▄▄▄██▄▄▄▄██
		▐┼▐  ██████████████
		▐▄▐████─▀▐▐▀█─█─▌▐██▄
		  █████──────────▐███▌
 		 █▀▀██▄█─▄───▐─▄███▀
	 	 █  ███████▄██████
		     ██████████████
		     █████████▐▌██▌
		     ▐▀▐ ▌▀█▀ ▐ █
		           ▐    ▌\x1b[00m
\x1b[1;35m
            █▀ █▀▄▀█ █▀ ▄▄ █▀ █▀█ ▄▀█ █▀▄▀█
            ▄█ █░▀░█ ▄█ ░░ ▄█ █▀▀ █▀█ █░▀░█ 
\x1b[00m           @sebas-hack                      6/31/2022
\x1b[00m"""

def show():
        os.system('clear')
        slowprint(logo)



