from ill import invalid_path_error, parser, interpreter

debug = False

parser_ = parser()  # The parser
interpreter_ = interpreter()  # The interpreter

"""
Compiles source code

Attributes:
	file_name: a string consisting of the source file name
	src: a string consisting of the source code
"""
def compile(file_name : str, src : str) -> None:
	interpreter_.interpret(parser_.parse(file_name, src))

"""
Compiles a source file

Attributes:
	file_name: a string consisting of the source file name
	path: a string consisting of the path to the source file
"""
def compile_file(file_name : str, path : str) -> None:
	try:
		with open(path, 'r') as file:
			compile(file_name, file.read())
			file.close()
	except FileNotFoundError:
		invalid_path_error(path)

"""
Main function
"""
def main():
	parser_ = parser()
	interpreter_ = interpreter()
	if debug:
		path = input('Path: ')
		# path = "tests/hello_world.ill"
		if path[-4:] != '.ill':
			invalid_file_error(path)
			return
		compile_file(path)
		return
	while True:
		code = input(':: ')
		if debug: print(f'Source code:\n{code}');
		if code == 'exit': break; 
		elif code[-4:] == '.ill': compile_file(code, code);
		else: compile('<stdin>', code);

if __name__ == '__main__':
	main()
