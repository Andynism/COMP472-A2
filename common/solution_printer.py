def print_solution_path(end_node, filename, execution_time):
    count = 0
    f = open(filename, "w")

    lines = []

    node = end_node
    while node != None:
        tilemoved = 0
        # the node that was moved is the node at the position of zero in the parent
        if(node.parent != None):
            tilemoved = node.state.arr[node.parent.state.zero]
        line = f'{str(tilemoved)} {str(node.state.cost)} {" ".join(str(x) for x in node.state.arr)}'
        lines.append(line)
        node = node.parent

    lines.reverse()
    for line in lines:
        f.write(line + '\n')
    
    f.write(str(end_node.cost) + " " + str(execution_time))
    f.close()