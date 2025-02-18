def barLen() -> int:
    return 50

def ft_tqdm(obj):
    index = 0
    objLen = len(obj)
    while index < objLen:
        progress = index / objLen
        completed = int(progress * barLen())
        remaining = barLen() - completed
        bar = '=' * completed + ' ' * remaining
        percent = str(int(progress * 100)).rjust(3)
        print(f"\r{percent}%|{bar}| {index + 1}/{objLen}", sep='', end='', flush=True)
        yield obj[index]
        index += 1
    bar = '=' * barLen()
    print(f"\r100%|{bar}| {objLen}/{objLen}", sep='', end='', flush=True)

