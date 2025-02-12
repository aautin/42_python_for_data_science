import sys
from ft_filter import ft_filter


def main():
    """
    Takes two command-line arguments:
    1. A string containing multiple words.
    2. An integer representing the minimum word length.

    Filters and prints words from the string that are longer than the given
    integer.

    Exceptions handled: incorrect number of arguments, non-integer second
    argument, or excessively long first argument.
    """

    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        string = sys.argv[1]
        length = int(sys.argv[2])
        print(list(ft_filter(lambda word: len(word) > length, string.split())))
    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError: the second argument is not an integer")
    except OverflowError:
        print("AssertionError: the length of the first argument is too long")


if __name__ == "__main__":
    main()
