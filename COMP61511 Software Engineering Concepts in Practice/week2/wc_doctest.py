def testAllInputs():
  """
  >>> import subprocess
  >>> from itertools import permutations
  >>> input = ["-", "-", "-", "w", "w", "c", "l"]
  >>> output = ""
  >>> output = [c for i in range(1, 4) for c in permutations(input,i)]
  >>> output = ["".join(a) for a in output]

  >>> passed, failed = 0, 0
  >>> for combo in output:
  ...   try:
  ...     wcOut = subprocess.check_output("wc testinputs/* 2>&1", shell=True)
  ...   except subprocess.CalledProcessError as exc:
  ...     wcOut = exc.output
  ...   wcPyOut = subprocess.check_output("python3 wc.py testinputs/* 2>&1", shell=True)
  ...   wcOut = [str(s) for s in wcOut.split()]
  ...   wcPyOut = [str(s) for s in wcPyOut.split()]
  ...   if wcOut == wcPyOut:
  ...     passed += 1
  ...   else:
  ...     failed += 1
  >>> print(passed, failed)
  259 0
  """

if __name__ == "__main__":
  import doctest
  doctest.testmod()