#!/usr/bin/python3

import sys
import fileinput
import os

enron_dict = {}
def create_pdf():
	paths = ['enron1/ham/','enron2/ham/','enron4/ham/','enron5/ham/','enron1/spam/','enron2/spam/','enron4/spam/','enron5/spam/']
	outputfilename = "email.feat"
	output_file = open(outputfilename, 'w+')
	email_files = []
	for p in paths:
		filenames = [p+f for f in os.listdir(p) if f.endswith(".txt")]
		#print (len(filenames))
		email_files.extend(filenames)
		#print (filenames)
	#print (len(email_files))
	p = set() #
	for file in email_files:
		wordcount = {} #dict for storing words with count
		emailfile = open(file, encoding='latin1')
		for word in emailfile.read().split():
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
		if "ham" in file:
			if len(sys.argv)==2 and sys.argv[1]=="megam":
				output_file.write('0 ')
			else:
				output_file.write('HAM ')
		elif "spam" in file:
			if len(sys.argv)==2 and sys.argv[1]=="megam":
				output_file.write('1 ')
			else:
				output_file.write('SPAM ')
		for key, value in wordcount.items():
			#output_file.write(' ')
			output_file.write(str(enron_dict[key]))
			if len(sys.argv)==2 and sys.argv[1]=="megam":
				output_file.write(' ')
			else:
				output_file.write(':')
			output_file.write(str(value))
			output_file.write(' ')
			p.add(key)
		output_file.write('\n')
		emailfile.close()
		#print(len(wordcount))
	#print(len(p))
	output_file.close()

def enron_vocab():
	vocabfile = "enron.vocab"
	if(os.path.isfile(vocabfile)):
		vocab_file = open(vocabfile, encoding='latin1')
		i = 0
		for line in vocab_file:
			enron_dict[line.rstrip('\n')] = i
			i += 1
		#print(enron_dict['christmas'])
		#print(len(enron_dict))	
	#print(i)

enron_vocab()
create_pdf()
	
print("Created email.feat")
			

