### Defines the print output for each room.
### Rm0 is the entry room.
### RmLx are rooms on the left.
### RmRx are rooms on the right.
### Rm1 is the final dungeon.

Rm0 = "You walk into the first room. The game designer will eventually get around to adding descriptions. Do you want to go left or right?"
RmL1 = "This is the first room on the left. It's probably creepy. There's a +20HP potion here."
RmL2 = "This is the second room on the left. There's a chest with +100 gold."
RmL3 = "This is the third room on the left. Omg, there's a monster. You can strike, cower, or run."
RmR1 = "Ack! A monster! You can strike, cover, or run."
RmR2 = "More potion."
RmR3 = "A chest! Wow."
Rm1 = "There's a boss monster here. You should try to kill it."

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

###Monsters/Boss
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

print "You walk into the first room. The game designer will eventually get around to adding descriptions. \n"
direction = raw_input("Do you want to go left or right?: ")
direction = direction.lower()

if direction == "left" or direction == "l":
	print RmL1
	
elif direction == "right" or direction == "r":
	print RmR1
	
else:
	print "\n What weird language was that?! In ENGLISH, please. Type 'left' or 'right.'"


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
