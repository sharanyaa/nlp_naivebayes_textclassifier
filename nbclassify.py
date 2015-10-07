#!/usr/bin/python3

import sys
import fileinput
import os
import math

class Classifier:
	def __init__(self, name, tw, cp):
		self.name = name
		self.tot_words = tw
		self.class_prob = cp
		#self.final_prob = 0
'''class Word:
	def __init__(self, id, cp1, cp2):
		self.id = id
		self.cp1 = cp1
		self.cp2 = cp2'''
class TestWord:
	def __init__(self, id, cnt):
		self.id = id
		self.cnt = cnt

def nbclassify():
	model_file = open(sys.argv[1], 'r')
	test_file = open(sys.argv[2], 'r')
	objects = [] #list of classes with class name, total words and class probs
	words = [] #list of words with id and class probablities
	vocabsize = 0
	cp1_dict = {} #word_id : class 1 prob
	cp2_dict = {} #word_id : class 2 prob
	for i, line in enumerate(model_file):
		if i == 0: #vocabsize
			vocabsize = int(line)
		if i == 1 or i == 2:
			words1 = [word for word in line.split( )]
			#print (words)
			objects.append(Classifier(words1[0], int(words1[1]), float(words1[2])))
		if i>2:
			words1 = [word for word in line.split( )]
			#print (words)
			#words.append(Word(int(words1[0]), float(words1[1]), float(words1[2])))
			cp1_dict[int(words1[0])] = float(words1[1])
			cp2_dict[int(words1[0])] = float(words1[2])
	model_file.close()
	if "spam" in sys.argv[1]:
		op = open("spam.nb.out", 'w+')
	else:
		op = open("sentiment.nb.out", 'w+')
	for line in test_file: #for every doc
		testwords = [] #list of words in test doc
		words1 = [word for word in line.split( )]
		for word in words1:
			x = (word.find(':'))
			wid = int(word[:x]) #word ID
			wcnt = int(word[x+1:]) #word count
			testwords.append(TestWord(wid,wcnt))

		fprob1 = objects[0].class_prob
		fprob2 = objects[1].class_prob
		for tword in testwords:
			'''for w in words:
				if tword.id == w.id:
					pwgc = w.cp1'''
			if tword.id in cp1_dict:
				pwgc1 = cp1_dict[tword.id]
			else:
				pwgc1 = 0
			fprob1 += (pwgc1*tword.cnt)
			
			if tword.id in cp2_dict:
				pwgc2 = cp2_dict[tword.id]
			else:
				pwgc2 = 0
			fprob2 += (pwgc2*tword.cnt)
	
		'''
		#first class prob
		#second class prob		
		for tword in testwords:
			for w in words:
				if tword.id == w.id:
					pwgc = w.cp2
			pwgc2 = cp2_dict[tword.id]
			fprob2 += (pwgc2*tword.cnt) '''

		#print(fprob1)
		#print(fprob2)
		#op.write(str(fprob1))
		#op.write("\n")
		#op.write(str(fprob2))
		#op.write("\n")

		if fprob1>fprob2:
			print(objects[0].name)
			op.write(objects[0].name)
			op.write("\n")
			
		else:
			print(objects[1].name)
			op.write(objects[1].name)
			op.write("\n")

def main():
	if(len(sys.argv) != 3):
		print ("\nInvalid number of cmd arguments. Exiting.")
		sys.exit(0)
	if(not os.path.isfile(sys.argv[1])):
		print('Invaild Model File Path. Exiting.')
		sys.exit(0)
	if(not os.path.isfile(sys.argv[2])):
		print('Invaild Test File Path. Exiting.')
		sys.exit(0)
	nbclassify()

main()
