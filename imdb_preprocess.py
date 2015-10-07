#!/usr/bin/python3

import sys
import fileinput
import os

enron_dict = {}
def imdbpreprocess():
	input_file = open('labeledBow.feat.fixed', 'r')
	outputfilename = "imdb.feat"
	output_file = open(outputfilename, 'w+')
	lines = input_file.readlines()
	editlines = []
	for line in lines:
		words = [word for word in line.split( )]
		label = int(words[0])
		if(label>=7):
			if len(sys.argv)==2 and sys.argv[1]=="megam":
				words[0] = '1'
			else:
				words[0] = 'POSITIVE'
		elif(label<=4):
			if len(sys.argv)==2 and sys.argv[1]=="megam":
				words[0] = '0'
			else:
				words[0] = 'NEGATIVE'
		if len(sys.argv)==2 and sys.argv[1]=="megam":
			for j, w in enumerate(words):
				if ":" in w:
					x = (w.find(':'))
					key = w[:x]
					value = w[x+1:]
					words[j] = key+" "+value
					
		editlines.append(words)
	for doc in editlines:
		words = [word for word in doc]
		for word in words:
			output_file.write(word)
			output_file.write(" ")
		output_file.write("\n")
	output_file.close()
	input_file.close()

imdbpreprocess()
print("Created imdb.feat")
			

