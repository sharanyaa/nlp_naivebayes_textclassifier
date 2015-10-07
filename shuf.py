#!/usr/bin/python3
import sys
import fileinput
import os
import random

feat_file = open(sys.argv[1], 'r')
lines = feat_file.readlines()
feat_file.close()
#print(lines)
feat_file = open(sys.argv[1], 'w+')
random.shuffle(lines)

feat_file.writelines(lines)
