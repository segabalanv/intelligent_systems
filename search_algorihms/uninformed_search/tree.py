class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = None
        self.parent = None
        self.cost = None
        self.set_children(children)

    def set_children(self, children):
        self.children = children
        if self.children != None:
            for c in self.children:
                c.parent = self

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def equals(self, node):
        if self.get_data() == node.get_data():
            return True
        else:
            return False

    def on_list(self, node_list):
        on_the_list = False
        for n in node_list:
            if self.equals(n):
                on_the_list = True
        return on_the_list

    def __str__(self):
        return str(self.get_data())
