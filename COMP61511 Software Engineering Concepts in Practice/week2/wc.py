FNF_ERR = "wc: {}: No such file or directory"
DIR_ERR = "wc: {}: Is a directory"
LONG_OPT_ERR = "wc: unrecognised option '{}'\nTry 'wc --help' for more information."
SHORT_OPT_ERR = "wc: invalid option -- '{}'\nTry 'wc --help' for more information."
ALLOWED_OPTIONS = ["l", "w", "c"]

def processFile(filepath):
  linecount, wordcount, bytecount = 0, 0, 0

  try:
    with open(filepath, 'rb') as f:
      for line in f:
        linecount += 1
        wordcount += len(line.split())
        bytecount += len(line)

  except FileNotFoundError:
    raise

  return linecount, wordcount, bytecount, filepath

def getOptions():
  options = []
  for arg in sys.argv[1:]:
    if arg == "-":
      continue
    elif str(arg).startswith("--"):
      longOpts = getLongOptions(arg)
      if longOpts:
        options.append(longOpts)
    elif str(arg).startswith("-"):
      shortOpts = getShortOptions(arg)
      if shortOpts:
        options.extend(shortOpts)

  return list(set(options))

def getLongOptions(arg):
  if arg[2:] in ALLOWED_OPTIONS:
    return arg[2:]
  else:
    print(LONG_OPT_ERR.format(arg))
    sys.exit(1)

def getShortOptions(arg):
  options = []
  for c in arg[1:]:
    if c in ALLOWED_OPTIONS:
      options.append(c)
    else:
      print(SHORT_OPT_ERR.format(c))
      sys.exit(1)

  return options

def printOutput(lc, wc, bc, last, options):
  args = []
  output = ""

  if ALLOWED_OPTIONS[0] in options or len(options) == 0:
    args.append(lc)
  if ALLOWED_OPTIONS[1] in options or len(options) == 0:
    args.append(wc)
  if ALLOWED_OPTIONS[2] in options or len(options) == 0:
    args.append(bc)

  args.append(last)

  for arg in args:
    output += "\t" + str(arg)

  print(output)

if __name__ == "__main__":
  import sys

  # TODO args "*" and \* are quoted in '' by wc, but not by wc.py. E.g.
  # TODO $ wc: '*': No such file or directory
  # TODO $ wc: *: No such file or directory

  # TODO I've not considered Folders and PDFs. Check how wc handles them.

  # TODO If arg before a flag is -- then flag is considered a file name?

  # wc spec (5)
  if len(sys.argv) < 2:
    print(FNF_ERR.format(""))
    sys.exit(1)
  else:
    totalLC, totalWC, totalBC = 0, 0, 0
    files = 0
    options = getOptions()
    for arg in sys.argv[1:]:

      # wc spec (5)
      if arg == "-":
        print(FNF_ERR.format(arg))
        continue

      if str(arg).startswith("-"):
        continue

      try:
        files += 1
        result = processFile(arg)
        lc, wc, bc = result[0], result[1], result[2]
        totalLC += lc
        totalWC += wc
        totalBC += bc

        printOutput(lc, wc, bc, arg, options)
      except FileNotFoundError:
        print(FNF_ERR.format(arg))
      except IsADirectoryError:
        print(DIR_ERR.format(arg))
        printOutput(0, 0, 0, arg, options)

    if files > 1:
      printOutput(totalLC, totalWC, totalBC, "total", options)