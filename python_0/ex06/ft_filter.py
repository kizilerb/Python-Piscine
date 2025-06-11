def ft_filter(function: callable, input: iter):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    """
    if function:
        yield from (i for i in input if function(i))
    else:
        yield from (i for i in input if i)
