import random

rows = 2
cols = 4
for i in range (3):
    if i==0:
        pass
    elif i%2 == 1:
        rows +=1
    else:
        cols +=1
    dim = rows*cols
    puzzle = random.sample(range(dim), dim)
    listToStr = ' '.join([str(row) for row in puzzle])
    with open("scaled_puzzles.txt", "a") as txt_file:
            txt_file.write(listToStr + '\n')