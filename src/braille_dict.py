# File created 26/01/2015
# Contains a single variable, braille_dict, which can be used for the 
# conversion between braille characters and Braille lights
# Nested lists allow for single list return values for all characters
from string import lowercase

braille_dict = {
	# Lower case alphabet
	'a': [[False, True, True, True, True, True]],
	'b': [[False, False, True, True, True, True]],
	'c': [[False, True, True, True, True, False]],
	'd': [[False, True, True, True, False, False]],
	'e': [[False, True, True, True, False, True]],
	'f': [[False, False, True, True, True, False]],
	'g': [[False, False, True, True, False, False]],
	'h': [[False, False, True, True, False, True]],
	'i': [[True, False, True, True, True, False]],
	'j': [[True, False, True, True, False, False]],
	'k': [[False, True, False, True, True, True]],
	'l': [[False, False, False, True, True, True]],
	'm': [[False, True, False, True, True, False]],
	'n': [[False, True, False, True, False, False]],
	'o': [[False, True, False, True, False, True]],
	'p': [[False, False, False, True, True, False]],
	'q': [[False, False, False, True, False, False]],
	'r': [[False, False, False, True, False, True]],
	's': [[True, False, False, True, True, False]],
	't': [[True, False, False, True, False, False]],
	'u': [[False, True, False, False, True, True]],
	'v': [[False, False, False, False, True, True]],
	'w': [[True, False, True, False, False, False]],
	'x': [[False, True, False, False, True, False]],
	'y': [[False, True, False, False, False, False]],
	'z': [[False, True, False, False, False, True]],

	# Punctuation
	' ': [[True, True, True, True, True, True]],
	'.': [[True, False, True, False, False, True]],
	',': [[True, False, True, True, True, True]],
	';': [[True, False, False, True, True, True]],
	':': [[True, False, True, True, False, True]],
	'?': [[True, False, False, False, True, True]],
	# l" is left speech mark
	'l"': [[True, False, False, False, True, True]],
	'!': [[True, False, False, True, False, True]],
	'(': [[True, False, False, False, False, True]],
	')': [[True, False, False, False, False, True]],
	'*': [[True, True, False, True, False, True]],
	# r" is right speech mark
	'r"': [[True, True, False, False, False, True]],
	'\'': [[True, True, False, True, True, True]],
	'-': [[True, True, False, False, True, True]],

	# Special Signs
	'capital': [[True, True, True, True, True, False]]

}

# Capital Letters
for upper, lower in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', lowercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
	braille_dict[upper] = braille_dict['capital'] + braille_dict[lower]

# Numbers
for number, letter in zip('1234567890', 'abcdefghij'):
	braille_dict[number] = braille_dict[letter]
