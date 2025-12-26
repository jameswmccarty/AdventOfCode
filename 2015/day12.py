#!/usr/bin/python

import json


def json_doc_int_sum(doc):
	sub_sum = 0
	if type(doc) is int:
		sub_sum += doc
	elif type(doc) is list:
		for elem in doc:
			sub_sum += json_doc_int_sum(elem)
	elif type(doc) is dict:
		for elem in doc:
			sub_sum += json_doc_int_sum(doc[elem])
	return sub_sum

def json_doc_int_sum_nored(doc):
	sub_sum = 0
	if type(doc) is int:
		sub_sum += doc
	elif type(doc) is list:
		for elem in doc:
			sub_sum += json_doc_int_sum_nored(elem)
	elif type(doc) is dict:
		if "red" not in doc.values():
			for elem in doc:
				sub_sum += json_doc_int_sum_nored(doc[elem])
	return sub_sum
	
if __name__ == "__main__":

	document_sum = 0

	# Part 1 Solution
	with open("day12_input", "r") as infile:
		doc = json.loads(infile.read().strip())
	
	print json_doc_int_sum(doc)
	
	# Part 2 Solution
	
	print json_doc_int_sum_nored(doc)
	
	
