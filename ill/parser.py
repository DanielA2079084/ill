from .error import invalid_char_error

debug = False

"""
Ill's Parser Node
"""
class node:

	"""
	Initializes Node

	Attributes:
		file: a string consisting of the file name
		coloumn: an integer consisting of the value's coloumn position
		line: an integer consisting of the value's line position
		value: an integer consisting the ASCII index
	"""
	def __init__(self, file : str, coloumn : int, line : int, value : int) -> None:
		self.coloumn = coloumn
		self.line = line
		self.value = value

	"""
	Represents the node
	"""
	def __repr__(self):
		return f"Node: [Coloumn: {self.coloumn}, Line: {self.line}, Value: {self.value}]"

"""
Ill's Parser
"""
class parser:

	"""
	Initializes Parser
	"""
	def __init__(self) -> None:
		self.reset_pos()

	"""
	Resets the parser's position back to default
	"""
	def reset_pos(self) -> None:
		self.coloumn = 0
		self.line = 1
		self.pos = -1

	"""
	Advances the parser's current position and character
	"""
	def advance(self) -> None:
		self.pos += 1
		self.coloumn += 1
		self.current_char = self.src[self.pos] if self.pos < len(self.src) else None

	"""
	Parse source code
	
	Attributes:
		src: a string consisting the source code
	Result:
		result: a list filled with integer / ASCII codes
	"""
	def parse(self, file_name : str, src : str) -> list:
		self.src = src
		self.reset_pos()
		result = []
		first = 65 
		self.advance()
		while self.current_char != None:
			if self.current_char == ' ':  # Output
				result.append(node(file_name, self.coloumn, self.line, first))
			elif self.current_char == '\n':  # Delimiter
				self.coloumn = 1
				self.line += 1
			elif self.current_char == 'I':  # Increment
				first += 1
			elif self.current_char == 'l':  # Decrement
				first -= 1
			elif self.current_char == 'i' or self.current_char == 'L':  # Multiplication and Division
				operator = self.current_char
				self.advance()
				if (
					self.current_char != ' ' and
					self.current_char != '\n' and
					self.current_char != 'I' and 
					self.current_char != 'l'
				): 
					raise Exception("Invalid use of operator")
				second = 0
				while (
					self.current_char and
					(
						self.current_char == 'I' or
						self.current_char == 'l'
					)
				): 
					if self.current_char == 'I':
						second += 1
					elif self.current_char == 'l':
						second -= 1
					self.advance()
				if operator == 'i':  # Multiplication
					first *= second
				elif operator == 'L':  # Division
					first = int(first / second)
				self.pos -= 1
			else:
				raise invalid_char_error(self.current_char)
			self.advance()
		if debug: print(result);
		return result
