# ILP with backtracking
# Here we solve a very simple problem of integer linear programming
# that can be stated as follows:
#       f(x1, x2) = (12-6)*x1 + (8-4)*x2
#       7*x1 + 4*x2 <= 150
#       6*x1 + 5*x2 <= 160
#       x1 >= 0
#       x2 >= 0

def b_track(variables, var_range, opt, depth):
    min_val = var_range[depth][0]
    max_val = var_range[depth][1]
    for x in range(min_val, max_val):
        variables[depth] = x
        if depth < len(variables)-1:
            # the assignment is complete if it doesn't violate restrictions
            if isComplete(variables):
                opt = b_track(variables[:], var_range, opt, depth+1)

        else:
            # at leaf. Check solution
            sol = grade_sol(variables)
            if sol > grade_sol(opt) and isComplete(variables):
                opt = (variables[0], variables[1])
    return opt

def grade_sol(variables):
    x1 = variables[0]
    x2 = variables[1]
    val = (12-6)*x1+(8-4)*x2
    return val

def isComplete(variables):
    x1 = variables[0]
    x2 = variables[1]
    val1 = 7*x1+4*x2
    val2 = 6*x1+5*x2
    # check if restrictions are valid
    if val1 <= 150 and val2 <= 160:
        return True
    else:
        return False

if __name__ == "__main__":
    # values of x1 and x2
    variables = [0,0]
    # range of x1 and x2
    var_range = [(0,51), (0,76)]
    # best solution
    opt = (0,0)
    sol = b_track(variables[:], var_range, opt, 0)
    print "Best solution found:"
    print str(sol[0]) + " pants."
    print str(sol[1]) + " t-shirts."
    print "Total cost: " + str(grade_sol(sol))
