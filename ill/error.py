"""
Ill's Error Class
"""
class error:

	"""
	Initializes error

	Attributes:
		name: a string consisting of the error name
		coloumn: an optional integer consisting of the value of the coloumn position of the error
		line: an optional integer consisting of the value of the line position of the error
		details: an optional string consisting of the error details
	"""
	def __init__(self, name : str, coloumn = None, line = None, details = None) -> None:
		self.name = name
		self.coloumn = coloumn
		self.line = line
		self.details = details
		self.warn()

	"""
	Raises the error
	"""
	def warn(self):
		print(f"{self.name}: {self.details}")
		if self.coloumn and self.line:
			print(f"Coloumn: {self.coloumn}, Line: {self.line}")

class invalid_path_error(error):

	def __init__(self, path : str):
		super.__init__(name = "InvalidPathError", details = f"Unable to open file '{path}'")

class invalid_char_error(error):

	def __init__(self, coloumn : int, line : int, char : str):
		super.__init__("InvalidCharacterError", coloumn, line, f"Invalid character '{char}'")
