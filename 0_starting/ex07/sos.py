import sys


def get_morse(text: str) -> str:
    """
    Converts a given text into Morse code.

    Parameters:
    text (str): The input string consisting of letters, digits, and spaces.

    Returns:
    str: The Morse code representation of the input text.
    """

    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',

        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

        ' ': '/'
    }
    return ' '.join([morse[c] for c in text])


def main():
    """
    Main function to handle command-line input and convert it to Morse code.

    Validates input to ensure it contains only alphanum characters or spaces.
    If the input is valid, it prints the corresponding Morse code.

    Exceptions:
    - Prints an AssertionError message if the input format is incorrect.
    """

    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        for c in sys.argv[1]:
            assert c.isalnum() or c == ' ', "the arguments are bad"
    except AssertionError as e:
        print("AssertionError:", e)
        return

    print(get_morse(sys.argv[1]))


if __name__ == "__main__":
    main()
