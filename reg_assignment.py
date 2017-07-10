#!/usr/bin/python
import re
sample_file= open("pythonweb/regex_sum_318665.txt","r")
num_list= list()
total=0
for line in sample_file:
	numbers=re.findall('([0-9]+)',line)
	if len(numbers)==0:
		continue
	#num= sum(int(numbers))
	num_list= num_list + numbers
for (num) in num_list:
	total= total + int(num)

print total
