# vehicle routing problem
import math
from operator import itemgetter

def distance(coord1, coord2):
	lat1 = coord1[0]
	lon1 = coord1[1]
	lat2 = coord2[0]
	lon2 = coord2[1]
	return math.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)

def on_path(paths, c):
	path = None
	for p in paths:
		if c in p:
			path = p
	return path

def path_weight(path):
	total = 0
	for c in path:
		total = total + orders[c]
	return total

def vrp_greedy():
	# calculate the savings
	s = {}
	for c1 in coord:
		for c2 in coord:
			if c1 != c2:
				if not (c2, c1) in s:
					d_c1_c2 = distance(coord[c1], coord[c2])
					d_c1_store = distance(coord[c1], store)
					d_c2_store = distance(coord[c2], store)
					s[c1,c2] = d_c1_store + d_c2_store - d_c1_c2
	# sort savings
	s = sorted(s.items(), key=itemgetter(1), reverse=True)
	# build paths
	paths = []
	for k, v in s:
		rc1 = on_path(paths, k[0])
		rc2 = on_path(paths, k[1])
		if rc1 == None and rc2 == None:
			# we create them since they can't be found in any path
			if path_weight([k[0],k[1]]) <= max_load:
				paths.append([k[0],k[1]])
		elif rc1 != None and rc2 == None:
			# first city already in path. Add city 2
			if rc1[0] == k[0]:
				if path_weight(rc1) + path_weight([k[1]]) <= max_load:
					paths[paths.index(rc1)].insert(0, k[1])
			elif rc1[len(rc1)-1] == k[0]:
				if path_weight(rc1) + path_weight([k[1]]) <= max_load:
					paths[paths.index(rc1)].append(k[1])
		elif rc1 == None and rc2 != None:
			# second city already in path. Add city 1
			if rc2[0] == k[1]:
				if path_weight(rc2) + path_weight([k[0]]) <= max_load:
					paths[paths.index(rc2)].insert(0, k[0])
			elif rc2[len(rc2)-1] == k[1]:
				if path_weight(rc2) + path_weight([k[0]]) <= max_load:
					paths[paths.index(rc2)].append(k[0])
		elif rc1 != None and rc2 != None and rc1 != rc2:
			# both cities in path. Try to join them
			if rc1[0] == k[0] and rc2[len(rc2)-1] == k[1]:
				if path_weight(rc1) + path_weight(rc2) <= max_load:
					paths[paths.index(rc2)].extend(rc1)
					paths.remove(rc1)
			elif rc1[len(rc1)-1] == k[0] and rc2[0] == k[1]:
				if path_weight(rc1) + path_weight(rc2) <= max_load:
					paths[paths.index(rc1)].extend(rc2)
					paths.remove(rc2)
	
	return paths

if __name__ == "__main__":
	coord = {
		"Malaga" : (36.43, -4.24),
		"Sevilla" : (37.23, -5.59),
		"Granada" : (37.11, -3.35),
		"Valencia" : (39.28, -0.22),
		"Madrid" : (40.24, -3.41),
		"Salamanca" : (40.57, -5.40),
		"Santiago" : (42.52, -8.33),
		"Santander" : (43.28, -3.48),
		"Zaragoza" : (41.39, -0.52),
		"Barcelona" : (41.23, 2.11)
	}
	
	orders = {
		"Malaga" : 10,
		"Sevilla" : 13,
		"Granada" : 7,
		"Valencia" : 11,
		"Madrid" : 15,
		"Salamanca" : 8,
		"Santiago" : 6,
		"Santander" : 7,
		"Zaragoza" : 8,
		"Barcelona" : 14
	}

	store = (40.23, -3.40)
	max_load = 40
	
	paths = vrp_greedy()
	for p in paths:
		print p
	