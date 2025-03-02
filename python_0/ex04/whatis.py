import sys
if len(sys.argv) < 2:
    exit()
if len(sys.argv) > 2 :
    print("AssertionError: more than one argument is provided")
    exit()
try:
    arg = int(sys.argv[1])
    if (arg % 2 == 0):
        print("I'm Even.")
    else :
        print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer")
