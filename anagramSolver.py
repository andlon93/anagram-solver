'''Input file format: One line with all words. Each word is separated by a comma.'''
def read_words_from_file(file_path):#read in each word from file
	return [line.strip().split(',') for line in open(file_path+".txt", "r")][0]
#
def find_anagrams(all_words):
	while all_words:#when list is empty all words have been added to an annagram list.
		compare_word = all_words.pop(0)#pop first word in list
		compare_word_sorted = sorted(compare_word)#sort the compare word
		annagrams = [compare_word]#list of anagrams to compare_word
		#
		for word in all_words:#iterate through the rest of the words
			'''1. check for equal length because it is faster
			   2. if equal length -> sort and check if words are annagrams
			   2. if word is annagram, it can be removed from all_words'''
			if len(word) == len(compare_word) and sorted(word) == compare_word_sorted:
				annagrams.append(word)
				all_words.remove(word)
		print ("Annagrams: ",annagrams)
find_anagrams(read_words_from_file("words"))