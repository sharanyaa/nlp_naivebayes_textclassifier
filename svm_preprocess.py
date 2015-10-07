#!/usr/bin/python3

import sys
import fileinput
import os
import random
import collections

def svmpreprocess():
	feat_file = open(sys.argv[1], 'r')
	train_file = open(sys.argv[2], 'w+')
	test_file = open(sys.argv[3], 'w+')

	lines = feat_file.readlines()
	editlines = []
	for line in lines:
		d = {}
		ewords = []
		words = [word for word in line.split( )]
		for i, word in enumerate(words): #add one to word id
			if words[i] == 'POSITIVE' or words[i] == 'SPAM':
				#words[i] = '+1'
				ewords.append('+1')
			elif words[i] == 'NEGATIVE' or words[i] == 'HAM':
				#words[i] = '-1'
				ewords.append('-1')
			else:
				x = (word.find(':'))
				key = int(word[:x]) #word ID
				#print (key)
				key += 1
				value = int(word[x+1:])
				d[key] = value
				#words[i] = str(key) + ':' +str(value)
		od = collections.OrderedDict(sorted(d.items()))
		for k, v in od.items():
			ewords.append(str(k)+ ':' +str(v))
		editlines.append(ewords)
		
	random.shuffle(editlines)
	''' train = lines[len(lines)//4:] #75% - GOOD
	test = lines[:len(lines)//4] #25%

	test = lines[len(lines)//4:] #75% - BAD
	train = lines[:len(lines)//4] #25%'''
	if sys.argv[4] == "good":
		train = editlines[len(editlines)//4:]
		test = editlines[:len(editlines)//4]
		#print ("good")
	else:
		train = editlines[:len(editlines)//4]
		test = editlines[len(editlines)//4:]
		#print ("bad")
	for doc in train:
		words = [word for word in doc]
		for word in words:
			train_file.write(word)
			train_file.write(" ")
		train_file.write("\n")
	for doc in test:
		words = [word for word in doc]
		for word in words:
			test_file.write(word)
			test_file.write(" ")
		test_file.write("\n")
	feat_file.close()
	train_file.close()
	test_file.close()

def main():
	if(len(sys.argv) != 5):
		print ("\nInvalid number of cmd arguments. Exiting.")
		sys.exit(0)
	if(not os.path.isfile(sys.argv[1])):
		print('Invaild Feat File Path. Exiting.')
		sys.exit(0)
	svmpreprocess()
	print("Created SVM training and test file")

main()
