from braille_dict import braille_dict as bdict
import re

number_pattern = re.compile('.*\d.*')

def convert_string(s):
	""" Takes a string and converts using Braille rules into a list of 
		lists, which contain pin values """
	assert type(s) == str
	# Split by space is default
	words = s.split()
	characters = []

	for word in words:
		# Check for numbers using regex
		if not number_pattern.match(word) is None:
			# TODO: Found a number. Convert to use number braille
			pass

		for c in word:
			characters += bdict[c]
		# Join words with spaces
		characters += bdict[' ']

	return characters
