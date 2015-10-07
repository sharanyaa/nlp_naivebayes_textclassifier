#!/usr/bin/python3

import sys
import fileinput
import os
import random
import collections


def createchksvm():

	feat_file = open(sys.argv[1], 'r')
	chk_file = open("test/check.txt", "w+")
	lines = feat_file.readlines()
	#random.shuffle(lines)
	#print(sys.argv[1])
	for doc in lines:
		words = [word for word in doc.split( )]
		#print(doc)
		if words[0] == "+1":
			#print("hi")
			if data == "spam":
				words[0] = "SPAM"
			else:
				words[0] = "POSITIVE"
		elif words[0] == "-1":
			if data == "spam":
				words[0] = "HAM"
			else:
				words[0] = "NEGATIVE"
			
		chk_file.write(words[0])
		chk_file.write("\n")
		words.remove(words[0])
		#print(words[0])
def createchkmegam():
	feat_file = open(sys.argv[1], 'r')
	chk_file = open("test/check.txt", "w+")
	lines = feat_file.readlines()
	#random.shuffle(lines)
	#print(sys.argv[1])
	for doc in lines:
		words = [word for word in doc.split( )]
		#print(doc)
		if words[0] == "1":
			#print("hi")
			if data == "spam":
				words[0] = "SPAM"
			else:
				words[0] = "POSITIVE"
		elif words[0] == "0":
			if data == "spam":
				words[0] = "HAM"
			else:
				words[0] = "NEGATIVE"
			
		chk_file.write(words[0])
		chk_file.write("\n")
		words.remove(words[0])

tool = sys.argv[2]
data = sys.argv[3]
if tool == "svm":
	createchksvm()
else:
	createchkmegam()
	
