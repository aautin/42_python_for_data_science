import sys

def main():
	if len(sys.argv) < 2:
		return

	try:
		assert len(sys.argv) == 2, "more than one argument is provided"
		print("I'm Odd." if int(sys.argv[1]) % 2 else "I'm Even.")
	except AssertionError as e:
		print("AssertionError:", e)
		return
	except ValueError:
		print("AssertionError: argument is not an integer")
		return

main()