# Line Puzzle with Breadth First Search
from tree import Node

def find_sol_BFS(initial_state, solution):
    solved = False
    visited_nodes = []
    frontier_nodes = []
    startNode = Node(initial_state)
    frontier_nodes.append(startNode)
    while (not solved) and len(frontier_nodes) != 0:
        node = frontier_nodes.pop(0)
        # extract node and add it to visited
        visited_nodes.append(node)
        if node.get_data() == solution:
            # solution found
            solved = True
            return node
        else:
            # expand child nodes
            node_data = node.get_data()

            # left operator
            child = [node_data[1], node_data[0], node_data[2], node_data[3]]
            left_child = Node(child)
            if not left_child.on_list(visited_nodes) \
               and not left_child.on_list(frontier_nodes):
                frontier_nodes.append(left_child)
            # central operator
            child = [node_data[0], node_data[2], node_data[1], node_data[3]]
            central_child = Node(child)
            if not central_child.on_list(visited_nodes) \
               and not central_child.on_list(frontier_nodes):
                frontier_nodes.append(central_child)
            # right operator
            child = [node_data[0], node_data[1], node_data[3], node_data[2]]
            right_child = Node(child)
            if not right_child.on_list(visited_nodes) \
               and not right_child.on_list(frontier_nodes):
                frontier_nodes.append(right_child)

            node.set_children([left_child, central_child, right_child])

if __name__ == "__main__":
    initial_state = [4,2,3,1]
    solution = [1,2,3,4]
    solution_node = find_sol_BFS(initial_state, solution)
    # show result
    result = []
    node = solution_node
    while node.get_parent() != None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print result
