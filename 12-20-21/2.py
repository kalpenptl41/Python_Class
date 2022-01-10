county = ['FortBend', 'Harris', 'Brazoria']
def find_index(to_search, target):
	for i, value in enumerate(to_search):
		if value == target:
			return i
		return -1
print (find_index(county, 'FortBend'))