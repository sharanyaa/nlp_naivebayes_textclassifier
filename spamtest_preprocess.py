#!/usr/bin/python3

import sys
import fileinput
import os
vocab_dict = {}

def megamcreatepdf():
	path = "spam_or_ham_test/"
	output_file = open("spamtest.feat", 'w+')
	email_files = [path+f for f in os.listdir(path) if f.endswith(".txt")]
	email_files.sort()
	vocab_dict = {}
	i = 0
	for file in email_files:
		wordcount = {} #dict for storing words with count
		emailfile = open(file, encoding='latin1')
		for word in emailfile.read().split():
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
			vocab_dict[word] = i
			i += 1
		for key, value in wordcount.items():
			output_file.write(str(vocab_dict[key]))
			output_file.write(' ')
			output_file.write(str(value))
			output_file.write(' ')
		output_file.write('\n')
		emailfile.close()
		#print(len(wordcount))
	#print(len(p))
	output_file.close()
def createpdf():
	path = "spam_or_ham_test/"
	output_file = open("spamtest.feat", 'w+')
	email_files = [path+f for f in os.listdir(path) if f.endswith(".txt")]
	email_files.sort()
	vocab_dict = {}
	i = 0
	for file in email_files:
		wordcount = {} #dict for storing words with count
		emailfile = open(file, encoding='latin1')
		for word in emailfile.read().split():
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
			vocab_dict[word] = i
			i += 1
		for key, value in wordcount.items():
			output_file.write(str(vocab_dict[key]))
			output_file.write(':')
			output_file.write(str(value))
			output_file.write(' ')
		output_file.write('\n')
		emailfile.close()
		#print(len(wordcount))
	#print(len(p))
	output_file.close()

if sys.argv[1] == "megam":
	megamcreatepdf()
else:
	createpdf()
