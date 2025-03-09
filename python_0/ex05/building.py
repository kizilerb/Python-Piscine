import sys


def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return (1)
    elif len(sys.argv) == 1:
        print("What is the text to count?")
        str = sys.stdin.readline()
        if str == "":
            print("\nEOF detected. Exiting...")
            sys.exit(1)
    else:
        str = sys.argv[1]
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    upper_count = sum(1 for char in str if char.isupper())
    lower_cnt = sum(1 for char in str if char.islower())
    space_count = sum(1 for char in str if char == ' ')
    punc_count = sum(1 for char in str if char in punctuations)
    digit_count = sum(1 for char in str if char.isdigit())
    print("The text contains", len(str), "characters:")
    print(upper_count, " upper letters\n", lower_cnt, " lower letters", sep="")
    print(punc_count, " punctuation marks\n", space_count, " spaces", sep="")
    print(digit_count, " digits", sep="")


if __name__ == "__main__":
    main()
