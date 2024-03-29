import sys
import argparse

FNF_ERR = "wc: {}: No such file or directory"
ZERO_LENGTH_FILE = "wc: invalid zero-length file name"
DIR_ERR = "wc: {}: Is a directory"
PERMISSION_ERROR = "wc: {}: Permission denied"
LONG_OPT_ERR = "wc: unrecognised option '{}'\nTry 'wc --help' for more information."
SHORT_OPT_ERR = "wc: invalid option -- '{}'\nTry 'wc --help' for more information."
ALLOWED_OPTIONS = ["l", "w", "c"]

# WHAT THE FUCK, wc?
ESCAPED_SYMBOLS = [" ", "!", "~", "#", "$", "^", "&", "*", "(", ")", "=", "<", ">", "?", ";", ":", "[", "{", "]", "}", "|"]

def processFile(filepath):
  linecount, wordcount, bytecount = 0, 0, 0

  with open(filepath, 'rb') as f:
    for line in f:
      linecount += line.count(b'\n')
      wordcount += len(line.split())
      bytecount += len(line)

  return linecount, wordcount, bytecount, filepath

def processFiles(filepaths, options):
  totalLC, totalWC, totalBC = 0, 0, 0

  for filepath in filepaths:
    try:
      result = processFile(filepath)
      lc, wc, bc = result[0], result[1], result[2]
      totalLC += lc
      totalWC += wc
      totalBC += bc

      printOutput(lc, wc, bc, filepath, options)
    except FileNotFoundError:
      eprint(FNF_ERR.format(escapeIllegalSymbols(filepath)))
    except IsADirectoryError:
      eprint(DIR_ERR.format(escapeIllegalSymbols(filepath)))
      printOutput(0, 0, 0, filepath, options)
    except PermissionError:
      eprint(PERMISSION_ERROR.format(escapeIllegalSymbols(filepath)))

  if len(filepaths) > 1:
    printOutput(totalLC, totalWC, totalBC, "total", options)

def escapeIllegalSymbols(string):
  for c in string:
    if str(c) in ESCAPED_SYMBOLS:
      return "'{}'".format(string)

  return string

def createArgParser():
  parser = argparse.ArgumentParser(add_help=False)

  for option in ALLOWED_OPTIONS:
    parser.add_argument("-{}".format(option), "--{}".format(option), action="store_true")

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

def printOutput(lc, wc, bc, last, options):
  output = ""
  options = [o for o in options if o in ALLOWED_OPTIONS]

  if ALLOWED_OPTIONS[0] in options or len(options) == 0:
    output += "\t{}".format(lc)
  if ALLOWED_OPTIONS[1] in options or len(options) == 0:
    output += "\t{}".format(wc)
  if ALLOWED_OPTIONS[2] in options or len(options) == 0:
    output += "\t{}".format(bc)

  output += "\t{}".format(last)

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

if __name__ == "__main__":
  parser = createArgParser()
  args = preprocessArgs(sys.argv[1:])
  args, badArgs = parser.parse_known_args(args)

  if len(badArgs) > 0:
    printBadArgsError(badArgs)
    sys.exit(1)

  # TODO Which error? Invalid zero-length or no such file?
  if len(sys.argv) < 2:
    eprint(FNF_ERR.format(""))
    sys.exit(1)
  else:
    processFiles(args.FILE, getOptions(args))