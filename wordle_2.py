# main.py
from imports import usage, printc
import sys, os, time, random

YL = "\033[1;33;40m"
GR = "\033[1;32;40m"
WH = "\033[0;37;40m"

# Method to check if board is empty
class BoardMethods:
        def __init__(self, board):
            self.board = board
        
        def state(self):
            state = bool(self.board)
            return state

def main():
    # take word from cmd as the answer
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
            # TODO colored word output
            #word_out(w)
    
def game(answer):
    word = answer
    global board 
    board = []

    # set board, check correct user input, add to board if good
    for i in range(6):
        game_init(board)
        word = word_input()
        board.append(word)

        # correct answer in 6 turns will end game
        if word == answer:
            game_init(board)
            i += 1
            if i == 1:
                printc(f"Congrats!, guessed in {i} round")
            else:
                printc(f"Congrats!, guessed in {i} rounds")
            break            
    else:
        game_init(board)
        printc(f"Tough Luck, Word was: {answer}")

def word_input():
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

def word_pick():
    num_lines = sum(1 for line in open('lista_di_sinku.txt',"r", encoding="UTF-8"))
    word_id = random.randint(0, num_lines)
    f = open("lista_di_sinku.txt", "r", encoding="UTF-8")
    content = f.readlines()
    word = content[word_id - 1]
    word = word[0:5]
    f.close()
    return word

def word_out(word):
    let_count = let_counter(word)
    
    pass

def let_counter(word):
    let_count = {}
    for l in word:
        if l in let_count:
            let_count[l] += 1
        elif l not in let_count:
            let_count[l] = 1
    return let_count

def answer_check(guess, word, counter):
    for x in guess:
        index = guess.find(x)
        if x not in word:
            print(f"{x}",end="")
        if counter[x] > 0:
            counter[x] -= 1




def main2():
    let_count = let_counter('karni')
    guess = 'karni'
    word = 'abeha'
    answer_check(guess, word, let_count)




if __name__ == "__main__":
    main()
    #main2()