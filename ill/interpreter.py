import sys

"""
Ill's Interpreter
"""
class interpreter(object):

	"""
	Initializes interpreter
	"""
	def __init__(self):
		pass

	"""
	Interprets ASCII codes
	
	Attributes:
		ast: a list of integers filled with ASCII codes
	"""
	def interpret(self, ascii_codes : list) -> None:
		for index, dec in enumerate(ascii_codes):
			# Alter values if not in range of 0 - 255
			while dec > 255:
				dec -= 255
			while dec < 0:
				dec += 255
			sys.stdout.write(chr(dec)) # Output converted values
		print() # \n
