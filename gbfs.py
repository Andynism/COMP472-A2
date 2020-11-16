import heuristic_node
import time
from queue import PriorityQueue

from common.priority_search import search
from common.solution_printer import print_solution_path
from common.puzzle_loader import load

def solve(heuristic, number):
    puzzles = load()
    for index, puzzle in enumerate(puzzles):
        print(puzzle.arr)
        
        first_node = heuristic_node.HeuristicNode(puzzle, heuristic)
        search_filename = f'output/{index}_gbfs-h{number}_search.txt'
        line_writer = lambda node : f'0 0 {str(node.score)} {node.state.toString()} \n'

        start_time = time.time()
        end_node = search(first_node, search_filename, line_writer, lambda x, y : False)

        solution_filename = f'output/{index}_gbfs-h{number}_solution.txt'
        print_solution_path(end_node, solution_filename, time.time()-start_time)

solve("hamming", 1)
solve("manhattan", 2)