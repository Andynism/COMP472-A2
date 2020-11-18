from common.puzzle import Puzzle


def load():
    rows = 2
    columns = 4
    puzzles = []
    counter = 0

    f = open("input/scaled_puzzles.txt", "r")
    for line in f:
        if counter==0:
            counter +=1
        elif counter%2==0:
            rows+=1
            counter+=1
        else:
            columns+=1
            counter+=1
        line = line.rstrip()
        arr = list(map(int, line.split(" ")))
        puzzles.append(Puzzle(arr, rows, columns))

    return puzzles