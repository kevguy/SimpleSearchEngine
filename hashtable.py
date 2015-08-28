def hash_string(keyword, buckets):
	sum = 0
	for e in keyword:
		sum += ord(e)
	return sum % buckets

print hash_string('a',12)


def make_hashtable(nbuckets):
	index = []
	i = 0
	while i < nbuckets:
		index.append([])
		i += 1
	return index

def hashtable_get_bucket(htable, keyword):
	return htable[hash_string(keyword, len(htable))]


def hashtable_add(htable, key, value):
	target = hash_string(key, len(htable))
	i = 0
	for e in htable[target]:
		if key in e:
			htable[target][i].append(value)
			return htable
		else:
			i += 1
	htable[target].append([key, value])
	return htable

def hashtable_lookup(htable, key):
	target = hash_string(key, len(htable))
	i = 0
	for e in htable[target]:
		if key in e:
			return htable[target][i][1]
		else:
			i += 1
	return None

def hashtable_update(htable, key, value):
	target = hash_string(key, len(htable))
	i = 0
	for e in htable[target]:
		if key in e:
			htable[target][i][1] = value
			return htable
		else:
			i += 1
	htable[target].append([key, value])
	return htable


table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42], 
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2], 
#>>> ['Rochelle', 94]]]