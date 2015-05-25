# simple perpeptron for the OR function
def output(k, weights, t):
    z = -t
    for i in range(len(k)):
        z += k[i]*weights[i]
    if z >= 0:
        return 1
    else:
        return 0


def train_perceptron(input_data, weights, t, l):
    counter = 0
    errors = True
    while errors:
        counter+=1 
        errors = False
        # train perceptron
        for k, y in input_data.iteritems():
            z = output(k, weights, t)
            if z != y:
                errors = True
                # error
                e = y-z
                # calculate adjustment
                delta_t = -(l*e)
                t += delta_t
                for i in range(len(k)):
                    delta_w = l*e*k[i]
                    weights[i] += delta_w
    print counter
    return weights, t

def classify(inputs, weights, t):
    return output(inputs, weights, t)

if __name__ == "__main__":
    input_data = { (0,0): 0, (0,1): 0, (1,0): 0, (1,1): 1 }
    weights = [0.2, -0.5]
    t = 0.4
    l = 0.2
    weights, t = train_perceptron(input_data, weights, t, l)
    print classify((0,0), weights, t)
