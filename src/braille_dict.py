# File created 26/01/2015
# Contains a single variable, braille_dict, which can be used for the 
# conversion between braille characters and Braille lights
# Nested lists allow for single list return values for all characters

braille_dict = {
	# Lower case alphabet
	'a': [[True, False, False, False, False, False]],
	'b': [[True, True, False, False, False, False]],
	'c': [[True, False, False, True, False, False]],
	'd': [[True, False, False, True, True, False]], 
	'e': [[True, False, False, False, True, False]],
	'f': [[True, True, False, True, False, False]],
	'g': [[True, True, False, True, True, False]],
	'h': [[True, True, False, False, True, False]],
	'i': [[False, True, False, True, False, False]],
	'j': [[False, True, False, True, True, False]],
	'k': [[True, False, True, False, False, False]],
	'l': [[True, True, True, False, False, False]],
	'm': [[True, False, True, True, False, False]],
	'n': [[True, False, True, True, True, False]],
	'o': [[True, False, True, False, True, False]],
	'p': [[True, True, True, True, False, False]],
	'q': [[True, True, True, True, True, False]],
	'r': [[True, True, True, False, True, False]],
	's': [[False, True, True, True, False, False]],
	't': [[False, True, True, True, True, False]], 
	'u': [[True, False, True, False, False, True]],
	'v': [[True, True, True, False, False, True]],
	'w': [[False, True, False, True, True, True]],
	'x': [[True, True, False, False, True, True]],
	'y': [[True, False, True, True, True, True]],
	'z': [[True, False, True, False, True, True]],
	# Puncuation
	' ': [[False, False, False, False, True, True]]
	'.': [[False, True, False, False, True, True]],
	',': [[False, True, False, False, False, False]],
	';': [[False, True, True, False, False, False]],
	':': [[False, True, False, False, True, False]],
	'/': [[False, False, True, True, False, False]],
	'?': [[False, True, True, False, False, True]],
	'!': [[False, True, True, False, True, False]]
	'@': [[False, False, True, True, True, False]],
	'#': [[False, False, True, True, True, True]],
	'+': [[False, True, True, False, True, False]],
	'-': [[False, True, False, False, True, False]],
	'*': [[False, False, True, False, True, False]],
	'"': [[False, True, True, False, False, True]],
	'"': [[False, False, True, False, True, True]],
	'\'': [[False, False, True, False, False, False]],
	'<': [[True, True, False, False, False, True]],
	'>': [[False, False, True, True, True, False]],
	'(': [[False, True, True, False, True, True]],
	')': [[False, True, True, False, True, True]],
}
