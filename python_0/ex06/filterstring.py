import sys
from ft_filter import ft_filter


def is_num(N):
    try:
        int(sys.argv[2])
        return (True)
    except ValueError:
        return (False)


def filterstring(str):
    separated = str.split()
    num = int(sys.argv[2])
    sorted = list(ft_filter(lambda i: 1 if len(i) > num else 0, separated))
    print(sorted)


def main():
    if len(sys.argv) == 3 and is_num(sys.argv[2]):
        filterstring(sys.argv[1])
    else:
        print("AssertionError: the arguments are bad")
        return (1)
    return (0)


if __name__ == "__main__":
    main()
