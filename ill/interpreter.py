import sys

class interpreter(object):

	def __init__(self, ascii_codes : list) -> None:
		self.ascii_codes = ascii_codes

	def interpret(self) -> None:
		for index, dec in enumerate(self.ascii_codes):
			# Alter values if not in range of 0 - 255
			while dec > 255:
				dec -= 255
			while dec < 0:
				dec += 255
			sys.stdout.write(chr(dec)) # Output converted values
		print() # \n