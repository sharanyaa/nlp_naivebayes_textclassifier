#!/usr/bin/python3
import sys
import fileinput
import os
import random
import collections

def count1():
	op_file = open(sys.argv[1], 'r') #output 
	chk_file = open("test/check.txt", 'r')
	chk = chk_file.read().splitlines()
	op = op_file.read().splitlines()
	spam = 'SPAM'
	ham = 'HAM'
	#print(op[0])
	b = len(chk) #total num of docs
	a = 0 #total num of correcty classified docs
	c1 = 0 #correctly classified as spam
	c2 = 0 #correctly classfied as ham
	d1 = op.count("SPAM") #total num of docs classified as spam
	d2 = op.count("HAM") #total num of docs classified as ham
	e1 = chk.count("SPAM") #total num actally belongs to spam
	e2 = chk.count("HAM") #total num actally belongs to ham
	#print (chk)
	#print("hi")
	#print (sys.argv[1])
	for i, line in enumerate(op):
		if(op[i] == chk[i]):
			#print("hi")
			a += 1
			if(op[i] == spam):
				c1+=1
			elif op[i] == ham:
				c2+=1
	print(a, b, c1, c2, d1, d2, e1, e2)
	acc = a/b
	p1 = c1/d1
	p2 = c2/d2
	r1 = c1/e1
	r2 = c2/e2
	f1 = (2*p1*r1)/(p1+r1)
	f2 = (2*p2*r2)/(p2+r2)
	print("acc: ", acc)
	print("SPAM - p1: ", p1, "r1: ", r1, "f1: ", f1)
	print("HAM - p2: ", p2, "r2: ", r2, "f2: ", f2)
	op_file.close()
	chk_file.close()

def count2():
	op_file = open(sys.argv[1], 'r') #output 
	chk_file = open("test/check.txt", 'r')
	chk = chk_file.read().splitlines()
	op = op_file.read().splitlines()
	
	pos = 'POSITIVE'
	neg = 'NEGATIVE'
	b = len(chk) #total num of docs
	a = 0 #total num of correcty classified docs
	c1 = 0 #correctly classified as spam
	c2 = 0 #correctly classfied as ham
	d1 = op.count("POSITIVE") #total num of docs classified as spam
	d2 = op.count("NEGATIVE") #total num of docs classified as ham
	e1 = chk.count("POSITIVE") #total num actally belongs to spam
	e2 = chk.count("NEGATIVE") #total num actally belongs to ham
	#print (chk)
	for i, line in enumerate(op):
		if(op[i] == chk[i]):
			a += 1
			if(op[i] == pos):
				c1+=1
			elif op[i] == neg:
				c2+=1
	print(a, b, c1, c2, d1, d2, e1, e2)
	acc = a/b
	p1 = c1/d1
	p2 = c2/d2
	r1 = c1/e1
	r2 = c2/e2
	f1 = (2*p1*r1)/(p1+r1)
	f2 = (2*p2*r2)/(p2+r2)
	print("acc: ", acc)
	print("POS - p1: ", p1, "r1: ", r1, "f1: ", f1)
	print("NEG - p2: ", p2, "r2: ", r2, "f2: ", f2)
	op_file.close()
	chk_file.close()
def main():
	if "spam" in sys.argv[1]:	
		count1()
	#elif "megam" in sys.argv[1]:
		#count3()
	else:
		count2()

main()
