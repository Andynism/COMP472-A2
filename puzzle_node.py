from queue import Queue
from copy import deepcopy

class PuzzleNode:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent

        if (parent is None):
            self.cost = 0
            self.moves = move
        else: 
            self.cost = parent.cost + self.state.cost
            self.moves = parent.moves + move

    def check_goal_state(self):
        return self.state.check_puzzle()
    
    def children(self):
        children = Queue()
        for move in self.state.possible_moves:
            copy = deepcopy(self.state)
            copy.do_move(move)
            if copy.zero is not self.state.zero:
                children.put(PuzzleNode(copy, self, move))
        return children