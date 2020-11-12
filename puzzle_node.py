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
        succs = Queue()
        for move in self.state.moves:
            p = deepcopy(self.state)
            p.do_move(move)
            if p.zero is not self.state.zero:
                succs.put(PuzzleNode(p, self, move))
        return children