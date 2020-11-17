import puzzle_node
import time

from common.priority_search import search
from common.solution_printer import print_solution_path
from common.puzzle_loader import load

puzzles = load()

for index, puzzle in enumerate(puzzles):
    print(puzzle.arr)
    
    first_node = puzzle_node.PuzzleNode(puzzle)
    search_filename = f'output50/{str(index)}_ucs_search.txt'
    line_writer = lambda node : f'0 {str(node.score)} 0 {node.state.toString()} \n'

    start_time = time.time()
    end_node = search(first_node, search_filename, line_writer, lambda x, y : False)
    
    solution_filename = f'output50/{str(index)}_ucs_solution.txt'
    print_solution_path(end_node, solution_filename, time.time()-start_time)