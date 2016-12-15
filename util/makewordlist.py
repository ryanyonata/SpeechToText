import re
import nltk

def remwithre(text, there=re.compile(re.escape('.')+'.*')):
  	return there.sub('', text)

def writewordlist(infile,outfile):
	for line in infile:
		line = line.lower()
		line = re.sub(r"\S+_\S+\t", "", line)
		line = line.replace("\t","")
		line = remwithre(line)
		chars_to_remove = ['!', '?', ',']
		rx = '[' + re.escape(''.join(chars_to_remove)) + ']'
		line = re.sub(rx, '', line)
		lines = line.split()
		for l in lines:
			outfile.write(l)
			outfile.write("\n")

with open('A.txt','w') as outfile:
	with open('../Dataset5/transcript/A-raw.tsv') as infile:
		writewordlist(infile,outfile)
	with open('../Dataset5/transcript/B-raw.tsv') as infile:
		writewordlist(infile,outfile)
	with open('../Dataset5/transcript/C-raw.tsv') as infile:
		writewordlist(infile,outfile)
	with open('../Dataset5/transcript/D-raw.tsv') as infile:
		writewordlist(infile,outfile)
	with open('../Dataset5/transcript/E-raw.tsv') as infile:
		writewordlist(infile,outfile)
	with open('../Dataset5/transcript/F-raw.tsv') as infile:
		writewordlist(infile,outfile)
	with open('../Dataset5/transcript/G-raw.tsv') as infile:
		writewordlist(infile,outfile)
	with open('../Dataset5/transcript/H-raw.tsv') as infile:
		writewordlist(infile,outfile)
	with open('../Dataset5/transcript/I-raw.tsv') as infile:
		writewordlist(infile,outfile)
	with open('../Dataset5/transcript/J-raw.tsv') as infile:
		writewordlist(infile,outfile)

with open('wlist','w') as outfile:
	with open('A.txt','r') as infile:
		mylist = infile.readlines()
		mylist.sort()
		newlist = []
		for l in mylist:
			if l not in newlist:
				newlist.append(l)
		for l in newlist:
			outfile.write(l)

