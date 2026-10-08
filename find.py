# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    # TODO: add an optional flag -i / --ignore-case  (use action="store_true")

    parser.add_argument("-i", "--ignore-case", action="store_true")

    args = parser.parse_args()

    # TODO: open args.filename and read its lines. For each line, numbered starting
    #   at 1, print "<number>: <line>" when the line contains args.pattern.
    #   If the --ignore-case flag was given, match without caring about upper/lower
    #   case (hint: compare the lowercased versions of both).

    file_string = "";
    with open(args.filename, "r") as file:
        for line_num, line in enumerate(file, start=1):
            if args.ignore_case:
                if args.pattern in line.lower():
                    print(f"{line_num}: {line.rstrip("\n")}")
            else:
                if args.pattern in line:
                    print(f"{line_num}: {line.rstrip("\n")}")

if __name__ == "__main__":
    main()