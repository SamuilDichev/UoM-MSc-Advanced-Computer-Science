OUTPUT = "\t{}\t{}\t{}\t{}"
FNF_ERR = "wc: {}: No such file or directory"
UNKNOWN_OPT_ERR = "wc: unknown option -- {}\nTry 'wc --help' for more information."
OPTIONS = ["l", "w", "c"]

def processFile(filepath, options=0):
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
    if arg != "-" and str(arg).startswith("-"):
      if not isOption(arg):
        print(UNKNOWN_OPT_ERR.format(arg[0:]))
        sys.exit(1)

  return options

def isOption(arg):
  return str(arg).count("-") <= 2


if __name__ == "__main__":
  import sys

  # TODO DO NOT FORGET TO HANDLE WILD CARDS (*)
  # TODO * should be expanded by bash on its own, so shouldn't need to handle it
  # TODO But maybe for Windows?

  # TODO * arg on Windows throws exceptions.
  # TODO Check if "*" on Linux does too and compare to wc, to see if identical.

  # TODO I've not considered Folders and PDFs. Check how wc handles them.

  # wc spec (5)
  if len(sys.argv) < 2:
    print(FNF_ERR.format(""))
    sys.exit(1)
  else:
    totalLC, totalWC, totalBC = 0, 0, 0
    options = getOptions()
    for arg in sys.argv[1:]:

      # wc spec (5)
      if arg == "-":
        print(FNF_ERR.format(arg))
        continue

      if str(arg).startswith("-"):
        continue

      try:
        result = processFile(arg)
        lc, wc, bc = result[0], result[1], result[2]
        totalLC += lc
        totalWC += wc
        totalBC += bc
        print(OUTPUT.format(lc, wc, bc, arg))
      except FileNotFoundError:
        print(FNF_ERR.format(arg))

    if len(sys.argv) > 2:
      print(OUTPUT.format(totalLC, totalWC, totalBC, "total"))

    print(options)

