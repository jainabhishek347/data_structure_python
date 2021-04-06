
def str_compression_in_place(str):
	start_ptr = 0
	char_need_to_macth = str[0]
	count = 1
	for c in str[1:]:
		if c == char_need_to_macth:
			count = count+1
		else:
			#if count>1:
			str[start_ptr] = char_need_to_macth
			str[start_ptr+1] = count
			start_ptr = start_ptr+2
			char_need_to_macth =c
			count =1
			#else:
			#	str[start_ptr] = char_need_to_macth
			#	start_ptr = start_ptr+1
			#	char_need_to_macth = c
	if count>1:
		str[start_ptr] = char_need_to_macth
		str[start_ptr+1] =count
	print str[:start_ptr+2]

str ="AAABBBCDEFGHIJKLLLLLLLLLLLLLLL"
str_compression_in_place(list(str))

