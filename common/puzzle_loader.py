from common.puzzle import Puzzle

def load():
    rows = 2
    columns = 4
    puzzles = []
    
    f = open("input/input.txt", "r")
    for line in f:
        line = line.rstrip()
        arr = list(map(int, line.split(" ")))
        puzzles.append(Puzzle(arr, rows, columns))

    return puzzles