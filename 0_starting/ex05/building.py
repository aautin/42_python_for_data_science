import sys

def print_assertion_error(error_type: str):
	print("AssertionError:", error_type)

def main():
	sys.tracebacklimit = 0
	assert len(sys.argv) <= 2, "more than one argument is provided"

	text: str
	if len(sys.argv) < 2 or sys.argv[1] == None:
		print("What is the text to count?")
		text = sys.stdin.readline()
	else:
		text = sys.argv[1]

	uppers_nb = len([c for c in text if c.isupper()])
	lowers_nb = len([c for c in text if c.islower()])
	spaces_nb = len([c for c in text if c.isspace()])
	digits_nb = len([c for c in text if c.isdigit()])
	recognized_nb = uppers_nb + lowers_nb + spaces_nb + digits_nb
	print("The text contains", len(text), "characters:")
	print(uppers_nb, "upper letters")
	print(lowers_nb, "lower letters")
	print(len(text) - recognized_nb, "punctuation marks")
	print(spaces_nb, "spaces")
	print(digits_nb, "digits")

if __name__ == "__main__":
	main()