from pytubefix import YouTube
from colorama import Fore
import threading
import time
import banner
from moviepy.editor import *


def Yt(url: str):

    banner.youtube()

    loading = ['/', '-', '\\', '|']

    # check link url validity

    if url.startswith("https://www.youtube.com/watch?v=") == False and url.startswith("https://youtu.be/") == False:

        print(Fore.RED + "[!] Invalid YouTube url" + Fore.RESET)

    else:

        yt = YouTube(url)

        print(Fore.GREEN + "[+] Title: " + Fore.YELLOW + yt.title + Fore.RESET)
        print(Fore.GREEN + "[+] Author: " + Fore.YELLOW + yt.author + Fore.RESET)
        print(Fore.GREEN + "[+] Published date: " + Fore.YELLOW +  yt.publish_date.strftime("%Y-%m-%d") + Fore.RESET)
        print(Fore.GREEN + "[+] Views: " + Fore.YELLOW + str(yt.views) + Fore.RESET)
        print(Fore.GREEN + "[+] Lenght: " + Fore.YELLOW + str(yt.length) + Fore.RESET)
        print(Fore.GREEN + "\n\n[+] 1. Download video\n[+] 2. Download audio" + Fore.RESET)

        ch = None

        while ch != 1 and ch != 2:
            ch = int(input(Fore.GREEN + "\n\nLazyDown -> " + Fore.YELLOW))

            if ch != 1 and ch != 2:
                print(Fore.RED + "\n[!] Invalid choice")

        print("\n")

        if ch == 1:
        # select resolution

            resolutions = []

            for rs in yt.streams:
                if rs.resolution not in resolutions and rs.resolution != None:
                    resolutions.append(rs.resolution)

            for i in resolutions:
                resolutions[resolutions.index(i)] = int(resolutions[resolutions.index(i)][:-1])

            resolutions.sort(reverse=True)

            for i in resolutions:
                print(Fore.GREEN + "[+] " + str(i) + Fore.RESET)


            res = None

            while res not in resolutions:
                res = int(input(Fore.GREEN + "\n\n[+] Enter a Resolution: " + Fore.YELLOW))

                if res not in resolutions:
                    print(Fore.RED + "\n[!] Invalid resolution")

            res = str(res) + 'p'

            print("\n")

        try:

            if ch == 1:
                th = threading.Thread(target=yt.streams.filter(res=res).first().download, args=("./downloads",))

            else:
                th = threading.Thread(target=yt.streams.filter(only_audio=True).first().download, args=("./downloads",))

            th.start()

            i = 0

            while th.is_alive():

                if ch == 1:
                    print(Fore.GREEN + "[" + loading[i] + "] Downloading the video" + Fore.RESET, end="\r")
                
                else:
                    print(Fore.GREEN + "[" + loading[i] + "] Downloading the audio" + Fore.RESET, end="\r")

                i+=1

                if i == 4:
                    i = 0

                time.sleep(0.5)

            if ch == 1:
                print(Fore.GREEN + "[+] Video Downloaded         " + Fore.RESET)

            else:
                file_name = './downloads/' + yt.streams.first().default_filename
                fl = AudioFileClip(file_name)
                fl.write_audiofile(file_name.replace('mp4', 'mp3'), logger=None)
                fl.close()
                os.remove(file_name)

                print(Fore.GREEN + "[+] Audio Downloaded         \n" + Fore.RESET)


        except OSError:

            if ch == 1:
                print(Fore.RED + "[!] Error downloading the YouTube video")
            
            else:
                print(Fore.RED + "[!] Error downloading the YouTube audio")
