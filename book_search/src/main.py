import argparse
import os 
import sys

import elasticsearch

def main():
	parser  = argparse.ArgumentParser()
	parser.add_argument("-f","--filename",
						help="the path of file name")
	parser.add_argument("-a","--author",
						help="book's author")
	parser.add_argument("-t","--title",
						help="book's title")

	options = parser.parse_args()

	file_name = options.filename
	# Check file exists
	if not os.path.isfile(file_name):
		print("File not found" + file_name)

	# Create es instance 
	es = elasticsearch.Elasticsearch()
	
