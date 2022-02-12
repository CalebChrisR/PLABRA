import random, os, time

YL = "\033[1;33;40m"
GR = "\033[1;32;40m"
WH = "\033[0;37;40m"

board = [
        [], [], [], [], [], []
        ]

def main():

    game_over = False
    num_lines = sum(1 for line in open('lista_di_sinku.txt',"r", encoding="UTF-8"))
    word_id = random.randint(0, num_lines)
    f = open("lista_di_sinku.txt", "r", encoding="UTF-8")
    content = f.readlines()
    word = content[word_id - 1]
    print(word)
    time.sleep(1)

    while game_over == False:
        init_board()
        time.sleep(1)
        game_over = True


def txt_res():
    print(WH)

def init_board():
    os.system("cls")
    print(" P  L  A  B  R  A ")

    for i in range(6):
        print("=-=", end="")
    print()
    #print("|{}||{}||{}||{}||{}||{}|".format(" ", " ", " ", " ", " ", " "))

def test():
    word = "papel"
    gameover = False

    let_count = {}
    #TODO count letters for words with repeating letters

    while gameover == False:
        guess = str(input("What word?: "))

        for i in range(5):
            if guess[i] not in word:
                print(guess[i] + WH, end="")
                continue
            if guess[i] == word[i]:
                print(GR + guess[i] + WH, end="")
                continue
            if guess[i] in word:
                print(YL + guess[i] + WH, end="")
                continue
        if guess == word:
            print("\nCorrect!")
            gameover = True
            break
        print()           



if __name__ == "__main__":
    txt_res()
    #main()	
    test()
    txt_res()