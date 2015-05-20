# Road trip with A* search
from tree import Node
from math import sin, cos, acos

def geo_dist(lat1, lon1, lat2, lon2):
    # conversion factor from degrees to radians
    deg_rad = 0.01745329
    # conversion factor from radians to degrees
    rad_deg = 57.29577951
    longitude = lon1 - lon2
    val = (sin(lat1*deg_rad)*sin(lat2*deg_rad)) \
          + (cos(lat1*deg_rad)*cos(lat2*deg_rad)*cos(longitude*deg_rad))
    return (acos(val)*rad_deg)*111.32

def compare(x,y):
    # heuristic function for the city x
    lat1 = coord[x.get_data()][0]
    lon1 = coord[x.get_data()][1]
    lat2 = coord[solution][0]
    lon2 = coord[solution][1]
    d = int(geo_dist(lat1, lon1, lat2, lon2))
    c1 = x.get_cost()+d

    # heuristic function for the city y
    lat1 = coord[y.get_data()][0]
    lon1 = coord[y.get_data()][1]
    lat2 = coord[solution][0]
    lon2 = coord[solution][1]
    d = int(geo_dist(lat1, lon1, lat2, lon2))
    c2 = y.get_cost()+d
    return c1 - c2

def find_sol_UCS(conns, init_st, sol):
    solved = False
    visited_nodes = []
    frontier_nodes = []
    start_node = Node(init_st)
    start_node.set_cost(0)
    frontier_nodes.append(start_node)
    while (not solved) and len(frontier_nodes) != 0:
        # sort the frontier nodes
        frontier_nodes = sorted(frontier_nodes, cmp=compare)
        current_node = frontier_nodes[0]
        # extract first node and add it to visited
        visited_nodes.append(frontier_nodes.pop(0))
        if current_node.get_data() == sol:
            # solution found
            solved = True
            return current_node
        else:
            # expand child nodes (connected cities)
            cn_data = current_node.get_data()
            children_list = []
            for ch in conns[cn_data]:
                child = Node(ch)
                # find g(n)
                cost = conns[cn_data][ch]
                child.set_cost(current_node.get_cost()+cost)
                children_list.append(child)
                if not child.on_list(visited_nodes):
                    # if is on list we replace it the new
                    # cost value, if less.
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

    coord = {
        "Malaga": (36.43, -4.24),
        "Sevilla": (37.23, -5.59),
        "Granada": (37.11, -3.35),
        "Valencia": (39.28, -0.22),
        "Madrid": (40.24, -3.41),
        "Salamanca": (40.57, -5.40),
        "Santiago": (45.52, -8.33),
        "Santander": (43.28, -3.48),
        "Zaragoza": (41.39, -0.52),
        "Barcelona": (41.23, 2.11)
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
