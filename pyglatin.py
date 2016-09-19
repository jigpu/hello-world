print "Welcome to the Pig Latin Translator! \n"

pyg = "ay"
original = raw_input("Enter a word: ")

if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	if word[0] != "a" or "e" or "i" or "o" or "u":
		new_word = word + first + pyg
		new_word = new_word[1:]

	else:
		new_word = word + pyg
		new_word = new_word[0:]

	print "\n"
	print new_word

elif len(original) == 0:
	print "Um, I'm waiting! \n"

elif original.isalpha() == False:
	print "No, not l33t. A WORD, please. \n"

else:
	print "Wow, you broke the program. How the hell did you do that?! \n"
