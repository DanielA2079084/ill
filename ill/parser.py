# Parser
class parser(object):

	def __init__(self, src : str) -> None:
		self.src = src
		self.line = 1
		self.pos = -1

	def advance(self) -> None:
		self.pos += 1
		self.current_char = self.src[self.pos] if self.pos < len(self.src) else None

	def parse(self) -> list:
		result = []
		first = 65
		self.advance()
		while self.current_char != None:
			if self.current_char == ' ':
				result.append(first)
			elif self.current_char == 'I':
				first += 1
			elif self.current_char == 'l':
				first -= 1
			elif self.current_char == 'i' or self.current_char == 'L':
				operator = self.current_char
				self.advance()
				if (
					# self.current_char != ' ' and
					self.current_char != 'I' and 
					self.current_char != 'l'
				):
					raise Exception("Invalid use of operator")
				second = 0
				while (
					self.current_char == 'I' or
					self.current_char == 'l'
				):
					if self.current_char == 'I':
						second += 1
					elif self.current_char == 'l':
						second -= 1
					self.advance()
				if not self.current_char:
					raise Exception("Invalid value for operation")
				if operator == 'i':
					first *= second
				elif operator == 'L':
					first = int(first / second)
				if self.current_char == ' ':
					result.append(first)
			else:
				raise Exception("Invalid character")
			self.advance()
		return result