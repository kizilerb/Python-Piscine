import sys
from ft_filter import ft_filter

def filterstring(str):
    sort = lambda input: True if len(input) > int(sys.argv[2]) else False
    separate = str.split()
    sorted = list(ft_filter(sort, separate))
    print(sorted)

def main():
    if len(sys.argv) == 3:
        try:
            number = int(sys.argv[2])
        except ValueError:
            print("AssertionError: the arguments are bad")
            return(1)
        filterstring(sys.argv[1])
    else:
        print("AssertionError: the arguments are bad")
        return(1)
    return(0)

if __name__ == "__main__":
    main()