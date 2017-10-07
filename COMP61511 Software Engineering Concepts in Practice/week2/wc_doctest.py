# Everything is in a docstring!
"""
>>> import subprocess
>>> subprocess.check_output('wc wc.py', shell=True)
b' 120  364 3183 wc.py\\n'
"""

 # We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()