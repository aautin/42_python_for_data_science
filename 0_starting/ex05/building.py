import sys


def main():

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as e:
        print("AssertionError:", e)
        return

    text: str
    if len(sys.argv) < 2 or sys.argv[1] is None:
        print("What is the text to count?")
        text = sys.stdin.readline()
    else:
        text = sys.argv[1]

    punct_marks = ['!', ",", "'", ";", "\"", ".", "-", "?"]
    print("The text contains", len(text), "characters:")
    print(len([c for c in text if c.isupper()]), "upper letters")
    print(len([c for c in text if c.islower()]), "lower letters")
    print(len([c for c in text if c in punct_marks]), "punctuation marks")
    print(len([c for c in text if c.isspace()]), "spaces")
    print(len([c for c in text if c.isdigit()]), "digits")


if __name__ == "__main__":
    main()
