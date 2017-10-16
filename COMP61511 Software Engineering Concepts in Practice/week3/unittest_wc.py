import unittest
import sys
from contextlib import contextmanager
from io import StringIO

class TestStringMethods(unittest.TestCase):

  def test_parser(self):
    from .wc import createArgParser
    from .wc import preprocessArgs

    parser = createArgParser()
    args = "txt1 -l txt2 --flag2 txt3 -- -w txt4 -- --w txt5 -- txt6 - txt7 -- - txt8 -c".split()
    args, badArgs = parser.parse_known_args(preprocessArgs(args))

    self.assertFalse(args.c)
    self.assertTrue(args.l)
    self.assertFalse(args.w)

    self.assertEqual(args.FILE, "txt1 txt2 txt3 -w txt4 -- --w txt5 -- txt6 - txt7 -- - txt8 -c".split())

  def test_isFileArg(self):
    from .wc import isFileArg
    self.assertFalse(isFileArg("-asasda"))
    self.assertFalse(isFileArg("-c"))
    self.assertTrue(isFileArg("--"))
    self.assertTrue(isFileArg("asdas"))

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
      Testing only good options (only valid) as this function doesn't actually handle options,
      it merely passes them onto the print function which is tested in another unit test
      """
      options = ["c", "w", "l"]
      processFiles(filepaths, options)

    output = stdout.getvalue()
    errors = stderr.getvalue()

    # Create a filepath string (all filepaths in a string, each quotes and each separated by a space
    filepathsString = ""
    for filepath in filepaths:
      filepathsString += "'{}' ".format(filepath)

    wcStdout = self.getExpectedStdout("-cwl", filepathsString)
    wcStderr = self.getExpectedStderr("-cwl", filepathsString)

    self.assertEqual("".join(str(output).split()), "".join(wcStdout.split()))
    self.assertEqual("".join(str(errors).split()), "".join(wcStderr.split()))

  def test_escapeIllegalSymbols(self):
    from .wc import escapeIllegalSymbols
    illegalSymbols = [" ", "!", "~", "#", "$", "^", "&", "*", "(", ")", "=", "<", ">", "?", ";", ":", "[", "{", "]", "}", "|"]
    exampleLegalSymbols = ["@", "%", "£", "€", "¥", "_"]
    legalString = "The_quick_brown_fox_jumps_over_the_lazy_dog"

    for s in illegalSymbols:
      testString = legalString[:5] + s + legalString[5:]
      escapedString = escapeIllegalSymbols(testString)
      self.assertEqual("'{}'".format(testString), escapedString)

    for s in exampleLegalSymbols:
      testString = legalString[:5] + s + legalString[5:]
      escapedString = escapeIllegalSymbols(testString)
      self.assertEqual(testString, escapedString)

  """
  Albeit short, this test covers the entire expected functionality of this function.
  It's merely supposed to print a slightly different error based on whether an option is prepended
  with a double hyphen '--' or a single one '-'
  """
  def test_printBadArgsError(self):
    from .wc import printBadArgsError
    with self.captured_output() as (stdout, stderr):
      printBadArgsError(["-z"])

    self.assertEqual("", stdout.getvalue())
    self.assertEqual("wc: invalid option -- 'z'\nTry 'wc --help' for more information.\n", stderr.getvalue())

    with self.captured_output() as (stdout, stderr):
      printBadArgsError(["--z"])

    self.assertEqual("", stdout.getvalue())
    self.assertEqual("wc: unrecognised option '--z'\nTry 'wc --help' for more information.\n", stderr.getvalue())

  """
  Tests that printOutput always prints the correct output based on what flags are given to it
  """
  def test_printOutput(self):
    lc, wc, bc, file = 1, 2, 3, "filename"
    doubleOutput = "\t{}\t{}\n"
    tripleOutput = "\t{}\t{}\t{}\n"
    quadOutput = "\t{}\t{}\t{}\t{}\n"

    # Test -c option
    options = ["c"]
    self.assertOutput(lc, wc, bc, file, options, doubleOutput.format(bc, file))

    # Test -l option
    options = ["l"]
    self.assertOutput(lc, wc, bc, file, options, doubleOutput.format(lc, file))

    # Test -w option
    options = ["w"]
    self.assertOutput(lc, wc, bc, file, options, doubleOutput.format(wc, file))

    # Test 2 options (-c -l)
    options = ["c", "l"]
    self.assertOutput(lc, wc, bc, file, options, tripleOutput.format(lc, bc, file))

    # Test 2 options (-w -c)
    options = ["w", "c"]
    self.assertOutput(lc, wc, bc, file, options, tripleOutput.format(wc, bc, file))

    # Test 3 options
    options = ["c", "l", "w"]
    self.assertOutput(lc, wc, bc, file, options, quadOutput.format(lc, wc, bc, file))

    # Test 0 options
    options = []
    self.assertOutput(lc, wc, bc, file, options, quadOutput.format(lc, wc, bc, file))

    # Test bad options
    options = ["z", "q"]
    self.assertOutput(lc, wc, bc, file, options, quadOutput.format(lc, wc, bc, file))

    # Test mix of good and bad options
    options = ["z", "q", "w"]
    self.assertOutput(lc, wc, bc, file, options, doubleOutput.format(wc, file))

  """
  Tests that errors end up in stderr, not stdout
  """
  def test_eprint(self):
    from .wc import eprint

    error = "this error should end up in stderr, not in stdout"
    with self.captured_output() as (stdout, stderr):
      eprint(error)

    self.assertEqual("", stdout.getvalue())
    self.assertEqual("{}\n".format(error), stderr.getvalue())

  def test_preProcessArgs(self):
    from .wc import preprocessArgs
    args = "txt1 -l txt2 --flag2 txt3 -- -w txt4 -- --w txt5 -- txt6 - txt7 -- - txt8 -c".split()
    expectedArgs = "-l --flag2 txt1 txt2 txt3 -- -w txt4 -- --w txt5 -- txt6 - txt7 -- - txt8 -c".split()
    newArgs = preprocessArgs(args)

    self.maxDiff=None

    self.assertEqual(newArgs, expectedArgs)

  """
  Helper for printOutput test. Does the actual assertions.
  """
  def assertOutput(self, lc, wrc, bc, file, options, expectedStdout):
    from .wc import printOutput

    with self.captured_output() as (stdout, stderr):
      printOutput(lc, wrc, bc, file, options)

    self.assertEqual(stdout.getvalue(), expectedStdout)
    self.assertEqual(stderr.getvalue(), "")

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