class Puzzle2:
    def __init__(self, arr, rows=2, columns=4, cost=0):
        self.arr = arr
        self.size = len(arr)
        self.rows = rows
        self.columns = columns
        self.cost = cost
        self.find_zero()

    def find_zero(self):
        for i in range(0, self.size):
            if (self.arr[i] == 0):
                self.zero = i
        self.describe_zero()

    def describe_zero(self):
        if(self.zero % self.columns == 0):
            self.in_first_col = True
        else:
            self.in_first_col = False

        if(self.zero % self.columns == self.columns-1):
            self.in_last_col = True
        else:
            self.in_last_col = False

        if(self.zero < self.columns):
            self.in_first_row = True
        else:
            self.in_first_row = False

        if(self.zero >= (self.size - self.columns)):
            self.in_last_row = True
        else:
            self.in_last_row = False

    def check_puzzle(self):
        return (self.check_puzzle_1() or self.check_puzzle_2())

    def check_puzzle_1(self):
        count = 1
        for i in range(self.size-1):
            if(self.arr[i] != count):
                return False
            count += 1
        return True

    def check_puzzle_2(self):
        row_count = 1
        col_count = 1
        count = 1
        for i in range(self.size-1):
            if(self.arr[i] != count):
                return False
            
            if(col_count % self.columns == 0):
                col_count = 1
                row_count += 1
                count = row_count
            else:
                col_count += 1
                count += self.rows
        return True   
    
    def up(self):
        target = (self.zero - self.columns)
        cost = 1
        if(target < 0):
            target = target % len(self.arr)
            cost = 2
        return self.swap(target, cost)
        
    def down(self):
        target = (self.zero + self.columns)
        cost = 1
        if(target > len(self.arr)):
            target = target % len(self.arr)
            cost = 2
        return self.swap(target, cost)

    def left(self):
        target = self.zero - 1
        cost = 1
        if(self.in_first_col):
            target = target + self.columns
            cost = 2
        return self.swap(target, cost)

    def right(self):
        target = self.zero + 1
        cost = 1
        if(self.in_last_col):
            target = target - self.columns
            cost = 2
        return self.swap(target, cost)
        
    def swap(self, new_pos, cost):
        arr = self.arr.copy()
        arr[self.zero], arr[new_pos] = arr[new_pos], arr[self.zero]
        return Puzzle2(arr, self.rows, self.columns, self.cost + cost)
    
    def corner(self):
        if(self.in_first_row & self.in_first_col):
            target1 = self.zero + 1 + self.columns
            target2 = len(self.arr) - 1
            return [self.swap(target1, 3), self.swap(target2, 3)]
        
        if(self.in_first_row & self.in_last_col):
            target1 = self.zero - 1 + self.columns
            target2 = len(self.arr) - self.columns
            return [self.swap(target1, 3), self.swap(target2, 3)]

        if(self.in_last_row & self.in_first_col):
            target1 = self.zero + 1 - self.columns
            target2 = self.columns - 1
            return [self.swap(target1, 3), self.swap(target2, 3)]

        if(self.in_last_row & self.in_last_col):
            target1 = self.zero - 1 - self.columns
            target2 = 0
            return [self.swap(target1, 3), self.swap(target2, 3)]

    def print_puzzle(self):
        for i in range(self.size):
            if(i % self.columns == 0):
                print()
            print(self.arr[i], end = " ")
        print()

    def allmoves(self):
        moves = [
            self.up(),
            self.down(),
            self.left(),
            self.right()
        ]
        moves.extend(self.corner())
        return moves