'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
import collections
no_of_chars, total_query = [int(x)  for x in raw_input().split()]
s= raw_input()

for x in range(total_query):
	l, r, k = [int(x)  for x in raw_input().split()]
	d = collections.OrderedDict()
	for key, value in enumerate(s[l-1:r]):
		if not d.has_key(value):
			d[value] = 1
		else:
			d[value] += 1
	sorted_dict = dict(sorted(d.iteritems(), key=lambda key_value: key_value[0], reverse=False)	)
	total_chars = 0
	found = None
	#print sorted_dict
	for key, value in sorted_dict.items():
		total_chars += value
		if total_chars >= k and total_chars <= r-l:
			found = key
			break
	print found if found is not None else "Out of range"