def barLen() -> int:
    """
    Returns the length of the progress bar.

    Returns:
        int: The length of the progress bar (50).
    """
    return 50


def ft_tqdm(obj):
    """
    Simulates a progress bar while iterating through an iterable.

    Args:
        obj (iterable): The iterable object to iterate over.

    Yields:
        The elements of the iterable one by one.

    Prints a progress bar on the same line, showing the completion percentage,
    the progress bar, and the current index over the total number of elements.
    """
    index = 0
    objLen = len(obj)
    while index < objLen:
        progress = index / objLen
        completed = int(progress * barLen())
        remaining = barLen() - completed
        bar = '=' * completed + ' ' * remaining
        percent = str(int(progress * 100)).rjust(3)
        print(f"\r{percent}%|{bar}| {index + 1}/{objLen}",
              sep='', end='', flush=True)
        yield obj[index]
        index += 1
    bar = '=' * barLen()
    print(f"\r100%|{bar}| {objLen}/{objLen}", sep='', end='', flush=True)


def main():
    """
    Compare ft_tqdm with the original function.
    """
    from time import sleep
    from tqdm import tqdm

    for elem in ft_tqdm(range(4)):
        sleep(1)
    print()
    for elem in tqdm(range(4)):
        sleep(1)
    print()


if __name__ == "__main__":
    main()
