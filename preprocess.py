# Author: 	Joel Kemp
# File: 	preprocess.py
# Purpose: 	A collection of functions that strip unnecessary characters from tweets.
# Notes:	Tweet preprocessing is done offline, so this doesn't have to be a module.
from stemming.porter2 import stem	# Stemming algorithm
from twitter import removeAllOccurrences

def removeStopWords(data):
	"""
	Purpose: 	Removes instances of stop words from the passed list, data
	Precond: 	Data is a list of strings
	Notes: 		Inplace modification of data
				Stop words loaded from a textfile in the data/ directory.
	"""
	try:	
		stop_words = load_stop_words()
		for sw in stop_words:
			if not sw in data:
				continue
			# Remove all occurrences of that stop word
			removeAllOccurrences(sw, data)

	except Exception, e:
		print "removeStopWords:", e

def load_stop_words():
	"""
	Purpose:	Loads the stop words from file.
	Notes: 		The file is currently hardcoded.
	Returns:	A list of strings where each string is a stop word.
	"""
	file = open("data/stopwords.txt")
	stop_words = []
	for line in file:
		stop_words.append(line)
	file.close()
	# If there's only a single string
	if(len(stop_words) == 1):
		# Our stop words are a list of the string's tokens
		stop_words = stop_words[0].split()
	return stop_words

def stem(data):
	"""
	Purpose: 	Computes the stem of each word in the passed word list
	Returns:	A list containing a stem for each word in the words list
	"""
	stems = []
	for w in words:
		stems.append(stem(w))		
	return stems


def main():
	try:
		# Open the tweet file
		file = open("data/tweetsashton.txt")
		file_write = open("data/tweetsprocessedashton.txt", "w")

		# For each tweet, 
		for tweet in file:
			# split the tweet into tokens
			tokens = tweet.split()

			# Remove stop words from the list of tokens
			removeStopWords(tokens)

			# Remove the stems
			tokens = stem(tokens)

			# Convert the token list to a string representation
			token_string = "".join(tokens)

			# Store the processed tweets in a new file
			file_write.write(token_string + "\n")

		file.close()
		file_write.close()
	
	except Exception, e:
		print "Error:", e

main()