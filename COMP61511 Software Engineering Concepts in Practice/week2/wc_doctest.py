def testAllInputs():
  """
  >>> import subprocess
  >>> try:
  ...   wcOut = subprocess.check_output("wc testinputs/* 2>&1", shell=True)
  ... except subprocess.CalledProcessError as exc:
  ...   wcOut = exc.output
  >>>
  >>> wcPyOut = subprocess.check_output("python3 wc.py testinputs/* 2>&1", shell=True)
  >>> wcOut = [str(s) for s in wcOut.split()]
  >>> wcPyOut = [str(s) for s in wcPyOut.split()]
  >>> wcOut == wcPyOut
  True
  """

# TODO Make the above vary generate combinations of flags.

if __name__ == "__main__":
  import doctest
  doctest.testmod()