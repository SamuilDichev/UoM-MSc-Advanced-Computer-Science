"""
>>> preprocessArgs("txt1 -l txt2 --flag2 txt3 -- -w txt4 -- --w txt5 -- txt6 - txt7 -- - txt8 -c".split())
['-l', '--flag2', 'txt1', 'txt2', 'txt3', '--', '-w', 'txt4', '--', '--w', 'txt5', '--', 'txt6', '-', 'txt7', '--', '-', 'txt8', '-c']
"""
if __name__ == "__main__":
  import doctest
  from wc import preprocessArgs
  doctest.testmod()