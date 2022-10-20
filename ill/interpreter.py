import sys

class interpreter(object):

	def __init__(self, ascii_codes : list) -> None:
		self.ascii_codes = ascii_codes

	def interpret(self) -> None:
		for index, dec in enumerate(self.ascii_codes):
			while dec > 255:
				dec -= 255
			while dec < 0:
				dec += 255
			sys.stdout.write(chr(dec))
		print()