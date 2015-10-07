#!/usr/bin/python3

import sys
import fileinput
import os
import random
import collections

def addonesort(): #add one and sort by feature
	ipfile = open(sys.argv[1], 'r')
	lines = ipfile.readlines()
	ipfile.close()
	opfile = open(sys.argv[1], 'w+')
	editlines = []
	for line in lines:
		d = {}
		ewords = []
		words = [word for word in line.split( )]
		for i, word in enumerate(words): 
			if ":" in word:
				x = (word.find(':'))
				key = int(word[:x]) 
				key += 1
				value = int(word[x+1:])
				d[key] = value
		od = collections.OrderedDict(sorted(d.items()))
		for k, v in od.items():
			ewords.append(str(k)+ ':' +str(v))
		if(words[0] == "POSITIVE" or words[0] == "SPAM"):
			words[0] = "+1"
		else:
			words[0] = "-1"
		ewords.insert(0, words[0])
		#print(ewords)
		editlines.append(ewords)
	for doc in editlines:
		#print(doc)
		words = [word for word in doc]
		for word in words:
			opfile.write(word)
			opfile.write(" ")
		opfile.write("\n")
	opfile.close()


addonesort()
