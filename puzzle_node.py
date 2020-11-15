from queue import Queue

class PuzzleNode:
    def __init__(self, puzzle, parent=None):
        self.state = puzzle
        self.parent = parent

        if (parent is None):
            self.cost = 0
        else: 
            self.cost = parent.cost + self.state.cost

    def check_goal_state(self):
        return self.state.check_puzzle()
    
    def children(self):
        children = Queue()
        for move in self.state.allmoves():
            if move.zero is not self.state.zero:
                children.put(PuzzleNode(move, self))
        return children