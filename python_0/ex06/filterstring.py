import sys
from ft_filter import ft_filter


def is_num(N):
    # Second given argument should be checked whether it is an integer.
    try:
        int(sys.argv[2])
        return (True)
    except ValueError:
        return (False)


def filterstring(str):
    # Words are separated from each other by space characters.
    separated = str.split()
    num = int(sys.argv[2])
    sorted = list(ft_filter(lambda i: 1 if len(i) > num else 0, separated))
    print(sorted)


def main():
    """
    Create a program that accepts two arguments: a string(S), and an integer(N)
    The program should output a list of words
    from S that have a length greater than N.
    """
    try:
        if len(sys.argv) == 3 and is_num(sys.argv[2]):
            filterstring(sys.argv[1])
        else:
            raise AssertionError("The arguments are bad")
        """
        If the number of argument is different from 2,
        or if the type of any argument is wrong,
        the program prints an AssertionError.
        """
    except AssertionError as error:
        # raised assertion error is caught by except.
        print("AssertionError:", error)
        return (1)
    return (0)


if __name__ == "__main__":
    main()
