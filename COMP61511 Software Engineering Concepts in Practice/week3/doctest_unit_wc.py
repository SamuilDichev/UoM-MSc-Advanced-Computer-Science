"""
>>> preprocessArgs("txt1 -l txt2 --flag2 txt3 -- -w txt4 -- --w txt5 -- txt6 - txt7 -- - txt8 -c".split())
['-l', '--flag2', 'txt1', 'txt2', 'txt3', '--', '-w', 'txt4', '--', '--w', 'txt5', '--', 'txt6', '-', 'txt7', '--', '-', 'txt8', '-c']
>>> createArgParser().parse_known_args('-l --flag2 txt1 txt2 txt3 -- -w txt4 -- --w txt5 -- txt6 - txt7 -- - txt8 -c'.split())
(Namespace(FILE=['txt1', 'txt2', 'txt3', '-w', 'txt4', '--', '--w', 'txt5', '--', 'txt6', '-', 'txt7', '--', '-', 'txt8', '-c'], c=False, l=True, w=False), ['--flag2'])
>>> isFileArg("-asasda") or isFileArg("-c")
False
>>> isFileArg("--") and isFileArg("asdas")
True
>>> getOptions(Namespace(z=True, b=False, d=False, o=2, l="s", f=-1, q=99999999))
['z']
>>> escapeIllegalSymbols('The_q uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q!uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q!uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q~uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q~uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q#uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q#uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q$uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q$uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q^uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q^uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q&uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q&uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q*uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q*uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q(uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q(uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q)uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q)uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q=uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q=uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q<uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q<uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q>uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q>uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q?uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q?uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q;uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q;uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q:uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q:uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q[uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q[uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q{uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q{uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q]uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q]uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q}uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q}uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q|uick_brown_fox_jumps_over_the_lazy_dog')
"'The_q|uick_brown_fox_jumps_over_the_lazy_dog'"
>>> escapeIllegalSymbols('The_q@uick_brown_fox_jumps_over_the_lazy_dog')
'The_q@uick_brown_fox_jumps_over_the_lazy_dog'
>>> escapeIllegalSymbols('The_q%uick_brown_fox_jumps_over_the_lazy_dog')
'The_q%uick_brown_fox_jumps_over_the_lazy_dog'
>>> escapeIllegalSymbols('The_q£uick_brown_fox_jumps_over_the_lazy_dog')
'The_q£uick_brown_fox_jumps_over_the_lazy_dog'
>>> escapeIllegalSymbols('The_q€uick_brown_fox_jumps_over_the_lazy_dog')
'The_q€uick_brown_fox_jumps_over_the_lazy_dog'
>>> escapeIllegalSymbols('The_q¥uick_brown_fox_jumps_over_the_lazy_dog')
'The_q¥uick_brown_fox_jumps_over_the_lazy_dog'
>>> escapeIllegalSymbols('The_q_uick_brown_fox_jumps_over_the_lazy_dog')
'The_q_uick_brown_fox_jumps_over_the_lazy_dog'
>>> with capturedOutput(None, False, True): printBadArgsError(["-z"])
wc: invalid option -- 'z'\nTry 'wc --help' for more information.
>>> with capturedOutput(None, False, True): printBadArgsError(["--z"])
wc: unrecognised option '--z'\nTry 'wc --help' for more information.
>>> with capturedOutput(" ", True, False): printOutput(1, 2, 3, "qwerty", ["c"])
3 qwerty
>>> with capturedOutput(" ", True, False): printOutput(1, 2, 3, "qwerty", ["l"])
1 qwerty
>>> with capturedOutput(" ", True, False): printOutput(1, 2, 3, "qwerty", ["w"])
2 qwerty
>>> with capturedOutput(" ", True, False): printOutput(1, 2, 3, "qwerty", ["c", "l"])
1 3 qwerty
>>> with capturedOutput(" ", True, False): printOutput(1, 2, 3, "qwerty", ["w", "c"])
2 3 qwerty
>>> with capturedOutput(" ", True, False): printOutput(1, 2, 3, "qwerty", ["c", "l", "w"])
1 2 3 qwerty
>>> with capturedOutput(" ", True, False): printOutput(1, 2, 3, "qwerty", [])
1 2 3 qwerty
>>> with capturedOutput(" ", True, False): printOutput(1, 2, 3, "qwerty", ["z", "q"])
1 2 3 qwerty
>>> with capturedOutput(" ", True, False): printOutput(1, 2, 3, "qwerty", ["z", "q", "w"])
2 qwerty
>>> with capturedOutput(None, True, False): eprint("this error should end up in stderr, not in stdout")
<BLANKLINE>
>>> with capturedOutput(None, False, True): eprint("this error should end up in stderr, not in stdout")
this error should end up in stderr, not in stdout
>>> processFile("testinputs/services")
(11176, 61033, 670293, 'testinputs/services')
>>> processFile("testinputs/os-release")
(15, 22, 484, 'testinputs/os-release')
>>> processFile("testinputs/empty.txt")
(0, 0, 0, 'testinputs/empty.txt')
>>> processFile("testinputs/small.txt")
(1, 1, 2, 'testinputs/small.txt')
>>> processFile("testinputs/small2.txt")
(2, 1, 3, 'testinputs/small2.txt')
>>> with capturedOutput(" ", True, True): processFiles(["testinputs/services", "testinputs/os-release", "testinputs/empty.txt", "testinputs/qwerty-non-existent-file-hopefully", "testinputs"], [])
11176 61033 670293 testinputs/services 15 22 484 testinputs/os-release 0 0 0 testinputs/empty.txt 0 0 0 testinputs 11191 61055 670777 total
wc: testinputs/qwerty-non-existent-file-hopefully: No such file or directory wc: testinputs: Is a directory
"""

from contextlib import contextmanager

@contextmanager
def capturedOutput(delimiter, out, err):
  my_stdout, my_stderr = StringIO(), StringIO()
  default_stdout, default_stderr = sys.stdout, sys.stderr

  try:
    sys.stdout, sys.stderr = my_stdout, my_stderr
    yield sys.stdout, sys.stderr
  finally:
    sys.stdout, sys.stderr = default_stdout, default_stderr
    outString = my_stdout.getvalue().strip()
    errString = my_stderr.getvalue().strip()

    if delimiter:
      if out:
        print(delimiter.join(outString.split()))
      if err:
        print(delimiter.join(errString.split()))
    else:
      if out:
        print(outString)
      if err:
        print(errString)

if __name__ == "__main__":
  import doctest
  import sys
  from argparse import Namespace
  from io import StringIO

  from wc import preprocessArgs
  from wc import createArgParser
  from wc import isFileArg
  from wc import getOptions
  from wc import escapeIllegalSymbols
  from wc import printBadArgsError
  from wc import printOutput
  from wc import eprint
  from wc import processFile
  from wc import processFiles

  doctest.testmod()