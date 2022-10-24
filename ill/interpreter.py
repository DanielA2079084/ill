import sys

"""
Ill's Interpreter
"""
class interpreter:

	"""
	Interprets ASCII codes
	
	Attributes:
		ast: a list of integers consisting of ASCII codes
	"""
	def interpret(self, ascii_codes : list) -> None:
		for index, dec in enumerate(ascii_codes):
			# Alter values if not in range of 0 - 255
			while dec.value > 255: dec.value -= 255;
			while dec.value < 0: dec.value += 255;
			sys.stdout.write(chr(dec.value)) # Output converted values
		print()
