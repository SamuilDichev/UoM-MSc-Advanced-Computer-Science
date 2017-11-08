def generateTest():
  with open("tests.txt", "w") as f:
    f.write(">>> import subprocess\n")
    for flags in generateFlagPermutations()[1:]:
        f.write(generateTestString(flags))

def generateTestString(flags):
  testStr = (">>> subprocess.check_output(\"python3 wc.py {} testinputs/* 2>/dev/null\", shell=True)\n"
  "{}\n"
  ">>> subprocess.check_output(\"python3 wc.py {} testinputs/* 2>&1 >/dev/null\", shell=True)\n"
  "{}\n").format(flags, getExpectedStdout(flags), flags, getExpectedStderr(flags))
  return testStr

def getExpectedStdout(flags):
  try:
    wcOut = subprocess.check_output("wc {} testinputs/* 2>/dev/null".format(flags), shell=True)
  except subprocess.CalledProcessError as e:
    wcOut = e.output

  wcOut = "\\t".join(str(wcOut).split())

  return wcOut

def getExpectedStderr(flags):
  try:
    wcOut = subprocess.check_output("wc {} testinputs/* 2>&1 >/dev/null".format(flags), shell=True)
  except subprocess.CalledProcessError as e:
    wcOut = e.output

  return wcOut

def generateFlagPermutations():
  perms_input = ["-", "w", "w", "c", "l"]
  output = [c for i in range(1, 4) for c in permutations(perms_input, i)]
  output = ["".join(a) for a in output]
  return output

if __name__ == "__main__":
  import doctest
  import subprocess
  from itertools import permutations
  generateTest()
  doctest.testfile("tests.txt")