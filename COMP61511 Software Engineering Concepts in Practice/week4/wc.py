import sys
import argparse

FNF_ERR = "wc: {}: No such file or directory"
ZERO_LENGTH_FILE = "wc: invalid zero-length file name"
DIR_ERR = "wc: {}: Is a directory"
PERMISSION_ERROR = "wc: {}: Permission denied"
LONG_OPT_ERR = "wc: unrecognised option '{}'\nTry 'wc --help' for more information."
SHORT_OPT_ERR = "wc: invalid option -- '{}'\nTry 'wc --help' for more information."

# WHAT THE FUCK, wc?
ESCAPED_SYMBOLS = [" ", "!", "~", "#", "$", "^", "&", "*", "(", ")", "=", "<", ">", "?", ";", ":", "[", "{", "]", "}", "|"]

def processFile(filepath):
  linecount, wordcount, bytecount, maxlc = 0, 0, 0, 0

  with open(filepath, 'rb') as f:
    for line in f:
      linecount += line.count(b'\n')
      wordcount += len(line.split())
      bytecount += len(line)

      if len(line) > maxlc:
        maxlc = len(line)

  return {"lc": linecount, "maxlc": maxlc, "wc": wordcount, "cc": bytecount, "bc": bytecount, "fp": filepath}

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

  if len(filepaths) > 1:
    printOutput(totals, options)

def escapeIllegalSymbols(string):
  for c in string:
    if str(c) in ESCAPED_SYMBOLS:
      return "'{}'".format(string)

  return string

def createArgParser():
  parser = argparse.ArgumentParser(add_help=False)

  parser.add_argument("-l", "--l", "--lines", action="store_true", dest="l")
  parser.add_argument("-w", "--w", "--words", action="store_true", dest="w")
  parser.add_argument("-c", "--c", "--bytes", action="store_true", dest="c")
  parser.add_argument("-m", "--m", "--chars", action="store_true", dest="m")
  parser.add_argument("-L", "--max-line-length", action="store_true", dest="L")
  parser.add_argument("--help", action="store_true", dest="help")
  parser.add_argument("--version", action="store_true", dest="version")

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
more than one FILE is specified.  A word is a non-zero-length sequence of
characters delimited by white space.

With no FILE, or when FILE is -, read standard input.

The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
      --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
  -L, --max-line-length  print the maximum display width
  -w, --words            print the word counts
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/wc>
or available locally via: info '(coreutils) wc invocation'""")

def printVersion():
  print("""wc (GNU coreutils) 8.25
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Paul Rubin and David MacKenzie.""")

if __name__ == "__main__":
  parser = createArgParser()
  args = preprocessArgs(sys.argv[1:])
  args, badArgs = parser.parse_known_args(args)

  if len(badArgs) > 0:
    printBadArgsError(badArgs)
    sys.exit(1)

  for arg in sys.argv[1:]:
    if arg == "--help":
      printHelp()
      sys.exit(0)
    elif arg == "--version":
      printVersion()
      sys.exit(0)

  # TODO Which error? Invalid zero-length or no such file?
  if len(sys.argv) < 2:
    eprint(FNF_ERR.format(""))
    sys.exit(1)
  else:
    processFiles(args.FILE, getOptions(args))