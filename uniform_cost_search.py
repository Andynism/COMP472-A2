import puzzle_node
import puzzle
from queue import PriorityQueue

def ucs(arr, rows, columns):
    node = puzzle_node.PuzzleNode(puzzle.Puzzle(arr, rows, columns))
    leaves = PriorityQueue()
    count=0
    leaves.put((node.cost, count, node))
    print(node.cost)
    closed = list()
    while True:
        if leaves.empty():
            return None
        node = leaves.get()[2]
        if node.state.check_puzzle():
            return node
        elif node.state.arr not in closed:
            closed.append(node.state.arr)
            children = node.children()
            while not children.empty():
                child = children.get()
                count+=1
                leaves.put((child.cost, count, child))

ucs([1,0,3,7,2,6,4,5], 2,4)
        