import heuristic_node
import puzzle
import time
from queue import PriorityQueue

def gbfs(arr, rows, columns, filename, heuristic):
    node = heuristic_node.HeuristicNode(puzzle.Puzzle(arr, rows, columns), heuristic)
    leaves = PriorityQueue()
    count=0
    # Because PriorityQueue resolves ties by comparing the next element in the tuple,
    # we also insert the "count" - which we increment each time we insert an element.
    # This breaks ties by taking the first node inserted.
    leaves.put((node.score, count, node))
    closed = list()
    f = open(filename, 'w')
    while True:
        if leaves.empty():
            f.close()
            return None
        node = leaves.get()[2]
        # Write f(n) g(n) h(n) state
        # GBFS does not use f(n) or g(n) so we print 0 for them
        f.write(f'0 0 {str(node.score)} {node.state.toString()} \n')
        if node.state.check_puzzle():
            f.close()
            return node
        elif node.state.arr not in closed:
            closed.append(node.state.arr)
            children = node.children()
            while not children.empty():
                child = children.get()
                count+=1
                leaves.put((child.score, count, child))
    
def print_solution_path(puzzle, end_node, filename, execution_time):
    count = 0
    f = open(filename, "w")

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

def solve(heuristic, number):
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
        end_node = gbfs(arr, rows, columns, f'output/{count}_gbfs-h{number}_search.txt', heuristic)
        print_solution_path(parent, end_node, f'output/{count}_gbfs-h{number}_solution.txt', time.time()-start_time)
        count += 1
    f.close()

solve("hamming", 1)
solve("manhattan", 2)