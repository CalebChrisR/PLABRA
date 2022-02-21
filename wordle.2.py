# main.py
from imports import usage, printc
import sys, os, time

YL = "\033[1;33;40m"
GR = "\033[1;32;40m"
WH = "\033[0;37;40m"

class BoardMethods:
        def __init__(self, board):
            self.board = board
        
        def state(self):
            state = bool(self.board)
            return state

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
    
    game(argv[1])

def game_init(board):
    m_board = BoardMethods(board)
    size = os.get_terminal_size()
    size = size[0]
    print(WH)
    os.system("cls")
    printc(" P  L  A  B  R  A ")
    printc("=-==-==-==-==-==-=")
    if m_board.state() == True:
        for w in board:
            printc(w)
    
def game(answer):
    word = answer
    global board 
    board = []

    for i in range(6):
        game_init(board)
        word = word_input(i)
        board.append(word)
        if word == answer:
            game_init(board)
            i += 1
            if 1 == 1:
                printc(f"Congrats!, guessed in {i} round")
            else:
                printc(f"Congrats!, guessed in {i} rounds")
            break            
    else:
        game_init(board)
        printc(f"Tough Luck, Word was: {word}")

def word_input(i):
    while True:
        word = input(f"".ljust(os.get_terminal_size()[0]//2 -2))
        
        if len(word) != 5:
            printc("Word must contain 5 letters")
            time.sleep(2)
            game_init(board)
            continue
        else:
            text = open("lista_di_sinku.txt", "r", encoding="utf-8")
            
            for x in text:
                if x.strip() == word.strip():
                    text.close()
                    game_init(board)
                    break
            else:
                text.close()
                printc("Not valid word")
                time.sleep(2)
                game_init(board)
                continue
            

        return word

if __name__ == "__main__":
    main()