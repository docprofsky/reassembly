from __future__ import print_function
from subprocess import call
from sys import version_info, stderr
import argparse
import difflib


parser = argparse.ArgumentParser()
parser.add_argument("c", help="path to c source to match")
parser.add_argument("asm", help="path to your assembly")
args = parser.parse_args()

cpath = args.c
asmpath = args.asm

print("Compiling to Assembly...\n", file=stderr)
call(["gcc", "-S", "-O0", cpath])

compiledfile = open(cpath.split('.')[0] + ".s", 'r')
userfile = open(asmpath, 'r')

diff = difflib.ndiff(compiledfile.readlines(), userfile.readlines())
delta = ''.join(x[2:] for x in diff if x.startswith('- '))
print(delta)
