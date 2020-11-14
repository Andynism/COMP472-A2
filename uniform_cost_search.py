import puzzle_node
import puzzle
import time
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
        # Write f(n) g(n) h(n) state
        # UCS does not use f(n) or h(n) so we print 0 for them
        f.write(f'0 {str(node.cost)} 0 {node.state.toString()} \n')
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

    lines = []

    node = end_node
    while node != None:
        tilemoved = 0
        # the node that was moved is the node at the position of zero in the parent
        if(node.parent != None):
            tilemoved = node.state.arr[node.parent.state.zero]
        line = f'{str(tilemoved)} {str(node.state.cost)} {" ".join(str(x) for x in node.state.arr)}'
        lines.append(line)
        node = node.parent

    lines.reverse()
    for line in lines:
        f.write(line + '\n')
    
    f.write(str(end_node.cost) + " " + str(execution_time))
    f.close()

def get_solution_path():
    pass


rows = 2
columns = 4
f = open("input/input.txt", "r")
count = 0
for x in f:
    x = x.rstrip()
    arr = list(map(int, x.split(" ")))
    print(arr)
    parent = puzzle.Puzzle(arr, rows, columns)
    start_time = time.time()
    end_node = ucs(arr, rows, columns, count)
    print_solution_path(parent, end_node, count, time.time()-start_time)
    count += 1
f.close()
