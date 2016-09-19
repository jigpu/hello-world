print "Welcome to the Pig Latin Translator! \n"

pyg = "ay"
original = raw_input("Enter a word: ")

if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	
	if word[0] in "aeiou":
		new_word = word + pyg
		new_word = new_word[0:]

	##elif word[0:1] == "bl"\
	##	or "br"\
	##	or "bw"\
	##	or "ch"\
	##	or "cl"\
	##	or "cr"\
	##	or "cs"\
	##	or "cw"\
	##	or "cz"\
	##	or "dh"\
	##	or "dj"\
	##	or "dr"\
	##	or "fl"\
	##	or "fr"\
	##	or "fw"\
	##	or "gh"\
	##	or "gl"\
	##	or "gn"\
	##	or "gr"\
	##	or "gw"\
	##	or "hr"\
	##	or "jh"\
	##	or "jr"\
	##	or "jw"\
	##	or "k
	
	else:
		new_word = word + first + pyg
		new_word = new_word[1:]

	print "\n"
	print new_word

elif len(original) == 0:
	print "Um, I'm waiting! \n"

elif original.isalpha() == False:
	print "No, not l33t. A WORD, please. \n"

else:
	print "Wow, you broke the program. How the hell did you do that?! \n"
