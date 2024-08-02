from colorama import init, Fore
import socket
import sys
import os
from banner import banner
from other import clean


def check():

    # banner

    clean()
    banner()


    # check python modules

    try:
        from colorama import init, Fore
        import requests
        from pytubefix import YouTube
    
    except ModuleNotFoundError:
        print(Fore.RED + "[!] Missing python moduless (run 'pip install -r requirements.txt')")


    print(Fore.GREEN + "[+] Check requirements" + Fore.RESET)

    # check text color compatibility

    if os.name == "nt":     # if the os is windows change the color keycodes
        init(True)

    # check connection

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect(('google.com', 443))
        s.close()

        print(Fore.GREEN + "[+] Connection OK" + Fore.RESET)

    except socket.gaierror:
        print(Fore.RED + "[!] Connection Error" + Fore.RESET)
        sys.exit()
    
    # check the download directory

    if os.path.isdir("./downloads") == False:

        try:
            os.mkdir("downloads")
            print(Fore.GREEN + "[+] 'Downloads' folder created")

        except PermissionError:
            print(Fore.RED + "[!] Error creating the 'Downloads' folder")
    
    else:
        print(Fore.GREEN + "[+] 'Downloads' folder found")

    input("\nPress enter to continue...")