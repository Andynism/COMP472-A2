import f_node
import time

from common.priority_search import search
from common.solution_printer import print_solution_path
from common.puzzle_loader import load

def solve(heuristic, number):
    puzzles = load()
    for index, puzzle in enumerate(puzzles):
        print(puzzle.arr)

        first_node = f_node.FNode(puzzle, heuristic)
        search_filename = f'output/{index}_astar-h{number}_search.txt'
        line_writer = lambda node: f'{str(node.score)} {str(node.cost)} {str(node.calculate_heuristic(heuristic))} {node.state.toString()} \n'

        start_time = time.time()
        end_node = search(first_node, search_filename, line_writer, lambda node, previousCost: node.cost < previousCost)

        solution_filename = f'output/{index}_astar-h{number}_solution.txt'
        print_solution_path(end_node, solution_filename, time.time() - start_time)

solve("hamming", 1)
solve("manhattan", 2)
solve("naive", 3)