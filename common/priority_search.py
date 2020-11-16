from queue import PriorityQueue

def search(first_node, filename, line_writer, should_revisit):
    leaves = PriorityQueue()
    count=0
    # Because PriorityQueue resolves ties by comparing the next element in the tuple,
    # we also insert the "count" - which we increment each time we insert an element.
    # This breaks ties by taking the first node inserted.
    leaves.put((first_node.score, count, first_node))
    closed = {}
    f = open(filename, 'w')
    while True:
        if leaves.empty():
            f.close()
            return None
        node = leaves.get()[2]

        if node.state.toString() not in closed or should_revisit(node, closed[node.state.toString()]):
            f.write(line_writer(node))
            if node.state.check_puzzle():
                f.close()
                return node
            closed[node.state.toString()] = node.cost
            children = node.children()
            while not children.empty():
                child = children.get()
                count+=1
                leaves.put((child.score, count, child))
    