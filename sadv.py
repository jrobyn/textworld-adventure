import random
from sys import exit

##### - fight system:
def fightSystem(Uhp, He, Lvl, name):
    print("FIGHT!") #the startup stuff is decided here
    if Lvl == 1:
        Hhp = 50
    if Lvl == 2:
        Hhp = 75
    if Lvl == 3:
        Hhp = 95
    if Lvl == 4:
        Hhp = 110
    if Lvl == 5:
        Hhp = 120
    Mhp = Hhp
    Ue = 8
    print("You are attacked by {0}: level {1}!".format(He, Lvl))
    print()
    
    while (Uhp > 0) and (Hhp > 0): #the battle begins, your status is printed
        print("YOU -- {0} -- Health: {1}/100 -- Energy: {2}".format(name, Uhp,  Ue))
        print("{0} -- Level: {1} -- Health: {2}/{3} -- Infinite Energy".format(He, Lvl, Hhp, Mhp))
        print()
        Uat = input("Enter '1' to Slash (0 En) -- '2' to use Magic (2 En) -- '3' to Heal 40hp (4 En): ")
        print()
        
        if (Uat == "2") and (Ue >= 2): #this is your moveset
            Ue -= 2
            print("YOU use Death Magic to launch a fireball!")
            Ah = random.randrange(0, 7)
            if Ah == 1:
                print("Bad luck, YOU missed!")
            else:
                Ad = random.randrange(20, 44)
                Hhp = (Hhp - Ad)
                print("It's a hit! YOU deal {0} damage to {1}!".format(Ad, He))
                
        elif (Uat == "3") and (Ue > 3):
            Ue -= 4
            Uhp = (Uhp + 40)
            print("YOU use Life Magic to heal yourself!")
            print("40 Health points restored!")
            if Uhp > 100:
                Uhp = 100
            
        else:
            if (Uat == "2") or (Uat == "3"):
                print("YOU don't have enough Energy for that!")
            print("YOU swing your weapon!")
            Ah = random.randrange(0, 5)
            if Ah == 1:
                print("Bad luck, YOU missed!")
            else:
                Ad = random.randrange(10, 30)
                Hhp = (Hhp - Ad)
                print("It's a hit! You deal {0} damage to {1}!".format(Ad, He))
                
        print() #this is the enemy's moveset
        if (Hhp > 0):
            print("{0} prepares their next move...".format(He))
            wA = random.randrange(0, 4)
            if (wA == 1) and (Hhp < 90):
                Hhp = (Hhp + 20)
                print("{0} uses a health potion!".format(He))
                print("20 health points restored!")
                if Hhp > Mhp:
                    Hhp = Mhp
                
            elif (wA == 2):
                print("{0} launches a bolt of magical energy!".format(He))
                Az = random.randrange(0, 6)
                if Az == 1:
                    print("Great, {0} missed!".format(He))
                else:
                    As = random.randrange(15, 40)
                    Uhp = (Uhp - As)
                    print("It's a hit! {0} deals {1} damage to YOU!".format(He, As))
                    
            else:
                print("{0} attacks with their weapon!".format(He))
                Az = random.randrange(0, 5)
                if Az == 1:
                    print("Great, {0} missed!".format(He))
                else:
                    As = random.randrange(11, 25)
                    Uhp = (Uhp - As)
                    print("It's a hit! {0} deals {1} damage to YOU!".format(He, As))
            print()
                    
    if Uhp > 0: #the battle ends!
        print("YOU have defeated {0}!".format(He))
        print("CONGRATULATIONS!\n")
    elif Hhp > 0:
        print("YOU are defeated at {0}'s hands!".format(He))
        print("Rest in piece, {0}".format(name))
        input("\nPress ENTER to leave the game.")
        exit()
    return Uhp

###############################################################################################################

##### - chapter one modules:
def cityStuff(gold, name, rep, Uhp, inv): #main part (complete)
    
    ext = False
    dKill = False
    maid = False
    tavAs = False
    tavCp = False
    gangJ = False
    gangK = False
    treasure = False
    burn = False
    
    while ext == False:
        print("\n(Enter: '1' - Look for a Tavern (talk, heal), '2' - Look for a store (purchase, steal), '3' - Explore the southern district, '4' - Sleep")
        print("Sleeping will end this chapter of the game if you have attained a reputation of 10 or more, yours is currently {0}.".format(rep))
        print("You have {0}HP and {1} gold. In your inventory is: {2}".format(Uhp, gold, inv))
        choice = input("What do you want to do? Enter your choice: ")
        if choice == "1":
            gold, name, rep, Uhp, inv, maid, tavAs, tavCp = sadvTav(gold, name, rep, Uhp, inv, maid, tavAs, tavCp)
        elif choice == "2":
            gold, name, rep, Uhp, inv, dKill = sadvShop(gold, name, rep, Uhp, inv, dKill)
        elif choice == "3":
            gold, name, rep, Uhp, inv, gangJ, gangK, tavAs, treasure, burn = sadvSouth(gold, name, rep, Uhp, inv, gangJ, gangK, tavAs, treasure, burn)
        elif choice == "4": #sleep (complete)
            if int(rep) > 9:
                ext = True
                print("\nYou enter a den, tucked away in the quiet backstreets, and do some chores in exchange for a night's rest...")
            else:
                print("\nYou enter a den, tucked away in the quiet backstreets, and do some chores in exchange for a night's rest...\nAll goes well and you wake up the next morning feeling fresh.")
        else:
            print("Invalid choice!\n")
    return gold, name, rep, Uhp, inv

#####
##
            
def sadvTav(gold, name, rep, Uhp, inv, maid, tavAs, tavCp): #look for a tavern (complete)
    tavtil1 = ["KING", "QUEEN", "BOAR", "GOBLIN", "DEVIL", "LORD", "OGRE"]
    tavtil2 = ["ARMS", "LEGS", "FOLLY", "RETREAT", "DOWNFALL", "CHICKEN", "DANCE"]
    tavti1 = tavtil1[random.randrange(5)]
    tavti2 = tavtil2[random.randrange(5)]
    print("\nYou find a tavern, \"THE {0}'S {1}\"".format(tavti1, tavti2))
    print("The wooden door creaks as you step through; it's probably rotten. In front of you is a great variety of people. There are large gatherings of peasants and drunks, solitary warriors hanging out by the windows, and a steely bartender who watches over everything.")
    ext = False
    while ext == False:
        print("(Enter: '1' - Approach the owner of the tavern, '2' - Approach a large group, '3' - Approach a warrior, '4' - Approach a maiden, '5' - Exit the tavern)")
        choice = input("What do you want to do? Enter your choice: ")

        if choice == "1":
            print("\nThe owner, a man who has the scars of an old soldier, speaks to you in a booming voice.\n\"Interested in buying a drink, friend?\"\nHis expression does not look as friendly as the tone he puts on.")
            print("(Enter: '1' - Buy a drink (10 gold, heals you), '2' - Walk away)")
            choice = input("What do you want to do? Enter your choice: ")
            if choice == "1":
                if int(gold) > 9:
                    print("You hand 10 GOLD and take the drink, it's refreshing and you are restored to full health!")
                    gold -= 10
                    Uhp = 100
                else:
                    print("You can't afford to buy anything! You're forced to walk away.")
            else:
                print("You walk away and don't spend any money.")
                
        elif choice == "2":
            stracel = ["elves", "orcs", "goblins", "humans", "dwarves", "gnomes", "minotaurs"]
            strnamel = ["Bonecrusher", "Windslayer", "Moutheater", "Lungsucker", "Fastfoot", "Heavyblood", "Syrupeye"]
            strace = stracel[random.randrange(6)]
            strname = strnamel[random.randrange(6)]
            print("\nYou walk up to the largest gathering of people and introduce yourself proudly.\n\"{0} eh?\" says one of the {1}, \"nice to meet ya! I'm {2}!\"".format(name, strace, strname))
            print("(Enter: '1' - Converse with the group, '2' - Show off your party trick, '3' - Brawl {0}, '4' - Leave)".format(strname))
            choice = input("What do you want to do? Enter your choice: ")
            if choice == "1":
                topics = ["the great gnome civil war", "the holy revolution of Ulthor, god of fish and dandelions", "the ways in which different races eat noodles", "the controversies surrounding necromancy", "dwarvern traders", "the ugly state of the North District","minotaur civil rights"]
                topic = topics[random.randrange(6)]
                print("You have a lengthy discussion with the group about {0}, it's very enjoyable but you decide to leave before it gets too late. They all bid you farewell and you wave goodbye as you walk away.".format(topic))
            if choice == "2":
                print("You go to show off your party trick but suddenly remember that you don't actually have one. You embarrass yourself in front of everybody and sulk away in shame.")
            if choice == "3":
                print("\"You want to brawl me?\" {0} says, \"Okay! But I won't hold back!\"".format(strname))
                He = strname.upper()
                Lvl = 2
                Uhp = fightSystem(Uhp, He, Lvl, name)
                goldfound = random.randrange(15, 25)
                print("You earn {0} GOLD and +1 reputation for winning the fight! People are getting roudy, so you walk away from the group once you're done.".format(goldfound))
                gold += goldfound
                rep += 1
            else:
                print("You walk away from the group, telling them that you just remembered there's somewhere else you need to be.")

        elif choice == "3":
            if tavAs == False:
                print("\nYou approach a mysterious warrior who eyes you with suspicion. You introduce yourself and he produces a bounty.\n\"{0}, huh? You look like a fighter, and yet you're not here to kill me, so maybe you can help me instead. See this man? He's a criminal who wants me dead. If you find him in the southern district, eliminate him for me. I'll pay you the reward. That's all.\"\nThe conversation seems to be over.".format(name))
            elif tavCp == False:
                print("\nYou're spoken to immediately, \"Good job!\" he says, \"You killed the criminal from the southern district, the one who was after me.\"\n30 GOLD is shoved into your hands, and a promise that earns you +2 reputation from talk of your deeds.")
                rep += 2
                gold += 30
                tavCp = True
            else:
                print("\nThe warrior you approach would prefer to be left alone now that you've completed the task he had.")

                
        elif choice == "4":
            print("\nYou approach a fair maiden, standing all alone.\n\"Hey there!\" you say.")
            if "Fancy Hat" in inv:
                if maid == True:
                    print("It's the girl from before, she blushes when she recognises your dashing hat. You tip it to her, and at this she faints, as people begin to crowd around her you are already on your way to the door.")
                else:
                    print("Her eyes light up after seeing your 'Fancy Hat'!\n\"Oh, hey there...\" says the maiden, trailing off.\nThe two of you continue to talk for a long time, she's too distracted by your amazing fashion sense to realise that you are actually a complete loser (no offense!). You can tell that the maiden will go off and spread rumours about the 'dashing warrior' she encountered.\n+2 reputation!")
                    rep += 2
                    maid = True
                    print("You have a once in a lifetime chance to take her purse.")
                    print("(Enter: '1' - Steal the purse, '2' - Leave her purse alone)")
                    choice = input("What do you want to do? Enter your choice: ")
                    if choice == "1":
                        goldfound = random.randrange(20, 30)
                        print("You find {0} GOLD!".format(goldfound))
                        gold += goldfound
                    else:
                        print("You decide not to steal, how noble of you (coward).")
            else:
                print("She snarls and starts to turn away.\n\"Someone with your fashion sense could never associate with a fair maiden like me.\"\nThe maiden quickly moves away from you, it's pointless to talk to her as you are.")

        elif choice == "5":
            print("\nYou walk out of the tavern and back onto the bustling streets.")
            ext = True
        else:
            print("Invalid choice!\n")
    return gold, name, rep, Uhp, inv, maid, tavAs, tavCp

##

def sadvShop(gold, name, rep, Uhp, inv, dKill): #look for a store (complete)
    print("\nThe merchant's quarter of the city is just as lively as one would expect. Angry faces shout at each other as all the 'civillised' races push past each other in the busy street; everyone has a place to get to. There's a very competitive atmosphere which you don't like to be part of for too long.")
    print("You enter the closest general store, it's dark and dusty. A grimy looking dwarf peers up at you from his stool with glaring eyes. Junk is piled high on both his desk and the surrounding shelves.")
    print("\"Blagh,\" he says, spitting a little, \"what do you want? Hurry up and get outta here.\"")
    if dKill == True:
        print("You think this dwarf may be a relative of the one you killed. There are a few gaurds in the room as an increased security measure against future attacks.")
    ext = False
    while ext == False:
        print("\n(Enter: '1' - Buy a shovel (40 gold), '2' - Buy a fancy hat (60 gold), '3' - Buy a tinderbox (80 gold),  '4' - Attack the dwarf (DANGEROUS), '5' - Exit the store)")
        choice = input("What do you want to do? Enter your choice: ")

        if choice == "1":
            if int(gold) > 39:
                gold -= 50
                print("\nThe dwarf smiles and hands you the shovel, snatching the 40 GOLD from your hands.\n\"Thanks fer ya purchase!\"")
                inv.append("Shovel")
            else:
                print("\n'You aint got enough cash fer that!'")

        elif choice == "2":
            if int(gold) > 59:
                gold -= 70
                print("\nThe dwarf smiles and hands you the fancy hat, snatching the 60 GOLD from your hands and drooling a little.\n\"Thanks fer ya purchase!\"")
                inv.append("Fancy Hat")
            else:
                print("\n'You aint got enough cash fer that!'")

        elif choice == "3":
            if int(gold) > 79:
                gold -= 100
                print("\nThe dwarf smiles and hands you the tinderbox, eagerly snatching the 80 GOLD from your hands, he drools and chuckles a little.\n\"Thanks fer ya purchase!\"")
                inv.append("Tinderbox")
            else:
                print("\n\"You aint got enough cash fer that!\"")

        elif choice == "4":
            if dKill == False:
                ext = True
                print("\nYou step towards the dwarf with your sword and he quickly prepares himself for the fight ahead.")
                He = "DWARF"
                Lvl = 2
                Uhp = fightSystem(Uhp, He, Lvl, name)
                dKill = True
                print("Standing over the dead dwarf gives you a sense of power, but the gaurds will be here soon.")
                print("(Enter: '1' - Take some gold and escape, '2' - Eat the corpse)")
                choice = input("What do you want to do? Enter your choice: ")
                if choice == "1":
                    print("You have time to grab 50 GOLD before escaping the store, and you narrowly miss the gaurd's arrival.\nRumours spread about your deed, but no conviction is made, +2 reputation.")
                    gold += 50
                    rep += 2
                if choice == "2":
                    yumlist = ["a little bit salty, but otherwise fine.", "disgusting, but you realise this too late.", "the most wonderful dwarf meat you've ever had, but that doesn't say much."]
                    yum = yumlist[random.randrange(2)]
                    print("You begin eating the corpse of the shopkeeper, it's {0} Suddenly, a gaurd bursts into the building and it's time for another fight!".format(yum))
                    He = "GAURD"
                    Lvl = 3
                    Uhp = fightSystem(Uhp, He, Lvl, name)
                    print("You have time to grab 50 GOLD before escaping the store, and 10 GOLD is found on the gaurd. You narrowly miss the arrival of reinforcements.\nRumours spread about your deeds, but no conviction is made, +3 reputation.")
                    gold += 60
                    rep += 3
            else:
                print("You can't kill another dwarf now, the shop has tightened its security since the last attack and you would never succeed.")
        elif choice == "5":
            ext = True
            print("\nYou walk out of the store and back onto the bustling streets.")
        else:
            print("Invalid choice!\n")
    return gold, name, rep, Uhp, inv, dKill

##

def sadvSouth(gold, name, rep, Uhp, inv, gangJ, gangK, tavAs, treasure, burn): #explore the southern district (INCOMPLETE!!)
    print("\nThe souther district is the poorest and the dirtiest area of the city. Situated near the docks, drenched in filth, you're certainly more likely to meet a deadly outlaw than you are a gaurd. Even the ocean breeze isn't very pleasant, you don't know what people have been dumping in the water, but it's shifty.")
    ext = False
    while ext == False:
        
        print("\n(Enter: '1' - Visit the orphanage, '2' - Visit the Snakehead Gang, '3' - Visit the pawnbroker, '4' - Hunt a Criminal, '5' - Exit)")
        choice = input("What do you want to do? Enter your choice: ")

        if choice == "1":
            if burn == True:
                print("\nYou can't go there, you burnt it to the ground.")
            else:
                print("\nYou enter and see maybe a hundred suffering children recieving help from aid workers.")
                print("\"Sir, a small donation of 20 gold will go a long way.\" says one of them.")
                print("\n(Enter: '1' - Pay the money, '2' - Burn down the building, '3' - Exit)")
                choice = input("What do you want to do? Enter your choice: ")
                if choice == "1":
                    print("You hand over 20 GOLD to the sound of \"bless you sir\", you gain +1 reputation point for your good deed!")
                    gold -= 20
                    rep += 1
                elif choice == "2":
                    print("Uh, that's a bit cruel.")
                    if "Tinderbox" in inv:
                        if gangJ == True:
                            print("You start a fire with your tinderbox, then dance an evil jig around the crying orphans. On your way out of the building, you're careful to make sure that no one can follow you, and so you relax on the grass outside whilst listening to the screams of the damned.")
                            burn = True
                        else:
                            print("You have a tinderbox, but not a strong enough motive to bring yourself to carry out this act of evil, so you leave peacefully.")
                    else:
                        print("You would need a tinderbox to do that, so you leave peacefully.")
                else:
                    print("You give a couple of badly thought out reasons to explain why you don't donate, then leave the building with eyes on your back.")


        elif choice == "2":
            print("\nYou enter the lair of the Snakehead Gang.")
            if gangK == True:
                print("There is no longer anyone here...")
            elif gangJ != True:
                print("\"Hey, you think you're tough enough to be here?\"")
                print("\n(Enter: '1' - 'Yes', '2' - 'No')")
                choice = input("What do you want to do? Enter your choice: ")
                if choice == "1":
                    print("You think you're tough enough to be there.\n\"You sure?\"")
                    print("\n(Enter: '1' - 'Yes', '2' - 'No')")
                    choice = input("What do you want to do? Enter your choice: ")
                    if choice == "1":
                        print("You still think so.\n\"But are you really certain?\"")
                        print("\n(Enter: '1' - 'Yes', '2' - Attack the leader (DANGEROUS), '3' - 'No')")
                        choice = input("What do you want to do? Enter your choice: ")
                        if choice == "1":
                            print("\"Alright! Prove it then, do something really evil and then come back here.\"\nIt looks like you have a new task!")
                            gangJ = True
                        elif choice == "2":
                            print("You attack!")
                            He = "SNAKEHEAD BOSS"
                            Lvl = 3
                            Uhp = fightSystem(Uhp, He, Lvl, name)
                            print("The rest of the gang runs in fear! +2 reputation and 20 GOLD!")
                            rep += 2
                            gold += 20
                            gangK = True
                        else:
                            print("You're not tough enough, you exit in shame.")
                    else:
                        print("You're not tough enough, you exit in shame.")
                else:
                    print("You're not tough enough, you exit in shame.")
            elif burn == True:
                  print("\"Nice job burning down that orphanage! We'll credit you for it, but you can't join us, you're a little bit too evil.\"\n+3 reputation and 30 GOLD!")
                  rep += 3
                  gold += 30
                  gangK = True
            else:
                print("\"You're still not evil enough to be here yet.\"")
                print("\n(Enter: '1' - Attack the leader (DANGEROUS), '2' - Exit)")
                choice = input("What do you want to do? Enter your choice: ")
                if choice == "1":
                    print("You attack!")
                    He = "SNAKEHEAD BOSS"
                    Lvl = 3
                    Uhp = fightSystem(Uhp, He, Lvl, name)
                    print("The rest of the gang runs in fear! +2 reputation and 20 GOLD!")
                    rep += 2
                    gold += 20
                    gangK = True
                else:
                    print("You're not tough enough, you exit in shame.")

                    
        elif choice == "3":
            print("\nAn especially creepy elf man leans over to you and starts inspecting your stuff.")
            if "Clothing" in inv:
                print("\"I'll take those clothes for 20 GOLD!\"")
                print("\n(Enter: '1' - Sell your clothing, '2' - Don't make the sale)")
                choice = input("What do you want to do? Enter your choice: ")
                if choice == "1":
                    gold += 20
                    inv.remove("Clothing")
                    print("You sell your clothing for 20 GOLD and stand naked in the room.")
                else:
                    print("You decide not to sell your clothes, the elf continues looking through your stuff.")
            if "Tinderbox" in inv:
                print("\"I'll take that tinderbox for 30 GOLD!\"")
                print("\n(Enter: '1' - Sell your tinderbox, '2' - Don't make the sale)")
                choice = input("What do you want to do? Enter your choice: ")
                if choice == "1":
                    gold += 30
                    inv.remove("Tinderbox")
                    print("You sell your tinderbox for 30 GOLD.")
                else:
                    print("You decide not to sell your tinderbox, the elf continues looking through your stuff.")
            if "Fancy Hat" in inv:
                print("\"I'll take that fancy hat for 20 GOLD!\"")
                print("\n(Enter: '1' - Sell your fancy hat, '2' - Don't make the sale")
                choice = input("What do you want to do? Enter your choice: ")
                if choice == "1":
                    gold += 20
                    inv.remove("Fancy Hat")
                    print("You sell your hat for 20 GOLD.")
                else:
                    print("You decide not to sell your fancy hat, the elf continues looking through your stuff.")
            if "Shovel" in inv:
                print("\"I'll take the shovel for 10 GOLD!\"")
                print("\n(Enter: '1' - Sell your shovel, '2' - Don't make the sale)")
                choice = input("What do you want to do? Enter your choice: ")
                if choice == "1":
                    gold += 10
                    inv.remove("Shovel")
                    print("You sell your shovel for 10 GOLD.")
                else:
                    print("You decide not to sell your clothes, the elf continues looking through your stuff.")
            print("The elf finishes inspecting your things, he has no more offers to make you and so you leave.")


        elif choice == "4":
            if tavAs == False:
                print("\nYou spot someone shifty and soon recognise them as a criminal from a bounty poster.")
                He = "CRIMINAL"
                Lvl = 2
                Uhp = fightSystem(Uhp, He, Lvl, name)
                goldfound = random.randrange(1, 10)
                print("He only has {0} GOLD on him, and you only gain +1 reputation point from the handful of people who saw you, maybe you could get greater rewards if you knew who issued the bounty.".format(goldfound))
                gold += goldfound
                rep += 1
                tavAs = True
            else:
                print("You can't find anyone worth fighting, they're all petty criminals besides those hiding in large groups.")

        elif choice == "5":
            ext = True
            print("\nYou walk out of the store and back onto the bustling streets.")
        else:
            print("Invalid choice!\n")
            
    return gold, name, rep, Uhp, inv, gangJ, gangK, tavAs, treasure, burn

##
###############################################################################################################

##### __main__
Uhp = 100
rep = 1
print("Weclome to TextWorld Adventure!")
input("PRESS ENTER TO START")
name = input("\nPlease enter your name: ")
print("One day you, {0}, are reading a book about a mythical kingdom.".format(name))
land = input("What is the name of the kingdom?: ")
city = input("And of the largest city?: ")
print("One day you, {0}, are sucked into a book about the land of {1}!\n".format(name, land))
if name == "VEINS":
    gold = 1000
    rep = 10
else:
    gold = 20
inv = ["Sword", "Clothing"]

print("Welcome to {0}! City of heroes... and losers. Close to the demonic forest of the Blood King, but also a centre of trade and commerce, all kinds of people flock here for various reasons. In a place like this, fame and glory are things achieved by very few people; you will have to fight hard to earn acknowledgement.\n".format(city))
print("You have {0} gold to your name!".format(gold))
print("\nCHAPTER I: THE ROAD TO SUCCESS")
gold, name, rep, Uhp, inv = cityStuff(gold, name, rep, Uhp, inv)

###############################################################################################################

print("You wake up early to a knock on your door, and open it with one hand on your sword hilt.")
print("'I am Gaelin, and I mean you no harm! You are {0}, correct?'".format(name))
print("\nCHAPTER II: THE TORMENT OF THE BLOOD KING")
print("He explains that he has heard of your reputation, and believes that only you can assist him in his quest to slay the Blood King of the far isles. After some persuasion, in which he promises you that great tresure awaits, you agree to go with Gaelin and fight the darkness.\nThe journey is long and cold, but you endure it well. Gaelin turns out to be a very good travel partner! However, after trekking through a dark forest for a couple of days, a band of goblins jump out in ambush!\n")
Uhp = 100
He = "UGLY GOBLIN"
Lvl = 1
Uhp = fightSystem(Uhp, He, Lvl, name)
print("\nYou slaughter the goblin and watch his head said through the air in an arc. It was an easy kill, but the battle isn't over, and another goblin charges for you! Luckily, Gaelin notices that you're in distress and he quickly chucks you a health potion.\n")
Uhp = 100
He = "BRUTISH GOBLIN"
Lvl = 1
Uhp = fightSystem(Uhp, He, Lvl, name)
print("\nIn the aftermath of the battle, you and Gaelin stand victorious together.\n\"This battle will be just one of many, friend. The Blood King's castle is just up ahead!\"\nAnd so it was... Gaelin pointed out the dreaded BLACK KNIGHT who stood gaurd, and explained his strategy. He would open the gate while you fought, but as the knight was an especially strong foe, Gaelin would also supply you with a unique potion to raise your health above the normal standard! It might not assure victory, and its effect can be broken by a health potion, but it could turn the tides.\nAnd so you approach the knight...\n")
Uhp = 150
He = "BLACK KNIGHT"
Lvl = 5
Uhp = fightSystem(Uhp, He, Lvl, name)
print("\nAha! You win a great victory, and slay the evil knight! And so you and Gaelin march into the castle together, worried about what might lie inside...\nGaelin heals you, but says that it's for the last time, as he's now all out of medical supplies. You continue through the castle until you encounter another enemy: a demonic minion of the king. This signifies that he knows you're here.\n")
Uhp = 100
He = "DEMON MINION"
Lvl = 1
Uhp = fightSystem(Uhp, He, Lvl, name)
print("\nThe demon falls to a joint assault from you and Gaelin, and you hurry through the caslte halls. Up ahead are two rooms, one is blocked by a dirt wall, and if you have a shovel...")
if "Shovel" in inv:
    print("You do! You break away the dirt and find a pool of healing in the hidden room. This is good news, and you both drink from here quickly before moving on.")
    Uhp = 100
else:
    print("Never mind, you don't, so you just move on.")
print("You enter through the other door, and meet with yet another demon, this one is greater than the last. Fresh blood drips from his teeth, but he is still hungry for yours!\n")
He = "DEMON WARRIOR"
Lvl = 3
Uhp = fightSystem(Uhp, He, Lvl, name)
print("Another win... or so you think... before you notice that Gaelin was cut wide open. Hardly a moment goes by before your friend is dead. A blackness enters your heart. It's terrible, but you know that it's too late to give up. You must avenge Gaelin, you must meet the Blood King in his throne room, and you must complete the quest...\n")

###############################################################################################################

print("CHAPTER III: A FINAL CONFRONTATION")
print("You push open a pair of heavy double doors to reveal a grand carpet stretching up to the Blood King's mighty throne. Torches light the dusty stone hall, which reaches up forever into aerial darkness.")
if "Clothes" not in inv:
    print("The Blood King begins to ask why you're not wearing clothes, but decides against it. It's time for you to die.")
print("\"A puny human like you... how dare you enter my lair!\" he roars, \"And the state you're in... don't you realise how weak you look to a being such as I?\"")
print("You raise your sword. Is this it? It's hard to believe how fast you achieved glory in the city... It's hard to believe how Gaelin found you for such a grand quest... And it's hard to believe you've survived this long... Maybe this is the end of the line?\n")
print("You put aside your doubts and gather all your strength for one invigorating final push, restoring your spirits.\n")
Uhp = 100
He = "BLOOD KING"
Lvl = 4
Uhp = fightSystem(Uhp, He, Lvl, name)
print("Somehow... somehow you have achieved victory. Total victory! The demons of the castle vanish, no longer supported by the Blood King's magic. The Blood King's corpse lies a hollow shell impaled on a pointless throne. Now, about that treasure...")
print("\nA few weeks later you have sold most of what you managed to loot from the Blood King's treasury, and you've certainly made quite a profit! Not only this, but the bards sing stories of how you cleansed the far isles from demon influence, and entire villages crowd to listen.\nYou're a real hero now!")
print("\nTHE END")
input("PRESS ENTER TO FINISH")
