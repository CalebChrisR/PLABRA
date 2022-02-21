# main.py
from imports import usage
import sys, os

YL = "\033[1;33;40m"
GR = "\033[1;32;40m"
WH = "\033[0;37;40m"

def main():
    argv = sys.argv
    argc = len(argv)

    # error handler, for correct usage
    error = usage(argc, argv)
    if error != 0:
        if error == 1:
            print(f"No arguments provided\nUsage: 'py {argv[0]} 'word'")
        if error == 2:
            print(f"Too many arguments\nUsage: 'py {argv[0]} 'word'")
        if error == 3:
            print(f"Too many letters, only 5 letter words accepted")
    else:
        # error code 0, so keep going lol
        pass
    
    game_init()
    game()

def game_init():
    print(WH)
    os.system("cls")
    print(" P  L  A  B  R  A ")

    for i in range(6):
        print("=-=", end="")
    print()

def game():
    

if __name__ == "__main__":
    main()