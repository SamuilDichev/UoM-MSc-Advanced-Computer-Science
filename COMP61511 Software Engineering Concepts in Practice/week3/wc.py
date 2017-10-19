import sys
import argparse
import time

FNF_ERR = "wc: {}: No such file or directory"
ZERO_LENGTH_FILE = "wc: invalid zero-length file name"
DIR_ERR = "wc: %s: Is a directory"
PERMISSION_ERROR = "wc: %s: Permission denied"
LONG_OPT_ERR = "wc: unrecognised option '%s'\nTry 'wc --help' for more information."
SHORT_OPT_ERR = "wc: invalid option -- '%s'\nTry 'wc --help' for more information."
ALLOWED_OPTIONS = ["l", "w", "c"]
TIMES = []

# WHAT THE FUCK, wc?
ESCAPED_SYMBOLS = [" ", "!", "~", "#", "$", "^", "&", "*", "(", ")", "=", "<", ">", "?", ";", ":", "[", "{", "]", "}", "|"]

def processFile(filepath):
  start = time.time()
  with open(filepath, 'rb') as f:
    # for line in f:
    #   linecount += line.count(b'\n')
    #   wordcount += len(line.split())
    #   bytecount += len(line)
    file = f.read()
    linecount = file.count(b'\n')
    wordcount = len(file.split())
    bytecount = len(file)

  end = time.time()
  TIMES.append("Time for processFile: %s" % end - start)

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
      eprint(FNF_ERR % escapeIllegalSymbols(filepath))
    except IsADirectoryError:
      eprint(DIR_ERR % escapeIllegalSymbols(filepath))
      printOutput(0, 0, 0, filepath, options)
    except PermissionError:
      eprint(PERMISSION_ERROR % escapeIllegalSymbols(filepath))

  if len(filepaths) > 1:
    printOutput(totalLC, totalWC, totalBC, "total", options)

def escapeIllegalSymbols(string):
  start = time.time()
  for c in string:
    if str(c) in ESCAPED_SYMBOLS:
      return "'%s'" % string

  end = time.time()
  TIMES.append("Time for escapeIllegalSymbols: %s" % end - start)

  return string

def createArgParser():
  start = time.time()
  parser = argparse.ArgumentParser(add_help=False)

  for option in ALLOWED_OPTIONS:
    parser.add_argument("-%s"% option, "--%s" % option, action="store_true")

  parser.add_argument("FILE", nargs="*")

  end = time.time()
  TIMES.append("Time for createArgParser: %s" % end - start)

  return parser

def getOptions(namespace):
  start = time.time()

  options = []
  for arg,v in vars(namespace).items():
    if v == True:
      options.append(arg)

  end = time.time()
  TIMES.append("Time for getOptions: %s" % end - start)

  return options

"""
Always prints an error as it expects it's always given bad args.
Does not do any checking if the arguments are actually bad, simply formats the error
correctly according to the type / length of the arguments.
"""
def printBadArgsError(args):
  start = time.time()
  if str(args[0]).startswith("--"):
    eprint(LONG_OPT_ERR % args[0])
  else:
    eprint(SHORT_OPT_ERR % args[0][1:])
  end = time.time()
  TIMES.append("Time for printBadArgsError: %s" % end - start)

def printOutput(lc, wc, bc, last, options):
  start = time.time()
  output = ""
  options = [o for o in options if o in ALLOWED_OPTIONS]

  if ALLOWED_OPTIONS[0] in options or len(options) == 0:
    output += "\t%s" % lc
  if ALLOWED_OPTIONS[1] in options or len(options) == 0:
    output += "\t%s" % wc
  if ALLOWED_OPTIONS[2] in options or len(options) == 0:
    output += "\t%s" % bc

  output += "\t%s" % last

  print(output)
  end = time.time()
  TIMES.append("Time for printOutput: %s" % end - start)

def eprint(*args, **kwargs):
  start = time.time()
  print(*args, file=sys.stderr, **kwargs)
  end = time.time()
  TIMES.append("Time for eprint: %s" % end - start)

def preprocessArgs(args):
  flags, files = [], []
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
    eprint(FNF_ERR % "")
    sys.exit(1)
  else:
    processFiles(args.FILE, getOptions(args))