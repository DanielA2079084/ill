from ill import parser, interpreter

# debug = True

parser_ = None
interpreter_ = None

"""
Compiles source code

Attributes:
	src: a string consisting the source code
"""
def compile(src : str) -> None:
	interpreter_.interpret(parser_.parse(src))

"""
Compiles a source file

Attributes:
	path: a string consisting the path to the source file
"""
def compile_file(path : str) -> None:
	try:
		with open(path, 'r') as file:
			compile(file.read())
			file.close()
	except FileNotFoundError:
		print(f"Invalid path '{path}'")

"""
Main function
"""
def main():
	parser_ = parser()
	interpreter_ = interpreter()
	if debug:
		# path = input("Path: ")
		path = "tests/hello_world.ill"
		if path[-4:] != '.ill':
			print("Invalid file")
			return
		compile_file(path)
		return
	while True:
		code = input(":: ")
		if code == 'exit': break; 
		elif code[-4:] == '.ill': compile_file(code);
		else: compile(code);

if __name__ == "__main__":
	main()
