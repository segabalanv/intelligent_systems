# Flights with Breadth First Search
from tree import Node

def find_solution_BFS(connections, initial_state, solution):
    solved = False
    visited_nodes = []
    frontier_nodes = []
    startNode = Node(initial_state)
    frontier_nodes.append(startNode)
    while(not solved) and len(frontier_nodes) != 0:
        node = frontier_nodes[0]
        # extract node and add it to visited_nodes
        visited_nodes.append(frontier_nodes.pop(0));
        if node.get_data() == solution:
            # solution found
            solved = True
            return node
        else:
            # expand child nodes (cities with connection)
            node_data = node.get_data();
            children_list = []
            for one_child in connections[node_data]:
                child = Node(one_child)
                children_list.append(child)
                if not child.on_list(visited_nodes) \
                   and not child.on_list(frontier_nodes):
                    frontier_nodes.append(child)

            node.set_children(children_list)

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
    initial_state = "Zaragoza"
    solution = "Sevilla"
    solution_node = find_solution_BFS(connections, initial_state, solution)
    # show result
    result = []
    node = solution_node
    while node.get_parent() != None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print result
