def ft_filter(function: callable, input: iter):
    if function:
        yield from (i for i in input if function(i))
    else:
        yield from (i for i in input if i)
