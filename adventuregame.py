### Defines the print output for each room.
### Rm0 is the entry room.
### RmLx are rooms on the left.
### RmRx are rooms on the right.
### Rm1 is the final dungeon.

Rm0 = "\n You walk into the first room. The game designer will eventually get around to adding descriptions."
RmL1 = "\n This is the first room on the left. It's probably creepy. There's a +20HP potion here."
RmL2 = "\n This is the second room on the left. There's a chest with +100 gold."
RmL3 = "\n This is the third room on the left. Omg, there's a monster. You can strike, cower, or run."
RmR1 = "\n Ack! A monster! You can strike, cover, or run."
RmR2 = "\n More potion."
RmR3 = "\n A chest! Wow."
Rm1 = "\n There's a boss monster here. You should try to kill it."

### Defines the exception output for each typing possibility.

lr_exception = "No, no, no. Type 'left' or 'right'. It's not that hard."
fb_exception = "You can't go through solid rock, dude. Type 'forward' or back'. Those are the only places with doors."
scr_excpetion = "No, that's not an option. Type 'strike', 'cower', or 'run'."
oc_exception = "You can't have your cake and eat it too. Type 'open' or 'leave'."

### Defines all starting values. These will be added to and subtracted from throughout the game.

### PC values
PC_HP = 100
PC_gold = 0
PC_strike = 10

### Monsters/Boss
RmL3_M_HP = 30
RmL3_M_strike = 10
RmR1_M_HP = 30
RmR1_M_strike = 10
Boss_HP = 40
Boss_strike = 20

### Potions
RmL1_potion = 20
RmR2_potion = 20

### Chests
RmL2_chest = 200
RmR3_chest = 150

### Monster options:
###   - Strike: -10HP to Monster
###   - Cower: -0HP to Monster, -10HP to PC
###   - Run: -0HP to Monster, -0HP to PC, go back to previous room
###
### Boss options:
###   - Strike: -10HP to Boss
###   - Cower: -0HP to Boss, -20HP to PC
###   - Run: -0HP to Monster, -0HP to PC, go back to previous room

### Defines gibberish and bad_end, which I use to avoid the need for loops. :p

gibberish = "\n Nope. Sorry. The programmer is far too lazy to take invalid input. Please think about what you've done and start the game again...IF YOU DARE!!!"
bad_end = "\n It's been a fun adventure, but you figure you got out while you were ahead. You walk into the distance, toward a new life, a new horizon, away from the programmer too lazy to write the (not actually) infinite IF statements it would take to make this game loop without GOTO statements. ~~~THE END~~~"

print Rm0
direction1 = raw_input("\n Do you want to go left or right?: ")
direction1 = direction1.lower()

if direction1 == "left" or direction1 == "l":
	print RmL1
	status1 = raw_input("\n Do you want to drink it? ")
	status1 = status1.lower()

	if status1 == "yes" or status1 == "y":
		print "\n Health tastes awful. But now you have 120HP, so, eh."
		PC_HP = PC_HP + RmL1_potion
		RmL1_potion = RmL1_potion - RmL1_potion
		
		'''
		FOR TESTING: the ability to print the values of varibles changed in the previous lines!
		print PC_HP
		print RmL1_potion
		'''
		
		direction2 = raw_input("\n Okay, nothing left here. Do you want to go forward or back? ")
		direction2 = direction2.lower()
		
		if direction2 == "forward" or direction2 == "f":
			print RmL2
			status2 = raw_input("\n Do you want to take it?")
			status2 = status2.lower()
			
			if status2 == "yes" or status2 == "y":
				print "\n Oh my god, you're a theif! Where are the cops when you need them? >_>"
				PC_gold = PC_gold + RmL2_chest
				RmL2_chest = RmL2_chest - RmL2_chest
				
				'''
				FOR TESTING: the ability to print the values of varibles changed in the previous lines!
				print PC_gold
				print RmL2_chest
				'''
				
				direction3 = raw_input("\n Well, you already stole everything (and I'll never forgive you). Do you want to go forward or back? ")
				direction3 = direction3.lower()
				
				if direction3 == "forward" or direction3 == "f":
					print RmL3
				
				elif direction3 == "back" or direction3 == "b":
					print bad_end
					print "Your health:" 
					print PC_HP
					print "Your gold:"
					print PC_gold
					
				else:
					print gibberish
				
			elif status2 == "no" or status2 == "n":
				direction3 = raw_input("\n You're kidding, right? It's just sitting there! Well, whatever. So, do you want to go forward or back?" )
				direction3 = direction3.lower()
				
				if direction3 == "forward" or direction3 == "f":
					print RmL3
					
				elif direction3 == "back" or direction3 == "b":
					print bad_end
					print "Your health:" 
					print PC_HP
					print "Your gold:"
					print PC_gold
					
				else:
					print gibberish
				
			else:
				print gibberish
			
		elif direction2 == "back" or direction2 == "b":
			print Rm0
			print bad_end
			print "Your health:" 
			print PC_HP
			print "Your gold:"
			print PC_gold
				
		else:
			print gibberish
		
	elif status1 == "no" or status1 == "n":
		print "\n Meh. Your funeral. So, you can go forward or back."
		
		'''
		FOR TESTING: the ability to print the values of varibles changed in the previous lines!
		print PC_HP
		print RmL1_potion
		'''
	
	else:
		print gibberish
	
elif direction1 == "right" or direction1 == "r":
	print RmR1
	
else:
	print gibberish


'''print RmL1
print RmL2
print RmL3
print RmR1
print RmR2
print RmR3
print Rm1
print lr_exception
print fb_exception
print scr_excpetion
print oc_exception'''
