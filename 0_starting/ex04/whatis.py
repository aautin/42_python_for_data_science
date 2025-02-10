import sys

def main():
	if len(sys.argv) < 2:
		sys.exit()

	sys.tracebacklimit = 0
	assert len(sys.argv) <= 2, "more than one argument is provided"
	
	exception = False
	try:
		int(sys.argv[1])
	except:
		exception = True
	assert exception == False, "argument is not an integer"

	print("I'm Odd." if int(sys.argv[1]) % 2 else "I'm Even.")

main()	