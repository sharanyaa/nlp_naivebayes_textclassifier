#!/usr/bin/python3

import sys
import fileinput
import os
import math


def createtestfile():
	feat_file = open(sys.argv[1], 'r')
	test_file = open(sys.argv[2], 'w+')

	for line in feat_file:
		words = [word for word in line.split( )]
		for word in words[1:]:
			test_file.write(word)
			test_file.write(" ")
		test_file.write("\n")

def main():
	if(len(sys.argv) != 3):
		print ("\nInvalid number of cmd arguments. Exiting.")
		sys.exit(0)
	if(not os.path.isfile(sys.argv[1])):
		print('Invaild Feat File Path. Exiting.')
		sys.exit(0)
	
	createtestfile()
	print("Created test file")

main()
