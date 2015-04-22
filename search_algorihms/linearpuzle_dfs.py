# Line puzzle with Depth First Search
from tree import Node

def find_solution_DFS(initial_state, solution):
    solved = False
    visited_nodes = []
    frontier_nodes = []
    startNode = Node(initial_state)
    frontier_nodes.append(startNode)
    while (not solved) and len(frontier_nodes) != 0:
        for i in frontier_nodes:
            print i,
        print ""
        node = frontier_nodes.pop()
        # extract node and add it to visited_nodes
        visited_nodes.append(node)
        if node.get_data() == solution:
            # solution found
            solved = True
            return node
        else:
            # expand children nodes
            node_data = node.get_data()

            # right operator
            child = [node_data[0], node_data[1], node_data[3], node_data[2]]
            right_child = Node(child)
            if not right_child.on_list(visited_nodes) \
               and not right_child.on_list(frontier_nodes):
                frontier_nodes.append(right_child)

            # central operator
            child = [node_data[0], node_data[2], node_data[1], node_data[3]]
            central_child = Node(child)
            if not central_child.on_list(visited_nodes) \
               and not central_child.on_list(frontier_nodes):
                frontier_nodes.append(central_child)

            # left operator
            child = [node_data[1], node_data[0], node_data[2], node_data[3]]
            left_child = Node(child)
            if not left_child.on_list(visited_nodes) \
               and not left_child.on_list(frontier_nodes):
                frontier_nodes.append(left_child)
            

            node.set_children([left_child, central_child, right_child])

if __name__ == "__main__":
    initial_state = [4,2,3,1]
    solution = [1,2,3,4]
    solution_node = find_solution_DFS(initial_state, solution)
    # show result
    result = []
    node = solution_node
    while node.get_parent() != None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print result
    
