#!/usr/bin/python3

import sys
import fileinput
import os
import math
class Classifier:
	def __init__(self, name, tw, cp, dc):
		self.name = name
		self.tot_words = tw
		self.class_prob = cp
		self.doc_count = dc
		self.wordcount_dict = {}
	
def create_model_file():
	training_file = open(sys.argv[1], 'r')
	model_file = open(sys.argv[2], 'w+')
	cnames = [] #ordered list of non unique class names
	classnames = set() #set of unique class names
	objects = [] #list of classes
	docs = [] #list of all docs (spam&ham or pos&neg)
	unique_vocab = set() #vocab list
	vocab_size = 0;

	for line in training_file: #for every doc
		words = [word for word in line.split( )] #list of word ID:count in every doc
		#classnames.add(words[0])
		cnames.append(words[0])		
		docs.append(words)
	
	classnames = set(cnames)
	training_file.close()
	for name in classnames:
		objects.append(Classifier(name, 0, 0, 0))
	for doc in docs: #for every doc
		words = [word for word in doc] #get list of words
		for word in words[1:]:
			x = (word.find(':'))
			key = int(word[:x]) #word ID
			value = int(word[x+1:]) #word count
			unique_vocab.add(key)
			for obj in objects:
				if words[0] == obj.name:
					obj.doc_count += 1
					obj.tot_words += 1 #add to total num of words in class
					if key not in obj.wordcount_dict: #insert word:count into dict
						obj.wordcount_dict[key] = value #value or 1??
					else:
						obj.wordcount_dict[key] += value
			'''for word in words[1:]:
				x = (word.find(':'))
				key = int(word[:x]) #word ID
				value = int(word[x+1:]) #word count
				unique_vocab.add(key)
				if words[0] == obj.name: #if label matches class name
					obj.tot_words += 1 #add to total num of words in class
					if key not in obj.wordcount_dict: #insert word:count into dict
						obj.wordcount_dict[key] = value #value or 1??
					else:
						obj.wordcount_dict[key] += value'''

	'''for obj in objects:
		print(len(obj.wordcount_dict)) #REPRESENTS ALL UNIQUE WORDS IN CLASS WITH COUNT'''	
	total_dc = 0
	for obj in objects:
		total_dc += obj.doc_count
		#model_file.write(str(obj.wordcount_dict))
		#model_file.write('\n')
	
	vocab_size = len(unique_vocab)
	s = str(vocab_size) 
	for obj in objects:
		obj.class_prob = obj.doc_count/total_dc
		s+= "\n" + obj.name + " " + str(obj.tot_words) + " " + str(obj.class_prob)
	#print(s)
	for key in unique_vocab:
		s += "\n" + str(key)
		for obj in objects:
			if key in obj.wordcount_dict:
				value = math.log(obj.wordcount_dict[key]+1) - math.log(obj.tot_words+vocab_size)
				s += " " + str(value)
			else:
				value = math.log(1) - math.log(obj.tot_words+vocab_size)
				s += " " + str(value)
	model_file.write(s)

def main():
	if(len(sys.argv) != 3):
		print ("\nInvalid number of cmd arguments. Exiting.")
		sys.exit(0)
	if(not os.path.isfile(sys.argv[1])):
		print('Invaild Feat File Path. Exiting.')
		sys.exit(0)
	create_model_file()
	print("Created model file")
main()
