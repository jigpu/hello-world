'''Jason's  less-optimal blending fix: 
def will_it_blend(word):
       blends = [ "bl", "br", "bw", "ch", "cl", "cr", "cs", "cw", "cz" ]
       for prefix in blends:
               if word.startswith(prefix):
                       return True
       return False


Jason's more optimal blending fix:
blends = ( "bl", "br", "bw", "ch", "cl", "cr", "cs", "cw", "cz" )

then add "elif: word.startswith(blends)" to the end of the blends section

'''

###   Welcome to my modified version of Codecademy's PygLatin program!
###   Instead of just taking the first letter of any word, slapping it on the end
###   and tacking on "ay," I've added functionality to help the program render
###   Pig Latin more like a human would. 
###
###   In this program, words that start with a vowel keep the first letter in place
###   and only add "ay" (e.g., "apple" becomes "appleay"). It also searches for
###   blends and renders them at the end of the word together (e.g., "blast" becomes
###   "astblay").

print "Welcome to the Pig Latin Translator! \n"

pyg = "ay"
original = raw_input("Enter a word: ")

if len(original) > 0 and original.isalpha():
	word = original.lower()

	if word[0:2] == "bl" or word[0:2] == "br"\
		or word[0:2] == "bw"\
		or word[0:2] == "ch"\
		or word[0:2] == "cl"\
		or word[0:2] == "cr"\
		or word[0:2] == "cs"\
		or word[0:2] == "cw"\
		or word[0:2] == "cz"\
		or word[0:2] == "dh"\
		or word[0:2] == "dj"\
		or word[0:2] == "dr"\
		or word[0:2] == "fl"\
		or word[0:2] == "fr"\
		or word[0:2] == "fw"\
		or word[0:2] == "gh"\
		or word[0:2] == "gl"\
		or word[0:2] == "gn"\
		or word[0:2] == "gr"\
		or word[0:2] == "gw"\
		or word[0:2] == "hr"\
		or word[0:2] == "jh"\
		or word[0:2] == "jr"\
		or word[0:2] == "jw"\
		or word[0:2] == "kh"\
		or word[0:2] == "kl"\
		or word[0:2] == "kn"\
		or word[0:2] == "kr"\
		or word[0:2] == "kw"\
		or word[0:2] == "lh"\
		or word[0:2] == "mn"\
		or word[0:2] == "pf"\
		or word[0:2] == "ph"\
		or word[0:2] == "pl"\
		or word[0:2] == "pn"\
		or word[0:2] == "pr"\
		or word[0:2] == "ps"\
		or word[0:2] == "qu"\
		or word[0:2] == "rh"\
		or word[0:2] == "sc"\
		or word[0:2] == "sh"\
		or word[0:2] == "sk"\
		or word[0:2] == "sl"\
		or word[0:2] == "sm"\
		or word[0:2] == "sn"\
		or word[0:2] == "sp"\
		or word[0:2] == "sr"\
		or word[0:2] == "st"\
		or word[0:2] == "sw"\
		or word[0:2] == "th"\
		or word[0:2] == "tr"\
		or word[0:2] == "ts"\
		or word[0:2] == "tw"\
		or word[0:2] == "vl"\
		or word[0:2] == "vr"\
		or word[0:2] == "wh"\
		or word[0:2] == "wr"\
		or word[0:2] == "xh"\
		or word[0:2] == "zh"\
		or word[0:2] == "zw":
		first = word[0:2]
		new_word = word + first + pyg
		new_word = new_word[2:]
	
	elif word[0] in "aeiou":
		new_word = word + pyg
		new_word = new_word[0:]
	
	else:
		first = word[0]
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
