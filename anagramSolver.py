'''Input file format: One line with all words. Each word is separated by a comma.'''

# --- Function that read words from a file and add them to an array.
#     Input: file path
#     Output: list of words
def read_words_from_file(file_path):
	return [line.split() for line in open(file_path, encoding="UTF-8")]

# --- Function that find all words in an array that are annagrams of each other.
#     Input: list of words
#     Output: 2D-matrix of annagrams
def find_anagrams(all_words):

	# Initialize array for all annagrams.
	all_annagrams = []

	# When list is empty all words have been added to an annagram list.
	while all_words:

		# Pop first word in list.
		compare_word = all_words.pop(0)

		# Sort the compare word.
		compare_word_sorted = sorted(compare_word[0])

		# List of anagrams to compare_word.
		annagrams = [compare_word[0]]
		
		# Iterate through the rest of the words.
		for word in all_words:

			# 1. check for equal length because it is faster    
			# 2. if equal length -> sort and check if words are annagrams
			if len(word[0]) == len(compare_word_sorted) and sorted(word[0]) == compare_word_sorted:

				# Append the found annagram to a list.
				annagrams.append(word[0])

				# Remove the found annagrams from the list of all words.
				all_words.remove(word)

		# Append the list of new annagrams to the final result.
		if len(annagrams) > 1: all_annagrams.append(annagrams)

	return all_annagrams

# --- Main
#     Input: none
#     Output: none
def main():

	# Find all annagrams.
	annagrams = find_anagrams(read_words_from_file("words.txt"))

	# Print result to console.
	for annagram in annagrams:
		temp = ""
		for word in annagram:
			temp = temp + " " + word
		print(temp)

# Run main.
main()