# Dijkstra's algorithm
import sys
def dijkstra(graph, init_node):
	tags = {}
	visited = []
	pending = [init_node]
	current_node = init_node
	
	# init_node
	tags[current_node] = [0, '']
	# pick next node with the east accumulated weight
	while len(pending) > 0:
		current_node = least_weight_node(tags, visited)
		visited.append(current_node)
		# get adjacent node
		for adjacent, weight in graph[current_node].iteritems():
			if adjacent not in pending and \
			adjacent not in visited:
				pending.append(adjacent)
			new_weight = tags[current_node][0] \
			+ graph[current_node][adjacent]
			# tag
			if adjacent not in visited:
				if adjacent not in tags:
					tags[adjacent] = [new_weight, current_node]
				else:
					if tags[adjacent][0] > new_weight:
						tags[adjacent] = \
						[new_weight, current_node]
						
		del pending[pending.index(current_node)]
	
	return tags

def least_weight_node(tags, visited):
	least = sys.maxint
	for node, tag in tags.iteritems():
		if tag[0] < least and node not in visited:
			least = tag[0]
			least_node = node
	return least_node

if __name__ == "__main__":
	graph = {
		'1' : {'3':6, '2':3},
		'2' : {'4':1, '1':3, '3':2},
		'3' : {'1':6, '2':2, '4':4, '5':2},
		'4' : {'2':1, '3':4, '5':6},
		'5' : {'3':2, '4':6, '6':2, '7':2},
		'6' : {'5':2, '7':3},
		'7' : {'5':2, '6':3}}
	tags = dijkstra(graph, '1')
	print tags