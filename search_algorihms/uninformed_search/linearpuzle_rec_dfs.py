# Linear puzzle with recursive Depth First Search
from tree import Node

def find_solution_RecDFS(startNode, solution, visited):
    visited.append(startNode.get_data())
    if startNode.get_data() == solution:
        return startNode
    else:
        # expand successor nodes (children)
        node_data = startNode.get_data()
        child = [node_data[1], node_data[0], node_data[2], node_data[3]]
        left_child = Node(child)
        child = [node_data[0], node_data[2], node_data[1], node_data[3]]
        central_child = Node(child)
        child = [node_data[0], node_data[1], node_data[3], node_data[2]]
        right_child = Node(child)
        startNode.set_children([left_child, central_child, right_child])

        for child_node in startNode.get_children():
            if not child_node.get_data() in visited:
                # recursive call
                sol = find_solution_RecDFS(child_node, solution, visited)
                if sol != None:
                    return sol
        return None

if __name__ == "__main__":
    initial_state = [4,2,3,1]
    solution = [1,2,3,4]
    solution_node = None
    visited = []
    initial_node = Node(initial_state)
    node = find_solution_RecDFS(initial_node, solution, visited)

    # show result
    result = []
    while node.get_parent() != None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print result
        
