import os
import sys
import argparse
import glob
import subprocess

def processFile(program, fpath):
  # TODO Quote path manually if taken from args, otherwise it tries to pass it unquoted and breaks
  out = subprocess.check_output("(bash -c 'time {} {}') 2>&1".format(program, fpath), shell=True).decode().split("\n")[2:5]
  real = getSeconds(out[0].split("\t")[1])
  cpu = getSeconds(out[1].split("\t")[1]) + getSeconds(out[2].split("\t")[1])
  return os.path.basename(fpath), real, cpu

def processFiles(program, dir):
  fpaths = glob.glob(os.path.join(dir, "*"))
  results = []
  for fpath in fpaths:
    results.append(processFile(program, fpath))

  return results

def getSeconds(timeString):
  minutes, seconds = str(timeString[:-1]).split("m")
  return int(minutes) * 60 + float(seconds)

def outputResults(results):
  print("Testcase\tReal\tCPU")
  for file, real, cpu in results:
    print("{}\t{}\t{}".format(file, real, cpu))

# TODO create calculateStats(results)

def createArgParser():
  parser = argparse.ArgumentParser(add_help=True)
  parser.add_argument("directory", nargs="?", default="testinputs", help="a directory of test files (default: testinputs)")
  return parser

if __name__ == "__main__":
  parser = createArgParser()
  args = parser.parse_args(sys.argv[1:])
  wcOut = processFiles("wc", args.directory)
  wcPyOut = processFiles("python3 wc.py", args.directory)

  outputResults(wcOut)