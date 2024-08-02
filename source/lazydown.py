from colorama import Fore
from check import check
from other import clean
import banner
from dw import *


def main():

    check()
    clean()
    banner.banner()

    banner.menu()

    ch = int(input(Fore.GREEN + "\n\n LazyDown -> " + Fore.YELLOW))

    if ch == 1:
        url = input(Fore.GREEN + "\n\n YouTube url: " + Fore.YELLOW)

        clean()

        Yt(url)

if __name__ == "__main__":
    main()