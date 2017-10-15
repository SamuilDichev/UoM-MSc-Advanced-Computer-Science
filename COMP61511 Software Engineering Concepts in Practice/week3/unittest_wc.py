import unittest
import sys
from contextlib import contextmanager
from io import StringIO

class TestStringMethods(unittest.TestCase):



  def test_parser(self):
    from .wc import createArgParser

    parser = createArgParser()
    args, badArgs = parser.parse_known_args("-lc filepath1 --w filepath2 -- -z".split())

    # TODO filepath2 is unrecognized.
    self.assertTrue(args.c)
    self.assertTrue(args.l)
    self.assertTrue(args.w)

    # TODO finish the below
    # self.assertEqual(args.FILE, "filepath1", "filepath2")

  def test_getOptions(self):
    from .wc import getOptions
    from argparse import Namespace

    namespace = Namespace(z=True, b=False, c=True, d=False, o=2, l="s")

    options = getOptions(namespace)
    self.assertEqual(len(options), 2)
    self.assertTrue(options.__contains__("c"))
    self.assertTrue(options.__contains__("z"))
    self.assertFalse(options.__contains__("b"))
    self.assertFalse(options.__contains__("d"))
    self.assertFalse(options.__contains__("o"))
    self.assertFalse(options.__contains__("l"))

  def test_processFile(self):
    import os
    from .wc import processFile

    # Get absolute path to "testinputs"
    testdir = os.path.join(os.path.dirname(__file__), "testinputs")

    # Get all files in "testinputs"
    files = os.listdir(testdir)
    self.assertNotEqual(len(files), 0)

    for file in files:
      filepath = os.path.join(testdir, file)

      linecount, wordcount, bytecount, filepath = processFile(filepath)
      result = "{} {} {} {}\n".format(linecount, wordcount, bytecount, filepath)
      wcStdout = self.getExpectedStdout("", "'{}'".format(filepath))

      self.assertEqual("".join(result.split()), "".join(wcStdout.split()))

  def test_processFiles(self):
    import os
    from .wc import processFiles
    import subprocess

    # Get absolute path to "testinputs"
    testdir = os.path.join(os.path.dirname(__file__), "testinputs")

    # Get all files in "testinputs"
    files = subprocess.check_output("ls '{}'".format(testdir), shell=True).decode().split()

    # Join absolute path of "testinputs" with the filenames to get absolute paths for all files.
    filepaths = []
    for file in files:
      filepaths.append(os.path.join(testdir, file))

    filepaths.append(os.path.join(testdir, "qwerty-non-existent-file-hopefully"))
    filepaths.append(testdir)
    filepaths.append("/etc/sudoers")
    filepaths.append("/etc/shadow")
    filepaths.append("/etc/passwd")

    # Extract stderr and stdout as variables, so we can compare results
    with self.captured_output() as (stdout, stderr):
      """
      Testing with only good options as this function doesn't actually handle options, it merely passes them onto
      the print function which is tested in another test
      """
      options = ["c", "w", "l"]
      processFiles(filepaths, options)

    output = stdout.getvalue().strip()
    errors = stderr.getvalue().strip()

    # Create a filepath string (all filepaths in a string, each quotes and each separated by a space
    filepathsString = ""
    for filepath in filepaths:
      filepathsString += "'{}' ".format(filepath)

    wcStdout = self.getExpectedStdout("-cwl", filepathsString)
    wcStderr = self.getExpectedStderr("-cwl", filepathsString)

    self.assertEqual("".join(str(output).split()), "".join(wcStdout.split()))
    self.assertEqual("".join(str(errors).split()), "".join(wcStderr.split()))

  # TODO test escapeIllegalSymbols()
  # TODO test handleBadArgs()
  # TODO test printOutput()
  # TODO test eprint()

  """
  Used to retrieve the stdout of GNU wc for certain file and flags, so it can be compared
  to the output of my program or certain units of it
  """
  def getExpectedStdout(self, flags, filepath):
    import subprocess

    try:
      wcOut = subprocess.check_output("wc {} {} 2>/dev/null".format(flags, filepath), shell=True)
    except subprocess.CalledProcessError as e:
      wcOut = e.output

    return wcOut.decode()

  """
  Used to retrieve the stderr of GNU wc for certain file and flags, so it can be compared
  to the output of my program or certain units of it
  """
  def getExpectedStderr(self, flags, filepath):
    import subprocess

    try:
      wcErr = subprocess.check_output("wc {} {} 2>&1 >/dev/null".format(flags, filepath), shell=True)
    except subprocess.CalledProcessError as e:
      wcErr = e.output

    return wcErr.decode()

  """
  Captures stdout and stderr, so they can be compared to expected output
  """
  @contextmanager
  def captured_output(self):
    my_stdout, my_stderr = StringIO(), StringIO()
    default_stdout, default_stderr = sys.stdout, sys.stderr

    try:
      sys.stdout, sys.stderr = my_stdout, my_stderr
      yield sys.stdout, sys.stderr
    finally:
      sys.stdout, sys.stderr = default_stdout, default_stderr

  """
  Generates all possible permutations (Up to size of 4) of some flags
  """
  def generateFlagPermutations(self):
    from itertools import permutations

    perms_input = ["-", "w", "w", "c", "l"]
    output = [c for i in range(1, 4) for c in permutations(perms_input, i)]
    output = ["".join(a) for a in output]
    return output

if __name__ == '__main__':
    unittest.main()