# Uses http://www.brokenlinkcheck.com/

import os.path, mmap
nameInput = raw_input("Name of input file: ");

if not os.path.isfile(nameInput):
	print """
File does not exist. Please enter a valid input file name with extension.
If the file is in a different directory, be sure to reference properly.
	""";
	nameInput = raw_input("Name of input file: ");

nameOutput = raw_input("Desired name of output file, without extension: ");
outputFile = nameOutput + ".txt";

root = 'http://www.happyvalley.com/';
rootLen = len(root) - 1;

f = open(nameInput);
g = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
h = open(outputFile, 'w');

a = g.find(root); # find url start
b = '"'; # find url end
counter = 0;

while a != -1:
	relStart = a+rootLen;
	relEnd = g.find(b, a);
	relPath = g[relStart:relEnd];
	if len(relPath) > 1: # hide base url errors from brokenlinkcheck
		oneLine = "Redirect 301 " + relPath + "\n" ;
		line = str(oneLine);
		h.write(oneLine);
	counter += 1;
	a = g.find(root, relEnd); # move cursor forward

f.close();
h.close();

print counter, "redirect bases generated for", root, "to", outputFile;
