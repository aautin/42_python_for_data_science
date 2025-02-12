def ft_filter(function, iterable):
    """
    Filters elements of an iterable based on a boolean function.
    If function is None, removes falsy values.
    Returns a generator of filtered elements.
    """
    if not function:
        return (it for it in iterable if it)
    else:
        return (it for it in iterable if function(it))
