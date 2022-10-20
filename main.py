from ill import parser, interpreter

debug = True

def main():
	if debug:
		path = input("Path: ")
		with open(path, "r") as file:
			ascii_codes = parser(file.read()).parse()
			interpreter(ascii_codes).interpret()
			return
	while True:
		code = input(":: ")
		if code == 'exit':
			break
		ascii_codes = parser(code).parse()
		interpreter(ascii_codes).interpret()

if __name__ == "__main__":
	main()