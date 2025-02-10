import sys

def print_assertion_error(error_type: str):
	print("AssertionError:", error_type)

def main():
	if len(sys.argv) > 2:
		print_assertion_error("more than one argument is provided")
		return

	message: str
	if len(sys.argv) < 2 or sys.argv[1] == None:
		print("What is the text to count?")
		message = sys.stdin.readline()
	else:
		message = sys.argv[1]

	uppers_nb = len([c for c in message if c.isupper()])
	lowers_nb = len([c for c in message if c.islower()])
	spaces_nb = len([c for c in message if c.isspace()])
	digits_nb = len([c for c in message if c.isdigit()])
	recognized_nb = uppers_nb + lowers_nb + spaces_nb + digits_nb
	print("The text contains", len(message), "characters:")
	print(uppers_nb, "upper letters")
	print(lowers_nb, "lower letters")
	print(len(message) - recognized_nb, "punctuation marks")
	print(spaces_nb, "spaces")
	print(digits_nb, "digits")

if __name__ == "__main__":
	main()