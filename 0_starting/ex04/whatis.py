import sys

def print_assertion_error(error_type: str):
	print("AssertionError:", error_type)

def main():
	if len(sys.argv) > 2:
		print_assertion_error("more than one argument is provided")
		return

	try:
		if int(sys.argv[1]) % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except:
		print_assertion_error("argument is not an integer")

main()	