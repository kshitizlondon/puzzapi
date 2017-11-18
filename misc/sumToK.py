

def commaListToInts(string_collection):
	string_collection = string_collection.split(",")
	i = 0
	for x in string_collection:
		string_collection[i] = int(x)
		i+=1
	return string_collection

def twoSum_hash(collection, target):
	collection = commaListToInts(collection)
	target = int(target)

	hash_map = {}
	i = 0

	for x in collection:
		if x in hash_map:
			hash_map[x].append(i)
		else:
			hash_map[x] = []
			hash_map[x].append(i)
		i+=1

	for x in collection:
		if target-x in hash_map:
			if target-x == x:
				if len(hash_map[x]) > 1:
					return [ (hash_map[x][0]), (hash_map[x][1]) ]
			else:
				return [ (hash_map[x][0]),(hash_map[target-x][0]) ]

	return None



def twoSum_iterative(collection, target):
	collection = commaListToInts(collection)
	target = int(target)

	l = 0
	r = len(collection)-1

	while l < r:
		if collection[l]+collection[r] > target:
			r-=1
		elif collection[l]+collection[r] < target:
			l+=1
		else:
			return [(l),(r)]
	return None


def threeSum(collection, target):
	collection = commaListToInts(collection)
	target = int(target)
	
	l = 0
	r = 0

	collection.sort()
	
	i = 0
	while i < len(collection)-2:
		l = i+1
		r = len(collection)-1

		while l < r:
			if collection[i]+collection[l]+collection[r] > target:
				r-=1
			elif collection[i]+collection[l]+collection[r] < target:
				l+=1
			else:
				return [(i),(l),(r)]
		i+=1
	return None