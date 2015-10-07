#!/usr/bin/python3
import sys
import fileinput
import os
import random
import collections

def process1():
	file = open(sys.argv[1], 'r') 
	lines = file.read().splitlines()
	file.close()
	for i, line in enumerate(lines):
		#print("\n",line)
		words = [word for word in line.split( )]
		val = int(words[0])
		#print(val)
		if val == 1:
			lines[i] = "SPAM"
		else:
			lines[i] = "HAM"
	file = open(sys.argv[1], 'w+') #output	
	file.write('\n'.join(lines))
	file.close()

def process2():
	file = open(sys.argv[1], 'r') 
	lines = file.read().splitlines()
	file.close()
	for i, line in enumerate(lines):
		words = [word for word in line.split( )]
		val = int(words[0])
		if val == 1:
			lines[i] = "POSITIVE"
		else:
			lines[i] = "NEGATIVE"
	file = open(sys.argv[1], 'w+') #output	
	file.write('\n'.join(lines))
	file.close()

def main():
	if "spam" in sys.argv[1]:	
		process1()
	else:
		process2()

main()
