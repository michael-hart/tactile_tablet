from braille_dict import braille_dict as bdict
import re

number_pattern = re.compile('.*\d.*')

def convert_string(s):
	""" Takes a string and converts using Braille rules into a list of 
		lists, which contain pin values """
	assert type(s) == str
	# Split by space is default
	words = s.split()
	braille_words = []

	for word in words:
		braille_words.append([])
		# Check for numbers using regex
		if not number_pattern.match(word) is None:
			# TODO: Found a number. Convert to use number braille
			pass

		for c in word:
			braille_words[-1] += bdict[c]

	return braille_words
