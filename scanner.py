
# Scanner Tool

# Author - Ratashi & Ghosted




print("Welcome to Scanner Tool")


import json
import urllib.request
import webbrowser
import os
try:
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
    def start():
        os.system('clear')
        print (CY+"""
             
     Scanner-Tool

    def m3():
        try:
            print(R+"""\n
            
               """+R+"""░█████╗░██╗░░░░░██╗░░░░░░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░
               """+R+"""██╔══██╗██║░░░░░██║░░░░░░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
               """+R+"""███████║██║░░░░░██║░░░░░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
               """+R+"""██╔══██║██║░░░░░██║░░░░░╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
               """+R+"""██║░░██║███████╗███████╗░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
               """+R+"""╚═╝░░╚═╝╚══════╝╚══════╝░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
               """+R+"""
               """+R+"""░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
               """+R+"""██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
               """+R+"""╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
               """+R+"""░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
               """+R+"""██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
               """+R+"""╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
                       """+W+"""╭General Idea: @Rattashi & @enesland31.py
                       """+W+"""│Developer: @Rattashi
                       """+W+"""│Version: 1.23
                       """+W+"""│Language: Python
	"""+W+"""╭──────────────┴Date: 01.12.2022
        """+Y+"""│ Options"""+G+""" >>"""+Y+"""
        """+W+"""│ 1-) Sub Page Scaning"""+Y+"""
        """+W+"""│ 2-) SQL Scanin"""+Y+"""
        """+W+"""│ 3-) XSS Scaning"""+Y+"""
        """+W+"""│ 4-) WPScaning"""+Y+"""
        """+W+"""│ 5-) Quit
""")
            ch=int(input(CY+"Seçeneği Girdiniz: "+W))
            if ch==1:
            os.system('CTRL+C')
                os.system('cd bruteforce-main')
                os.system('bash bruteforce.sh')
                main2()
                m3()
            elif ch==2:
                main()
                m3()
            elif ch==3:
                main()
                m3()
            elif ch==4:
                main()
                m3()
           elif ch==5:
                print(Y+"Çıkış................"+W)
            else:
                print(R+"\nGeçersiz!\n")
                m3()
        except ValueError:
            print(R+"\nGeçersiz!\n")
            m3()
        
    start()
    m3()
except KeyboardInterrupt:
    print(Y+"\nİYİ GÜNLER"+W)