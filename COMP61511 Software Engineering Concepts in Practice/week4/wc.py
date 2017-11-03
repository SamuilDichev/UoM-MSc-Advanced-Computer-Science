import sys
import argparse

FNF_ERR = "wc: {}: No such file or directory"
FNF_ERR2 = "wc: cannot open '{}' for reading: No such file or directory"
ZERO_LENGTH_FILE = "wc: invalid zero-length file name"
DIR_ERR = "wc: {}: Is a directory"
NOT_DIR_ERR = "wc: {}: Not a directory"
PERMISSION_ERROR = "wc: {}: Permission denied"
LONG_OPT_ERR = "wc: unrecognised option '{}'\nTry 'wc --help' for more information."
SHORT_OPT_ERR = "wc: invalid option -- '{}'\nTry 'wc --help' for more information."
EXTRA_OP_ERR = """wc: extra operand '%s'
file operands cannot be combined with --files0-from
Try 'wc --help' for more information."""

# WHAT THE FUCK, wc?
ESCAPED_SYMBOLS = [" ", "!", "~", "#", "$", "^", "&", "*", "(", ")", "=", "<", ">", "?", ";", ":", "[", "{", "]", "}", "|"]

def processFile(filepath):
  linecount, wordcount, charcount, bytecount, maxlc = 0, 0, 0, 0, 0

  lfChar = b'\n'
  if filepath == "-" or filepath == None:
    f = sys.stdin
    lfChar = '\n'
    filepath = ""
  elif filepath == "":
    eprint(ZERO_LENGTH_FILE)
    raise NameError
  else:
    f = open(filepath, 'rb')

  for line in f:
    linecount += line.count(lfChar)
    wordcount += len(line.split())

    try:
      charcount += len(line.decode("utf8"))
    except (UnicodeDecodeError, AttributeError):
      charcount += len(line)

    bytecount += len(line)

    if len(line) > maxlc:
      maxlc = len(line)

  f.close()

  return {"lc": linecount, "maxlc": maxlc, "wc": wordcount, "cc": charcount, "bc": bytecount, "fp": filepath}

def processFiles(filepaths, options):
  totals = {"lc": 0, "maxlc": 0, "wc": 0, "cc": 0, "bc": 0, "fp": "total"}
  for filepath in filepaths:
    try:
      results = processFile(filepath)
      totals["lc"] += results.get("lc")
      totals["wc"] += results.get("wc")
      totals["cc"] += results.get("cc")
      totals["bc"] += results.get("bc")

      if results.get("maxlc") > totals.get("maxlc"):
        totals["maxlc"] = results.get("maxlc")

      printOutput(results, options)
    except FileNotFoundError:
      eprint(FNF_ERR.format(escapeIllegalSymbols(filepath)))
    except IsADirectoryError:
      eprint(DIR_ERR.format(escapeIllegalSymbols(filepath)))
      printOutput({"lc": 0, "wc": 0, "cc": 0, "bc": 0, "fp": filepath}, options)
    except PermissionError:
      eprint(PERMISSION_ERROR.format(escapeIllegalSymbols(filepath)))
    except NotADirectoryError:
      eprint(NOT_DIR_ERR.format(filepath))
      sys.exit(1)
    except NameError:
      pass
    except KeyboardInterrupt:
      sys.exit(130)

  if len(filepaths) > 1:
    printOutput(totals, options)

def escapeIllegalSymbols(string):
  for s in ESCAPED_SYMBOLS:
    if string.__contains__(s):
      return "'{}'".format(string)

  return string

def createArgParser():
  parser = argparse.ArgumentParser(add_help=False)

  parser.add_argument("-l", "--l", "--lines", action="store_true", dest="l")
  parser.add_argument("-w", "--w", "--words", action="store_true", dest="w")
  parser.add_argument("-c", "--c", "--bytes", action="store_true", dest="c")
  parser.add_argument("-m", "--m", "--chars", action="store_true", dest="m")
  parser.add_argument("-L", "--max-line-length", action="store_true", dest="L")
  parser.add_argument("--h", "--help", action="store_true", dest="help")
  parser.add_argument("--version", action="store_true", dest="version")
  parser.add_argument("--f", "--files0-from", action="store", dest="f")

  parser.add_argument("FILE", nargs="*")

  return parser

def getOptions(namespace):
  options = []
  for arg,v in vars(namespace).items():
    if v == True:
      options.append(arg)

  return options

"""
Always prints an error as it expects it's always given bad args.
Does not do any checking if the arguments are actually bad, simply formats the error
correctly according to the type / length of the arguments.
"""
def printBadArgsError(args):
  if str(args[0]).startswith("--"):
    eprint(LONG_OPT_ERR.format(args[0]))
  else:
    eprint(SHORT_OPT_ERR.format(args[0][1:]))

def printOutput(results, options):
  output = ""
  options = [o for o in options if o in ["l", "w", "m", "c", "L"]]

  if "l" in options or len(options) == 0:
    output += "\t{}".format(results.get("lc"))
  if "w" in options or len(options) == 0:
    output += "\t{}".format(results.get("wc"))
  if "m" in options:
    output += "\t{}".format(results.get("cc"))
  if "c" in options or len(options) == 0:
    output += "\t{}".format(results.get("bc"))
  if "L" in options:
    output += "\t{}".format(results.get("maxlc"))

  output += "\t{}".format(results.get("fp"))

  print(output)

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

def preprocessArgs(args):
  flags = []
  files = []
  onlyFilesLeft = False
  for arg in args:
    if str(arg) == "--":
      onlyFilesLeft = True

    if not onlyFilesLeft and not isFileArg(arg):
      flags.append(arg)
    elif onlyFilesLeft or isFileArg(arg):
      files.append(arg)

  return flags + files

def isFileArg(arg):
  return not str(arg).startswith("-") or str(arg) == "-" or str(arg) == "--"

def printHelp():
  print("""Usage: wc [OPTION]... [FILE]...
  or:  wc [OPTION]... --files0-from=F
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  With no FILE, or when FILE is -,
read standard input.  A word is a non-zero-length sequence of characters
delimited by white space.
The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
      --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
  -L, --max-line-length  print the length of the longest line
  -w, --words            print the word counts
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
For complete documentation, run: info coreutils 'wc invocation'""")

def printVersion():
  print("""wc (GNU coreutils) 8.22
Copyright (C) 2013 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Paul Rubin and David MacKenzie.""")

def getFilesFrom0(filepath):
  with open(filepath, 'rb') as f:
    files = f.read().split(b'\x00')

  newFiles = []
  for file in files:
    file = file.decode()
    newFiles.append(file)

  return newFiles

if __name__ == "__main__":
  parser = createArgParser()
  args = preprocessArgs(sys.argv[1:])
  args, badArgs = parser.parse_known_args(args)

  if len(badArgs) > 0:
    printBadArgsError(badArgs)
    sys.exit(1)

  for arg in sys.argv[1:]:
    if arg == "--help" or arg == "--h":
      printHelp()
      sys.exit(0)
    elif arg == "--version" or arg == "--v":
      printVersion()
      sys.exit(0)

  files = args.FILE
  if args.f and len(args.FILE) == 0:
    try:
      files = getFilesFrom0(args.f)
    except FileNotFoundError:
      eprint(FNF_ERR2.format(args.f))
      sys.exit(1)
  elif args.f and len(args.FILE) > 0:
    eprint(EXTRA_OP_ERR % args.FILE[0])
    sys.exit(1)

  if len(files) == 0:
    processFiles([None], getOptions(args))
  else:
    processFiles(files, getOptions(args))