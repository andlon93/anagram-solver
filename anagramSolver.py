'''Input file format: One line with all words. Each word is separated by a comma.'''
def read_words_from_file(file_path):
	return [line.split() for line in open(file_path, encoding="UTF-8")]
#
def find_anagrams(all_words):
	all_annagrams=[]
	while all_words:#when list is empty all words have been added to an annagram list.
		compare_word = all_words.pop(0)#pop first word in list
		compare_word_sorted = sorted(compare_word[0])#sort the compare word
		annagrams = [compare_word[0]]#list of anagrams to compare_word
		#
		for word in all_words:#iterate through the rest of the words
			'''1. check for equal length because it is faster
			   2. if equal length -> sort and check if words are annagrams
			   2. if word is annagram, it can be removed from all_words'''
			if sorted(word[0]) == compare_word_sorted:
				annagrams.append(word[0])
				all_words.remove(word)
		if len(annagrams)>1: all_annagrams.append(annagrams)
	return all_annagrams
def main():
	annagrams = find_anagrams(read_words_from_file("words.txt"))
	for annagram in annagrams:
		temp = ""
		for word in annagram:
			temp = temp+" "+word
		print(temp)
main()