# Linear Puzzle with heuristic
from tree import Node

def find_heuristic_solution(start_node, solution, visited):
    visited.append(start_node.get_data())
    if start_node.get_data() == solution:
        return start_node
    else:
        # expand successor nodes (children)
        node_data = start_node.get_data();
        child = [node_data[1], node_data[0], node_data[2], node_data[3]]
        left_child = Node(child)
        child = [node_data[0], node_data[2], node_data[1], node_data[3]]
        central_child = Node(child)
        child = [node_data[0], node_data[1], node_data[3], node_data[2]]
        right_child = Node(child)
        start_node.set_children([left_child, central_child, right_child])

        for child_node in start_node.get_children():
            if not child_node.get_data() in visited \
               and isBetter(start_node, child_node):
                # recursive call
                sol = find_heuristic_solution(child_node, solution, visited)
                if sol != None:
                    return sol

        return None

def isBetter(parent_node, child_node):
    parent_quality = 0
    child_quality = 0
    parent_data = parent_node.get_data()
    child_data = child_node.get_data()
    for n in range(1,len(parent_data)):
        if(parent_data[n] > parent_data[n-1]):
            parent_quality += 1
        if(child_data[n] > child_data[n-1]):
            child_quality += 1

    if child_quality >= parent_quality:
        return True
    else:
        return False

if __name__ == "__main__":
    initial_state = [4,2,3,1]
    solution = [1,2,3,4]
    solution_node = None
    visited = []
    start_node = Node(initial_state)
    node = find_heuristic_solution(start_node, solution, visited)

    # show result
    result = []
    while node.get_parent() != None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print result
