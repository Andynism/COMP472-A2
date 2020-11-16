from queue import Queue
import math

class FNode:
    def __init__(self, puzzle, heuristic, parent=None):
        self.state = puzzle
        self.parent = parent
        self.heuristic = heuristic

        if (parent is None):
            self.cost = 0
        else:
            self.cost = parent.cost + self.state.cost

        self.score = self.calculate_heuristic(heuristic) + self.cost

    def check_goal_state(self):
        return self.state.check_puzzle()

    def children(self):
        children = Queue()
        for move in self.state.allmoves():
            if move.zero is not self.state.zero:
                children.put(FNode(move, self.heuristic, self))
        return children

    def calculate_heuristic(self, heuristic):
        goal1 = [1, 2, 3, 4, 5, 6, 7, 0]
        goal2 = [1, 3, 5, 7, 2, 4, 6, 0]

        if(heuristic == "hamming"):
            score1 = self.hamming(goal1)
            score2 = self.hamming(goal2)
            return min(score1, score2)

        elif(heuristic == "manhattan"):
            score1 = self.manhattan(goal1)
            score2 = self.manhattan(goal2)
            return min(score1, score2)

        else:
            raise Exception("A heuristic must be specified.")

    def hamming(self, target):
        score = 0
        for i in range(len(self.state.arr)):
            if self.state.arr[i] != target[i]:
                score += 1
        return score

    def manhattan(self, target):
        score = 0
        for index, value in enumerate(self.state.arr):
            i2 = target.index(value)
            dx = (i2 % self.state.columns) - (index % self.state.columns)
            dy = math.floor(i2 / self.state.columns) - math.floor(index / self.state.columns)
            score += abs(dx)
            score += abs(dy)
        return score

