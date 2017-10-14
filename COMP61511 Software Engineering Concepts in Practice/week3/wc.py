FNF_ERR = "wc: {}: No such file or directory"
DIR_ERR = "wc: {}: Is a directory"
PERMISSION_ERROR = "wc: {}: Permission denied"
LONG_OPT_ERR = "wc: unrecognised option '{}'\nTry 'wc --help' for more information."
SHORT_OPT_ERR = "wc: invalid option -- '{}'\nTry 'wc --help' for more information."
ALLOWED_OPTIONS = ["l", "w", "c"]

# WHAT THE FUCK, wc?
ESCAPED_SYMBOLS = ["!", "~", "#", "$", "^", "&", "*", "(", ")", "=", "<", ">", "?", ";", ":", "[", "{", "]", "}", "|"]

def processFile(filepath):
  linecount, wordcount, bytecount = 0, 0, 0

  with open(filepath, 'rb') as f:
    for line in f:
      linecount += line.count(b'\n')
      wordcount += len(line.split())
      bytecount += len(line)

  return linecount, wordcount, bytecount, filepath

def processFiles(files):
  totalLC, totalWC, totalBC = 0, 0, 0

  for file in files:
    try:
      result = processFile(file)
      lc, wc, bc = result[0], result[1], result[2]
      totalLC += lc
      totalWC += wc
      totalBC += bc

      printOutput(lc, wc, bc, file, options)
    except FileNotFoundError:
      for c in file:
        if str(c) in ESCAPED_SYMBOLS:
          file = "'{}'".format(file)
          break

      eprint(FNF_ERR.format(file))
    except IsADirectoryError:
      eprint(DIR_ERR.format(file))
      printOutput(0, 0, 0, file, options)
    except PermissionError:
      eprint(PERMISSION_ERROR.format(file))

  if len(files) > 1:
    printOutput(totalLC, totalWC, totalBC, "total", options)

def createArgParser():
  global parser
  parser = argparse.ArgumentParser(add_help=False)

  for option in ALLOWED_OPTIONS:
    parser.add_argument("-{}".format(option), "--{}".format(option), action="store_true")

  parser.add_argument("FILE", nargs="*")

def getOptions(args):
  options = []
  for arg,v in vars(args).items():
    if v == True:
      options.append(arg)

  return options

def handleBadArgs(args):
  if str(args[0]).startswith("--"):
    eprint(LONG_OPT_ERR.format(args[0]))
  else:
    eprint(SHORT_OPT_ERR.format(args[0][1:]))

  sys.exit(1)

def printOutput(lc, wc, bc, last, options):
  output = ""
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

if __name__ == "__main__":
  import sys
  import argparse

  createArgParser()
  args, badArgs = parser.parse_known_args(sys.argv[1:])

  if len(badArgs) > 0:
    handleBadArgs(badArgs)

  if len(sys.argv) < 2:
    eprint(FNF_ERR.format(""))
    sys.exit(1)
  else:
    options = getOptions(args)
    processFiles(args.FILE)