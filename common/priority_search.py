from queue import PriorityQueue

def search(first_node, filename, line_writer):
    leaves = PriorityQueue()
    count=0
    # Because PriorityQueue resolves ties by comparing the next element in the tuple,
    # we also insert the "count" - which we increment each time we insert an element.
    # This breaks ties by taking the first node inserted.
    leaves.put((first_node.score, count, first_node))
    closed = list()
    f = open(filename, 'w')
    while True:
        if leaves.empty():
            f.close()
            return None
        node = leaves.get()[2]

        f.write(line_writer(node))
        if node.state.check_puzzle():
            f.close()
            return node
        elif node.state.arr not in closed:
            closed.append(node.state.arr)
            children = node.children()
            while not children.empty():
                child = children.get()
                count+=1
                leaves.put((child.score, count, child))
    