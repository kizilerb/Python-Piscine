import sys

def ft_filter_return(function: callable, input: iter):
    if function:
        yield from (i for i in input if function(i))
    else:
        yield from (i for i in input if i)


def ft_filter_yield(function: callable, input: iter):
    if function:
        return (i for i in input if function(i))
    else:
        return (i for i in input if i)


def ft_filter_return(function, iterable):
    return [i for i in iterable if function(i)]  # Returns a full list (High memory usage)

def ft_filter_yield(function, iterable):
    yield from (i for i in iterable if function(i))  # Generates values lazily (Efficient)

def is_even(n):
    return n % 2 == 0

def main():
    numbers = range(1, 10000000)  # 10 million numbers

    print("Using return (First 5 numbers):")
    result_list = ft_filter_return(is_even, numbers)  # Stores full list
    print(result_list[:5])  # Print first 5 numbers

    print("\nUsing yield from (First 5 numbers):")
    count = 0
    for num in ft_filter_yield(is_even, numbers):  # Yields values one by one
        print(num)
        count += 1
        if count == 5:
            break  # Stop after 5 numbers

if __name__ == "__main__":
    main()


def ft_filter(function: callable, input: iter):
    if function:
        yield from (i for i in input if function(i))
    else:
        yield from (i for i in input if i)

def main2():
    is_even = lambda a : True if a % 2 == 0 else False
    iter = [2,4,5,6,7,8]
    print(is_even(1))
    print(list(ft_filter(is_even, iter)))

