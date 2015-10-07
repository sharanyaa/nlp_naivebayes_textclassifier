import sys
import fileinput
import os
import random
import collections

'''def insertsvm(): #add one to feature, sort by feat and insert random label into test data
	sort()
	ipfile = open("svm.test", "r")
	lines = ipfile.readlines()
	ipfile.close()
	opfile = open("svm.test", "w+")
	newlines = []
	for i, line in enumerate(lines):
		words = [word for word in line.split( )]
		if random.random() >0.5:
			words.insert(0, "+1")
		else:
			words.insert(0, "-1")
		l = ""
		for word in words:
			l += word + " "
		newlines.append(l)
	for doc in newlines:
		words = [word for word in doc.split( )]
		#print(words)
		for word in words:
			#print (word)
			opfile.write(word)
			opfile.write(" ")
		opfile.write("\n")'''	
	
def insertsvm():
#def sort(): #sort by feature
	ipfile = open(sys.argv[1], 'r')
	lines = ipfile.readlines()
	ipfile.close()
	opfile = open("svm.test", 'w+')
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
		if random.random() >0.5:
			ewords.insert(0, "+1")
		else:
			ewords.insert(0, "-1")
		editlines.append(ewords)
	#print(editlines)
	for doc in editlines:
		words = [word for word in doc]
		for word in words:
			opfile.write(word)
			opfile.write(" ")
		opfile.write("\n")
	opfile.close()
		
	
def insertmegam():
	ipfile = open(sys.argv[1], "r")
	opfile = open("megam.test", "w+")
	for line in ipfile:
		words = [word for word in line.split()]
		'''for i, word in enumerate(words):
			if ":" in word:
				words[i].replace(':',' ')'''
		if random.random() >0.5:
			words.insert(0, "1 ")
		else:
			words.insert(0, "0 ")
		for w in words:
			if ":" in w:
				x = (w.find(':'))
				key = w[:x]
				value = w[x+1:]
				w = key + " " + value
				#print(w)
			opfile.write(w)
			opfile.write(" ")
		opfile.write("\n")
	opfile.close()
def main():
	if(len(sys.argv) != 3):
		print ("\nInvalid number of cmd arguments. Exiting.")
		sys.exit(0)
	if(not os.path.isfile(sys.argv[1])):
		print('Invaild Feat File Path. Exiting.')
		sys.exit(0)
	if(sys.argv[2] == 'svm'):
		insertsvm()
	else:
		insertmegam()
main()
