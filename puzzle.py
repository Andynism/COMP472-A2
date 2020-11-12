class Puzzle:
    def __init__(self, arr, rows, columns):
        self.arr = arr
        self.size = len(arr)
        self.rows = rows
        self.columns = columns
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

        if(self.zero > (self.size - self.columns)):
            self.in_last_row = True
        else:
            self.in_last_row = False

    def check_puzzle(self):
        return (self.check_puzzle_1 & self.check_puzzle_2)

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
        if(not self.in_first_row):
            self.swap(self.zero - self.columns)
        
    def down(self):
        if(not self.in_last_row):
            self.swap(self.zero + self.columns)  

    def left(self):
        if(not self.in_first_col):
            self.swap(self.zero-1)

    def right(self):
        if(not self.in_last_col):
            self.swap(self.zero-1)

    def diagonal_up_left(self):   
        if(not self.in_first_row):
            if(self.in_first_col):
                self.swap(self.zero - 1)
            else :
                self.swap(self.zero - self.columns - 1)

    def diagonal_up_right(self):   
        if(not self.in_first_row):
            if(self.in_last_col):
                self.swap(self.zero - (2*self.columns - 1))
            else :
                self.swap(self.zero - self.columns + 1)

    def diagonal_down_left(self):   
        if(not self.in_last_row):
            if(self.in_first_col):
                self.swap(self.zero + (2*self.columns - 1))
            else :
                self.swap(self.zero + self.columns - 1)

    def diagonal_down_right(self):   
        if(not self.in_last_row):
            if(self.in_last_col):
                self.swap(self.zero + 1)
            else :
                self.swap(self.zero + self.columns + 1)

    def wrap(self):
        if(self.in_first_col):
            self.swap(self.zero + (self.columns - 1))
        elif(self.in_last_col):
            self.swap(self.zero - (self.columns - 1))
        
    def swap(self, new_pos):
        self.arr[self.zero], self.arr[new_pos] = self.arr[new_pos], self.arr[self.zero]
        self.zero = new_pos
        self.describe_zero()
    
    def print_puzzle(self):
        for i in range(self.size):
            if(i % self.columns == 0):
                print()
            print(self.arr[i], end = " ")
        print()

a = [1,4,7,2,5,8, 3, 6,0]
p1 = Puzzle(a, 3, 3)
print(p1.check_puzzle_2())