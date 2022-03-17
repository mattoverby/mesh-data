#!/usr/bin/env python

import sys
import os
from glob import glob

# Creates a txt of full-path file names

# Print usage
if len(sys.argv) < 2:
	print("Generates a text file of absolute paths of directory contents")
	print("Ignores .md files")
	print("Usage: ./gen_file_list.py <directory1> <directory2> ...")
	print("Output file is: files.txt")
	sys.exit()

if len(sys.argv) > 3:
	print("To-do: more than one directory")
	sys.exit()

# build directory
listdir = sys.argv[1]
if listdir[-1] != '/':
	listdir += '/'

files = [y for x in os.walk(listdir) for y in glob(os.path.join(x[0], '*.*'))]
files.sort()

outputname = 'files.txt'
outfile = open(outputname, 'w')
for f in files:
	if not os.path.isfile(f):
		continue
	if os.path.splitext(f)[1] == '.md':
		continue
	fpath = os.path.abspath(f)
	outfile.write("%s\n" % fpath)
