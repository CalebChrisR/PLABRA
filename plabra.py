from imports import usage, printc, YL, GR, WH, BoardMethods, quicksort
from pynput import keyboard
import sys, os, time, random


def main():
    global used_let
    used_let = []

    # optional word from terminal
    argv = sys.argv
    argc = len(argv)
    error = usage(argc, argv)

    # if no word provided random word will be answer
    if error == 2:
        print(f"Too many arguments\nUsage: 'py {argv[0]} 'word'")
        return error
    if error == 3:
        print(f"Too many letters, only 5 letter words accepted")
        return error
   
    # if argument provided make that answer
    # error gives random word
    try: 
        answer = argv[1]
    except:
        answer = word_picker()
    
    game(answer)


def word_picker():
    f = open("lista_di_sinku.txt", "r", encoding="UTF-8")
    num_lines = sum(1 for line in open('lista_di_sinku.txt',"r", encoding="UTF-8"))
    word_id = random.randint(1, num_lines)
    content = f.readlines()
    word = content[word_id - 1]
    word = word[0:5]
    f.close()
    return word


def game(answer):
    global board 
    board = []

    # six rounds, set board correctly and take word input
    for i in range(6):
        display_board(board, answer)
        guess = guess_input(answer)
        board.append(guess)

    # correct answer in under 6 turns will end game
        if guess == answer:
            display_board(board, answer)
            i += 1
            if i == 1:
                printc(f"Congrats!, guessed in {i} round")
            else:
                printc(f"Congrats!, guessed in {i} rounds")
            
            time.sleep(2)
            break            
    else:
        display_board(board, answer)
        printc(f"Tough Luck, Word was: {answer}")
        time.sleep(2)

def display_board(board, answer):
    # clear terminal and make text white
    os.system("cls")
    print(WH)
    printc(" P  L  A  B  R  A ")
    printc("=-==-==-==-==-==-=")

    # If there are previous guesses print 
    game = BoardMethods(board)
    if game.state() == True:  
        for word in board:
            print(f"".ljust(os.get_terminal_size()[0]//2 -2),end="")
            clr_output(word, answer)

    for x in range(3): print("")

    letters = quicksort(used_let) 
    if bool(letters) != False : printc(letters)



def guess_input(answer):
    while True:
        word = input(f"".ljust(os.get_terminal_size()[0]//2 -2))

        if len(word) < 5:
            printc("Not enough letters")
            time.sleep(2)
            display_board(board, answer)
            continue
        elif len(word) > 5:
            printc("Too many letters")
            time.sleep(2)
            display_board(board, answer)
            continue

        else:
            text = open("lista_di_sinku.txt", "r", encoding="utf-8")
            
            for x in text:
                if x.strip() == word.strip():
                    text.close()
                    display_board(board, answer)
                    break
            else:
                text.close()
                printc("Word not in dictionary")
                time.sleep(2)
                display_board(board, answer)
                continue
            

        return word


def clr_output(word, answer):
    ans_let_count = let_counter(answer)
    color = {}
    
    # cycle letters to find correct color output
    # each color stored in a dictionary for some reason
    for x in range(5):
        if word[x] not in answer:
                color[x] = WH
                if word[x] not in used_let: used_let.append(word[x])
        
    for x in range(5):
        if word[x] == answer[x]:
            color[x] = GR
            ans_let_count[word[x]] -= 1
        
    for x in range(5):
        if word[x] != answer[x] and word[x] in answer:
            if ans_let_count[word[x]] > 0:
                color[x] = YL
                ans_let_count[word[x]] -= 1
            else:
                color[x] = WH
    
    # matches color with letter and print word with correct colors
    for i in range(5):
        print(color[i] + "{0}".format(word[i]), end="")
    print(WH)
    

# counts how many times letter appear in a word
# returns in a dict
def let_counter(word):
    let_count = {}
    for l in word:
        if l in let_count:
            let_count[l] += 1
        elif l not in let_count:
            let_count[l] = 1
    return let_count

if __name__ == "__main__":
    main()

