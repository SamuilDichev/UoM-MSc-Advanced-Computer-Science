OUTPUT = "\t{}\t{}\t{}\t{}"
FNF_ERR = "wc: {}: No such file or directory"

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


if __name__ == "__main__":
  import sys

  # TODO DO NOT FORGET TO HANDLE WILD CARDS (*)
  # TODO * should be expanded by bash on its own, so shouldn't need to handle it

  # wc spec (5)
  if len(sys.argv) < 2:
    print(FNF_ERR.format(""))
    sys.exit(1)
  else:
    totalLC, totalWC, totalBC = 0, 0, 0
    for filepath in sys.argv[1:]:

      # wc spec (5)
      if filepath == "-":
        print(FNF_ERR.format(filepath))
        continue

      try:
        result = processFile(filepath)
        totalLC += result[0]
        totalWC += result[1]
        totalBC += result[2]
        print(OUTPUT.format(result[0], result[1], result[2], filepath))
      except FileNotFoundError:
        print(FNF_ERR.format(filepath))

    if len(sys.argv) > 2:
      print(OUTPUT.format(totalLC, totalWC, totalBC, "total"))
