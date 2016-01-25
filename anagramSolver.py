# --- Function that read words from a file and add them to an array.
#     Input: file path
#     Output: list of words
def read_words_from_file(file_path):
	return [line.split() for line in open(file_path, encoding="UTF-8")]

# --- Function that find all words in an array that are anagrams of each other.
#     Input: list of words
#     Output: 2D-matrix of anagrams
def find_anagrams(all_words):

	# Initialize array that will contain all anagrams found.
	all_anagrams = []

	# Run until all words have been processed.
	while all_words:

		# Pop first word in list.
		compare_word = all_words.pop(0)

		# Sort the word.
		compare_word_sorted = sorted(compare_word[0])

		# Initialize list that will contain anagrams of the word.
		anagrams = [compare_word[0]]
		
		# Iterate through the other words.
		for word in all_words:

			# 1. check for equal length because if they aren't, then they aren't anagrams.
			# 1.1 Checking for length is faster than sorting. 
			#     Would probably save runtime if the list of words was longer
			# 2. if equal length, then sort the other word and check if they are identical.
			if len(word[0]) == len(compare_word_sorted) and sorted(word[0]) == compare_word_sorted:

				# Append the found anagram to the list.
				anagrams.append(word[0])

				# Remove the found anagram from the list of all words.
				all_words.remove(word)

		# Append the list of words that are anagrams of the word to the final result.
		if len(anagrams) > 1: all_anagrams.append(anagrams)

	return all_anagrams

# --- Main
#     Input: none
#     Output: none
def main():

	# Find all anagrams.
	anagrams = find_anagrams(read_words_from_file("words.txt"))

	# Print result to console.
	for anagram in anagrams:
		temp = ""
		for word in anagram:
			temp = temp + " " + word
		print(temp)

# Run main.
main()