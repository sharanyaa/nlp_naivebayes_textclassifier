#!/usr/bin/python3

import sys
import fileinput
import os
import random
import collections

def badshufsplit():
	feat_file = open(sys.argv[1], 'r')
	train_file = open(sys.argv[2], 'w+')
	test_file = open(sys.argv[3], 'w+')
	chk_file = open("test/check.txt", "w+")
	lines = feat_file.readlines()
	random.shuffle(lines)
	test = lines[len(lines)//4:] #75%
	train = lines[:len(lines)//4] #25%
	for doc in train:
		words = [word for word in doc.split( )]
		for word in words:
			train_file.write(word)
			train_file.write(" ")
		train_file.write("\n")
	print(len(train))
	print(len(test))
	for doc in test:
		words = [word for word in doc.split( )]
		chk_file.write(words[0])
		chk_file.write("\n")
		words.remove(words[0])
		#print(words)
		for word in words:
			test_file.write(word)
			test_file.write(" ")
		test_file.write("\n")

def goodshufsplit():
	feat_file = open(sys.argv[1], 'r')
	train_file = open(sys.argv[2], 'w+')
	test_file = open(sys.argv[3], 'w+')
	chk_file = open("test/check.txt", "w+")
	lines = feat_file.readlines()
	random.shuffle(lines)
	train = lines[len(lines)//4:] #75%
	test = lines[:len(lines)//4] #25%
	for doc in train:
		words = [word for word in doc.split( )]
		for word in words:
			train_file.write(word)
			train_file.write(" ")
		train_file.write("\n")
	#print(len(train))
	#print(len(test))
	for doc in test:
		words = [word for word in doc.split( )]
		chk_file.write(words[0])
		chk_file.write("\n")
		words.remove(words[0])
		#print(words)
		for word in words:
			test_file.write(word)
			test_file.write(" ")
		test_file.write("\n")	
	feat_file.close()
	test_file.close()
	train_file.close()

def main():
	if(len(sys.argv) != 5):
		print ("\nInvalid number of cmd arguments. Exiting.")
		sys.exit(0)
	if(not os.path.isfile(sys.argv[1])):
		print('Invaild Feat File Path. Exiting.')
		sys.exit(0)
	if(sys.argv[4] == 'bad'):
		badshufsplit()
		print("Created 25% training and 75% test files for testing")
	elif(sys.argv[4] == 'good'):
		goodshufsplit()
		print("Created 75% training and 25% test files for testing")

main()
