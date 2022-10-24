"""
Ill's Parser
"""
class parser:

	"""
	Initializes Parser
	
	Attributes:
		src: a string consisting a source code
	"""
	def __init__(self, src : str) -> None:
		self.src = src
		self.line = 1
		self.pos = -1

	"""
	Advances the parser's current position and character
	"""
	def advance(self) -> None:
		self.pos += 1
		self.current_char = self.src[self.pos] if self.pos < len(self.src) else None

	"""
	Parse source code
	
	Result:
		result: a list filled with integer values
	"""
	def parse(self) -> list:
		result = []
		first = 65 # Start with the ASCII value of 'A'
		self.advance() # Initialize self.current_char
		while self.current_char != None:
			if self.current_char == ' ': # Output
				result.append(first)
			elif self.current_char == '\n': # Delimiter
				pass
			elif self.current_char == 'I': # Increment
				first += 1
			elif self.current_char == 'l': # Decrement
				first -= 1
			elif self.current_char == 'i' or self.current_char == 'L': # Multiplication and Division
				operator = self.current_char
				self.advance()
				if (
					self.current_char != ' ' and
					self.current_char != '\n' and
					self.current_char != 'I' and 
					self.current_char != 'l'
				): # Check if next character is not a possible value
					raise Exception("Invalid use of operator")
				second = 0 # Right node of the operation
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
				# if not self.current_char:
				# 	raise Exception("Invalid value for operation")
				if operator == 'i': # Multiplication
					first *= second
				elif operator == 'L': # Division
					first = int(first / second)
				self.pos -= 1
			else:
				raise Exception(f"Invalid character '{self.current_char}'")
			self.advance()
		return result
