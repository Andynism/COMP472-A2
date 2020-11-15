from queue import Queue

class HeuristicNode:
    def __init__(self, puzzle, heuristic, parent=None):
        self.state = puzzle
        self.parent = parent
        self.heuristic = heuristic

        self.score = calculate_heuristic(heuristic)

    def check_goal_state(self):
        return self.state.check_puzzle()

    def children(self):
        children = Queue()
        for move in self.state.allmoves():
            if move.zero is not self.state.zero:
                children.put(HeuristicNode(move, self))
        return children

    def calculate_heuristic(self, heuristic):
        goal1 = [1, 2, 3, 4, 5, 6, 7, 0]
        goal2 = [1, 3, 5, 7, 2, 4, 6, 0]

        if(heuristic == "hamming"):
            score1 = hamming(goal1)
            score2 = hamming(goal2)
            return min(score1, score2)

        if(heuristic == "manhattan"):
            score1 = manhattan(goal1)
            score2 = manhattan(goal2)
            return min(score1, score2)

    def hamming(self, target):
        score = 0
        for i in len(self.state.arr):
            if self.state.arr[i] != target[i]:
                score += 1
        return score

    def manhattan(self, target):
        score = 0
        for index, value in enumerate(self.state.arr):
            i2 = target.index(value)
            dx = (i2 % self.state.columns) - (index % self.state.columns)
            dy = (i2 / self.state.columns) - (index / self.state.columns)
            score += dx
            score += dy
        return score

