# Flights with iterative Depth Search

from tree import Node

def iter_DFS(node, solution):
    for limit in range(0,100):
        visited = []
        sol = find_solution_rec_DFS(node, solution, visited, limit)
        if sol != None:
            return sol

def find_solution_rec_DFS(node, solution, visited, limit):
    if limit > 0:
        visited.append(node)
        if node.get_data() == solution:
            return node
        else:
            # expand children nodes (cities with connection)
            node_data = node.get_data();
            children_list = []
            for a_child in connections[node_data]:
                child = Node(a_child)
                if not child.on_list(visited):
                    children_list.append(child)

            node.set_children(children_list)

            for child_node in node.get_children():
                if not child_node.get_data() in visited:
                    # recursive call
                    sol = find_solution_rec_DFS(child_node, solution, \
                                                visited, limit-1)
                    if sol != None:
                        return sol

        return None

if __name__ == "__main__":
    connections = {
        "Malaga" : { "Salamanca", "Madrid", "Barcelona" },
        "Sevilla" : { "Santiago", "Madrid" },
        "Granada" : { "Valencia" },
        "Valencia" : { "Barcelona", "Granada" },
        "Madrid" : { "Salamanca", "Sevilla", "Malaga", \
                     "Barcelona", "Santander" },
        "Salamanca": { "Malaga", "Madrid" },
        "Santiago" : { "Sevilla", "Santander", "Barcelona" },
        "Santander" : { "Santiago", "Madrid" },
        "Zaragoza" : { "Barcelona" },
        "Barcelona" : { "Zaragoza", "Santiago", "Madrid", "Malaga", \
                        "Valencia" },
        "Granada" : { "Valencia" }
        }
    initial_state = "Malaga"
    solution = "Santiago"
    initial_node = Node(initial_state)
    node = iter_DFS(initial_node, solution)

    #show result
    if node != None:
        result = []
        while node.get_parent() != None:
            result.append(node.get_data())
            node = node.get_parent()
        result.append(initial_state)
        result.reverse()
        print result
    else:
        print "solution not found"
