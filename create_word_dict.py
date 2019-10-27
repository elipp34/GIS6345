Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> fin = open ('c:/python27/words.txt')
>>> def create_word_dict():
	word_dict = dict()
	for line in fin:
		word = line.strip()
		word_dict[word] = word
	return word_dict
