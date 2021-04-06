input_strings = { "abb", "abc", "xyz", "xyy"}
pattern = "mno"

def pattern_decode(pattern):
	asc = ord(pattern[0])
	return map(lambda c: ord(c)-asc, pattern)

def pattern_match(input_strings):
    decoded_pattern = pattern_decode(pattern)
    print filter(lambda s: pattern_decode(s)== decoded_pattern, input_strings)
pattern_match(input_strings)