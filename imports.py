from os import get_terminal_size
from random import randint

YL = "\033[1;33;40m"
GR = "\033[1;32;40m"
WH = "\033[0;37;40m"


def usage(argc, argv):
    if argc == 1:
        # use random word
        return 0
    elif argc > 2:
        # too many words
        return 2
    elif argc == 2:
        if len(argv[1]) != 5:
            # word not 5 letters
            return 3
    else:
        return 0

def printc(text, tend="\n"):
    endarg = tend
    size = get_terminal_size()
    size = size[0]
    print(str(text).center(size),end=tend)

# Method to check if board is empty
class BoardMethods:
        def __init__(self, board):
            self.board = board
        
        def state(self):
            state = bool(self.board)
            return state

def quicksort(list):
    if len(list) < 2:
        return list
    low, same, high = [], [], []

    # selects pivot randomly, since list wont be too long
    pivot = list[randint(0, len(list) - 1)]

    for item in list:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)