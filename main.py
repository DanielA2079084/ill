from ill import parser, interpreter

# debug = True

def main():
	while True:
		if debug:
			# path = input("Path: ")
			path = "tests/hello_world.ill"
			if path[-4:] != '.ill':
				print("Invalid file")
				continue
			try:
				with open(path, "r") as file:
					ascii_codes = parser(file.read()).parse()
					interpreter(ascii_codes).interpret()
					file.close()
			except FileNotFoundError:
				print("Invalid path")
			break
		else:
			code = input(":: ")
			if code == 'exit': break; 
			ascii_codes = parser(code).parse()
			interpreter(ascii_codes).interpret()

if __name__ == "__main__":
	main()
