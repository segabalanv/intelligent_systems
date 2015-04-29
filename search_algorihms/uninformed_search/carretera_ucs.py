# Uniform cost search

from tree import Node

def compare(x, y):
    return x.get_cost() - y.get_cost()

def find_sol_UCS(conns, init_st, sol):
    solved = False
    visited_nodes = []
    frontier_nodes = []
    start_node = Node(init_st)
    start_node.set_cost(0)
    frontier_nodes.append(start_node)
    while(not solved) and len(frontier_nodes) != 0:
        frontier_nodes = sorted(frontier_nodes, cmp=compare)
        current_node = frontier_nodes[0]
        visited_nodes.append(frontier_nodes.pop(0))
        if current_node.get_data() == sol:
            solved = True
            return current_node
        else:
            cn_data = current_node.get_data()
            children_list = []
            for ch in conns[cn_data]:
                child = Node(ch)
                cost = conns[cn_data][ch]
                child.set_cost(current_node.get_cost()+cost)
                children_list.append(child)
                if not child.on_list(visited_nodes):
                    if child.on_list(frontier_nodes):
                        for n in frontier_nodes:
                            if n.equals(child) and n.get_cost() > child.get_cost():
                                frontier_nodes.remove(n)
                                frontier_nodes.append(child)
                    else:
                        frontier_nodes.append(child)
                        
            current_node.set_children(children_list)

if __name__ == "__main__":
    connections = {
        "Malaga" : {"Granada" : 125, "Madrid" : 513},
        "Sevilla" : {"Madrid" : 514},
        "Granada" : {"Malaga" : 125, "Madrid" : 423, "Valencia" : 491},
        "Valencia" : {"Granada" : 491, "Madrid" : 356, "Zaragoza" : 309, \
                      "Barcelona" : 346},
        "Madrid" : {"Salamanca" : 203, "Sevilla": 514, "Malaga" : 513, \
                    "Granada" : 423, "Barcelona" : 603, "Santander" : 437, \
                    "Valencia" : 356, "Zaragoza" : 313, "Santiago" : 599},
        "Salamanca" : {"Santiago" : 390, "Madrid": 203},
        "Santiago" : {"Salamanca" : 390, "Madrid" : 599},
        "Santander" : {"Madrid" : 437, "Zaragoza" : 394},
        "Zaragoza" : {"Barcelona" : 296, "Valencia" : 309, "Madrid" : 313},
        "Barcelona" : {"Zaragoza" : 296, "Madrid" : 603, "Valencia" : 346}
        }
    initial_state = "Malaga"
    solution = "Santiago"
    solution_node = find_sol_UCS(connections, initial_state, solution)

    result = []
    node = solution_node
    while node.get_parent() != None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print result
    print "Cost " + str(solution_node.get_cost())
