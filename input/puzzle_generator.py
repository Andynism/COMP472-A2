import random

for i in range (50):
    puzzle = random.sample(range(8), 8)
    listToStr = ' '.join([str(row) for row in puzzle])
    with open("50_puzzles.txt", "a") as txt_file:
            txt_file.write(listToStr + '\n')