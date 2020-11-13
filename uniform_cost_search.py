import puzzle_node
import puzzle
from queue import PriorityQueue

def ucs(arr, rows, columns, file_count):
    node = puzzle_node.PuzzleNode(puzzle.Puzzle(arr, rows, columns))
    leaves = PriorityQueue()
    count=0
    leaves.put((node.cost, count, node))
    closed = list()
    f = open('output/'+ str(file_count) +'_ucs_search.txt', 'w')
    while True:
        if leaves.empty():
            f.close()
            return None
        node = leaves.get()[2] 
        f.write(str(node.cost+node.state.cost) + " " + str(node.cost) + " " + str(node.state.cost) + " " + " ".join(str(x) for x in node.state.arr) + "\n")
        if node.state.check_puzzle():
            f.close()
            return node
        elif node.state.arr not in closed:
            closed.append(node.state.arr)
            children = node.children()
            while not children.empty():
                child = children.get()
                count+=1
                leaves.put((child.cost, count, child))
    
def print_solution_path(puzzle, end_node, file_count, execution_time):
    count = 0
    f = open("output/"+ str(file_count) + "_ucs_solution.txt", "w")
    f.write(str(count) + " " + str(puzzle.cost) + " " + " ".join(str(x) for x in puzzle.arr) + "\n")
    for i in range(len(end_node.moves)):
        puzzle.do_move(end_node.moves[i])
        count += 1
        f.write(str(count) + " " + str(puzzle.cost) + " " +" ".join(str(x) for x in puzzle.arr) + "\n")
    f.write(str(end_node.cost) + " " + str(execution_time))
    f.close()


rows = 2
columns = 4
f = open("input/input.txt", "r")
count = 0
for x in f:
    x = x.rstrip()
    arr = list(map(int, x.split(" ")))
    print(arr)
    parent = puzzle.Puzzle(arr, rows, columns)
    end_node = ucs(arr, rows, columns, count)
    print_solution_path(parent, end_node, count, 1)
    count += 1
f.close()
