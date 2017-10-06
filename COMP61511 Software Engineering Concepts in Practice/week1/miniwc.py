# Miniwc spec ( http://syllabus.cs.manchester.ac.uk/pgt/2017/COMP61511/labs/cw1/wc-first-implementation.html )
# miniwc is a work-alike for wc under the following restrictions:
#     1. There are no flag options.
#     2. The output is linecount wordcount bytecount filename (each separated by tab characters)
#     3. There is exactly one filepath passed as an argument.
#     4. That path argument is not stdin (i.e., “-”)
#     5. It should handle errors as wc, where errors include passing too many or the wrong arguments.
# Schematically, we restrict our UI to be equivalent to the following form: `wc <some file name which isn’t ‘-’>

# Miniwc spec (1) is satisfied implicitly. Filepaths starting with, but not equal to '-'
# will be treated as legitimate paths. Such file/folder names are possible under Linux and Windows.
# NOTE: I am purposely not copying the error wc prints (example below) when the wrong option is entered:
# wc: unrecognized option '-q'
# Try 'wc --help' for more information.
#
# This is because "unrecognized" implies some options are recognized, but in our case
# we cannot have any at all. Furthermore, wc suggests you use the '--help' option. Copying this
# message for the sake of creating a work-alike wouldn't make sense as we don't have options.
def miniwc(filepath):
    linecount = 0
    wordcount = 0
    bytecount = 0

    try:
        with open(filepath, 'rb') as f:
            for line in f:
                linecount += 1
                wordcount += len(line.split())
                bytecount += len(line)

    # Satisfies Miniwc spec (5) for wrong arguments
    except FileNotFoundError:
        return "wc: {}: No such file or directory".format(filepath)

    # Satisfies miniwc spec (2)
    return "{}\t{}\t{}\t{}".format(linecount, wordcount, bytecount, filepath)

if __name__ == "__main__":
    import sys

    # Satisfies Miniwc spec (3), (4) and the "too many arguments" part of (5)
    #
    # NOTE: miniwc spec (4) says the argument cannot be stdin. It does not explicitly tell us
    # that even files with the name of "-" can't be an argument. The UI restriction at the bottom
    # of the spec, however, does do that. Hence why the argument "-" is not allowed at all,
    # neither as stdin nor as a filename.
    if len(sys.argv) != 2 or sys.argv[1] == "-":
        # Prints usage according to restriction of UI in the miniwc spec above.
        print("usage: %s filepath" % sys.argv[0])
        sys.exit(1)
    else:
        print(miniwc(sys.argv[1]))
