from ill import parser, interpreter

debug = True

def main():
	while True:
		# For debugging
		if debug:
			# path = input("Path: ")
			path = "tests/hello_world.ill"
			# Check if file is valid
			if path[-4:] != '.ill':
				print("Invalid file")
				continue
			# Open the file
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
			if code == 'exit': break; # For exiting
			ascii_codes = parser(code).parse()
			interpreter(ascii_codes).interpret()

if __name__ == "__main__":
	main()