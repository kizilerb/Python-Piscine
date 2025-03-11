import sys
"""
A real autonomous program, with a main, which takes
a single string argument and displays the sums of its
upper-case characters, lower-case
characters, punctuation characters, digits and spaces.
"""


def main():
    try:
        if len(sys.argv) > 2:
            """
            Parse: If more than one argument is provided to the program,
            print an AssertionError.
            """
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 1:
            """
            Parse: If None or nothing is provided,
            the user is prompted to provide a string.
            Expected outputs: (the carriage return counts as a space,
            if you don't want to return one use ctrl + D)
            """
            print("What is the text to count?")
            str = sys.stdin.readline()
            if str == "":
                print("\nEOF detected. Exiting...")
                return (0)
        else:
            str = sys.argv[1]
    except AssertionError as error:
        print("AssertionError:", error)
        return (1)
    """
    Checking the counts of different types of characters in the given argument
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
