import sys
from ft_filter import ft_filter

def is_num(N):
    try:
        int(sys.argv[2])
        return(True)
    except ValueError:
        return(False)

def filterstring(str):
    sort_func = lambda input: True if len(input) > int(sys.argv[2]) else False
    separated = str.split()
    sorted = list(ft_filter(sort_func, separated))
    print(sorted)

def main():
    if len(sys.argv) == 3 and is_num(sys.argv[2]):
        filterstring(sys.argv[1])
    else:
        print("AssertionError: the arguments are bad")
        return(1)
    return(0)

if __name__ == "__main__":
    main()