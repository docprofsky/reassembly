from __future__ import print_function
from subprocess import call
from sys import version_info

def get_input(prompt):
    if version_info < (3, 0):
        return raw_input(prompt)
    else:
        return input(prompt)

cfile = get_input("Enter C file name: ")
afile = get_input("Enter Assembly output file name: ")

print("Compiling to Assembly...")

call(["gcc", "-S", "-O0", cfile, "-o", afile])
