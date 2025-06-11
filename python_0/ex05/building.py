import sys


def main():
    """
    Argument validity is checked and if it is not an valid argument for
    example there is more than one argument AssertionError exception's raised.
    If there is no argument is given, the argument is taken through readline
    function. Readline function is also used to provide control-D functioning.
    Arguments are taken with sys.argv in list type.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 1:
            print("What is the text to count?")
            str = sys.stdin.readline()
            if str == "":
                print("\nEOF detected. Exiting...")
                return (0)
        else:
            str = sys.argv[1]
        process_str(str)
    except AssertionError as error:
        print("AssertionError:", error)
        return (1)


def process_str(str):
    """
    Checking the counts of different types of characters in the given
    argument by sum() function. After getting counts of upper-case characters
    lower-case, characters, punctuation characters, digits and spaces, it is
    displayed thorugh print() function.
    """
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    upper_count = sum(1 for char in str if char.isupper())
    lower_cnt = sum(1 for char in str if char.islower())
    space_count = sum(1 for char in str if char == ' ')
    punc_count = sum(1 for char in str if char in punctuations)
    digit_count = sum(1 for char in str if char.isdigit())
    # Printing taken counts as an output.
    print("The text contains", len(str), "characters:")
    print(upper_count, " upper letters\n", lower_cnt, " lower letters", sep="")
    print(punc_count, " punctuation marks\n", space_count, " spaces", sep="")
    print(digit_count, "digits")


if __name__ == "__main__":
    main()
