##HCD Final Fantasy test v .3 last update 4/28/15
##Multi character, mapped, simple AI, single weapon, 4 race, single ability
#tested with two enemy types (goblin/orc), attack, defend, run all work, melee, magic, defend all work
#going to add more enemies, more full location list, better user interaction (clean screens, list of stats)
#mapgen created, gives map, and a separate file with sorted locations to make easier to test
#try created to check for file in two places before kicking an error
#created inventory, will add items as needed, deciding on weight calc

import math, sys, random, time
pname=""#primary name
sname=""#secondary name
tname=""#third name
race=""
race2=""
race3=""
stats={'health':0,'strength':0,'magic':0,'stamina':0,'accuracy':0,'speed':0} #stats dictionary starts at 0
estats={'health':1,'strength':0,'magic':0,'stamina':0,'accuracy':0,'speed':0,'c':0} #estats dictionary starts at 0
gold=1000 #starting global gold
loc={'x':0,'y':0}#location by dictionary
dlvl=0#difficulty level, will be increased over time
dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}#first roll of dice, rolled at the beginning of all functions to see if needed
inv=[]#inventory starts empty



def maingreeting(): #only on game open
    print('''---------------------------------
Welcome to Paradisio, the land of near paradise....
---------------------------------''')
    #get new/load game input
    c=input('''
1. New Game
2. Load Game
''')
    try:#test for 1,2
        c=int(c)
    except ValueError:
        print('INVALID')
        maingreeting()
    if c==1:
        newg()#call new game
    elif c==2: #call load file
        load()
    else:
        print('INVALID')#catch
        maingreeting()

def newg(): #start new game, player name and race globalized
    global pname, race
    print('''---------------------------------
You have awoken in a land that is new to you, feeling as though you have been
forgotten, as you have forgotten all of your life. You are clothed in simple
rags, hungry, and without defense. You are greeted by a child from a nearby village
who found you on the roadside.
---------------------------------''')
    pname=input('Young girl: What is your name traveler? ')
    pname=pname.strip("'")
    human_choice=input('Greetings %s, you look different than the rest of us? Are you even human? (y/n)'%pname) #change pname and greet
    if human_choice=='y': #if human change race and call human function
        print('Young girl: Oh, it must have just been how dirty you were. Good luck on your travels.')
        race='h'
        human()
        travelchoice()
    elif human_choice=='n':
        print('Young girl: Oh... well... what are you?') #call racechoice if not human
        racechoice()
    else:
        newg()
def racechoice(): #allows other races, changes race, calls race function to update stats
    global pname,race
    r_choice=input('''---------------------------------
Choose one from below
1. Human
2. Elf
3. Troll
4. Dwarf
Enter the number: ''')
    if r_choice=='1':
        print("""Young girl: Um... ok, you just said you weren't a human, apparently you took a hard hit to the head!

""")
        race='h'
        human()
    elif r_choice=='2':
        print("""Young girl: I've never met an Elf before, you look strange... yet kind of beautiful. I hope you won't hurt us

              """)
        race='e'
        elf()
    elif r_choice=='3':
        print("Young girl: AHHHH!!!")
        print('''The young girl runs away. She seems frightened by your appearance.
It may be difficult to make friends here,
this land is not used to evil creatures like you. At least they won't bug you either

''')
        race='t'
        troll()
    elif r_choice=='4':
        print("""Young girl: Explains why you are so short.
You look silly, I'm going to go tell my friends I saw a silly creature!

""")
        race='d'
        dwarf()
    else:
        racechoice()
    travelchoice()
def human():#human race chosen, update global stats dictionary with random rolls
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global stats#use global stats
    print('Human')
    stats['strength']=random.randint(1,18)
    if stats['strength']<8:
        stats['strength']+=1
    stats['magic']=random.randint(1,18)
    stats['stamina']=random.randint(1,18)
    if stats['stamina']<8:
        stats['stamina']+=2
    stats['accuracy']=random.randint(1,18)
    stats['speed']=random.randint(1,18)
    stats['health']=100
    print('Your character has the following stats:')
    print(stats)
    print('----------------------------------------')
def elf():#elf race chosen, update global stats dictionary with random rolls
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global stats
    print('Elf')
    stats['strength']=random.randint(1,18)
    stats['magic']=random.randint(1,18)
    if stats['magic']<8:
        stats['magic']+=1
    stats['stamina']=random.randint(1,18)

    stats['accuracy']=random.randint(1,18)
    if stats['accuracy']<8:
        stats['accuracy']+=3
    stats['speed']=random.randint(9,18)
    stats['health']=110
    print('Your character has the following stats:')
    print(stats)
    print('----------------------------------------')
    
def troll():#troll race chosen, update global stats dictionary with random rolls
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global stats
    print('Troll')
    stats['strength']=random.randint(9,18)#troll only one with predetermined ranges for their stats, no plusses. goes low and high
    stats['magic']=random.randint(1,15)
    
    stats['stamina']=random.randint(9,18)

    stats['accuracy']=random.randint(1,14)
    stats['speed']=random.randint(1,10)
    stats['health']=125
    print('Your character has the following stats:')
    print(stats)
    print('----------------------------------------')
    
def dwarf():#dwarf race chosen, update global stats dictionary with random rolls
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global stats
    print('Dwarf')
    stats['strength']=random.randint(1,18)
    if stats['strength']<10:
      stats['strength']+=3
    stats['magic']=random.randint(1,18)
    if stats['magic']>16:
        magic-=1
    stats['stamina']=random.randint(1,18)
    if stats['stamina']<10:
      stats['stamina']+=3
    stats['accuracy']=random.randint(1,18)
    stats['speed']=random.randint(1,16)
    stats['health']=100
    print('Your character has the following stats:')
    print(stats)
    print('----------------------------------------')
    
def travelchoice():#this is to choose direction, and speed. gives location first, also shows health and gold
    print('----------------------------------------')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global loc,pname,race
    print('Health: %r %r    Gold: %r'%(pname.strip("'"),stats['health'],gold))
    print('%r, your current location is %r'%(pname.strip("'"),loc))
    print('''

What direction shall we travel?
N: North
E: East
S: South
W: West
I: Inventory
H: Use Heal Potion

''')
    d=input('Direction?: ').lower()
    if d=='n':
        print('North')
    elif d=='e':
        print('East')
    elif d=='s':
        print('South')
    elif d=='w':
        print('West')
    elif d=='i':
        print(inv)
        travelchoice()
    elif d=='h':
        heal()
    else:
        print('ERROR')
        travelchoice()
        
    print('''
How fast?
1-Regular
2-Fast
3-Sprint
''')
    s=input('Speed: ')
    try:
        s=int(s)
        if s==1:
            s==1
        elif s==2:
            s==2
        elif s==3:
            s==3
        elif s==4:#only available for elves
            if race=='e':
                print('SUPERSPEED!')
            else:
                print("You can't go that fast!")
                s==3
        else:
            print('ERROR')
            travelchoice()
    except ValueError:
        print('ERROR')
        travelchoice()
    totalmv=s #move was originally times a random number, now it is purely based on speed chosen
    print('You moved %i spaces'%totalmv)
    if d=='n': #change x/y based on direction and speed
        loc['y']+=totalmv
    elif d=='s':
        loc['y']-=totalmv
    elif d=='e':
        loc['x']+=totalmv
    elif d=='w':
        loc['x']-=totalmv
    print(loc)
    locchk()
    
def locchk():#check loccheck.txt file for encounters, if nothing found then random result that can be nothing or anything else
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    try:
        ref=open('loccheck.txt','r')#check for check file in current directory
    except:
        ref=open('storage/sdcard0/Download/loccheck.txt','r')#check android download folder

        
    line=ref.readline()
    
    while line:
        values=line.split()
        check={'x':int(values[0]),'y':int(values[1])}
        if check.items()==loc.items():
            event(values[2])
            break
        line=ref.readline()
    print('----------------------------------------')
    print('By random chance...')#if current location not found in loccheck file, random event is pulled
    randevent()
    time.sleep(1)
    travelchoice()
    ref.close()
def event(etype):#if an event is found, a letter is passed that determines the event type
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if etype=='a':#a calls enemy, b is treasure, c is trap, d is merchant, e is random for now (will have friend and city
        print('You have encountered an enemy!')
        enemy()
    elif etype=='b':
        
        treasure()
    elif etype=='c':
        trap()
    elif etype=='d':
        merchant()
    elif etype=='e':
        randevent()
    else:
        print('Error, my bad :(')
        travelchoice()
    
def load():#will have load ability
    print('Load')
    
def enemy():#chooses enemy, highest chance is goblin, then orc, then trap least likely
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    e=random.randint(1,10)
    if e<=5:
        goblin(estats)
    elif e<=8:
        orc(estats)
    else:
        trap()
    
    travelchoice()
def heal():
    print('heal')
    
def treasure():#gives treasure based on d20 roll, you can actually lose gold on a 1, on 19 or 20 you get nothing
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global gold
    chance=dice['20r']
    if chance<19 and chance>=2:
        print('You found treasure!')
        tre=dice['20r']*chance
        print('You found %r gold!'%tre)
        gold+=tre
        travelchoice()
    elif chance<2:
        print('You unfortunately have lost some of your gold!')
        tre=dice['20r']*chance
        print('You lost %r gold!'%tre)
        gold-=tre
        travelchoice()
    else:
        print('You thought you saw something, but must have just been your imagination')
        travelchoice()

    
def randevent():#random event, most likely nothing, then enemy, then treasure
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    num=random.randint(1,10)
    if num<=7:
        print('An uneventful day ends')
        print('----------------------------------------\n\n')
    elif num<=9:
        enemy()
    elif num==10:
        treasure()
    travelchoice()

    
def merchant():#find a sales person
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    print('You run into a merchant, looking to sell some merchandise')
    print('''
Would you like to buy something?
''')
    x=input('Yes or no? ').lower()
    if x=='yes':
        lvlstore=random.randint(1,10)
        store(lvlstore)
    elif x=='no':
        print('OK, bye!')
        time.sleep(1)
        travelchoice()
    else:
        merchant()
    travelchoice()
    
def store(level):
    global gold,inv
    try:
        ref=open('store.txt','r')#check for check file in current directory
    except:
        ref=open('storage/sdcard0/Download/store.txt','r')#check android download folder

    
    if level<=6:
        l=1
    elif level<=9:
        l=2
    else:
        l=3
    available=[]
    line=ref.readline()
    while line:
        values=line.split(';')
        info={'li':int(values[0]),'name':values[1],'type':values[2],'cost':values[3].strip()}#info=level item, name, type, and cost
        if info['li']==l:
            print("Item: %r, Cost: %r"%(info['name'],info['cost']))
        line=ref.readline()
    ref.close()
    choice=input('Would you like to buy something? ')
    if choice.lower()=='yes':
        try:
            ref=open('store.txt','r')#check for check file in current directory
        except:
            ref=open('storage/sdcard0/Download/store.txt','r')#check android download folder
        ch=input('What would you like to buy? ').lower()
        line=ref.readline()
        while line:
            values=line.split(';')
            info={'name':values[1],'cost':values[3].strip()}#info=level item, name, type, and cost
            if info['name'].lower()==ch:
                print('Cost is %r'%info['cost'])
                ch2=input('Want to buy? ').lower()
                if ch2=='yes':
                      if gold-int(info['cost'])>=0:
                          print('You bought it!')
                          inv.append(info['name'])
                          store(level)
                      else:
                          print('NOT ENOUGH MONEY!')
                          store(level)
  
            line=ref.readline()
        
    elif choice.lower()=='no':
        print('Ok, bye')
        time.sleep(1)
        travelchoice()
    else:
        store(level)


        
def city():
    
    print('city')
    travelchoice()

def trap():#trap, auto damage unless avoided with d20 chance roll
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    chance=dice['20r']
    if chance<17:
        print('AH! You stepped on a trap!')
        dmg=dice['10r']
        stats['health']-=dmg
        travelchoice()
    else:
        print('You found a trap, but were able to avoid it.')
        travelchoice()
def orc(estats):#orc, gets estats passed to it
    if estats['health']<=0:
        print('You killed it!')
        estats['c']=0
        treasure()
        travelchoice()
    print('----------------------------------------\n\n')
    
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if estats['c']==0:
        nume=1
        print('You have met %i orcs!'%nume)
        
        estats={'health':15,'strength':10,'magic':0,'stamina':5,'accuracy':3,'speed':11,'c':1}
    print('Your health=%r          Enemy health=%r'%(stats['health'],estats['health']))
    a=act()#get action
    if a==1:
        b=atype()
        if b==1:
            astr=dice['8r']*stats['strength']
            estr=dice['8r']*estats['strength']
            if astr>estr:
                dmg=dice['8r']+stats['strength']/10
                print('You did %f damage!'%dmg)
                estats['health']-=dmg
                orcact(estats)
                if estats['health']<=0:
                    print('You killed it!')
                    estats['c']=0
                    travelchoice()
                    ###------------------------------------------------
                else:
                    orcact(estats)
            elif astr==estr:
                print("It's a draw!")
                orcact(estats)
            elif astr<=estr:
                print("You miss!")
                orcact(estats)
        elif b==2:
                astr=dice['8r']*stats['magic']
                estr=dice['8r']*estats['magic']
                if astr>estr:
                    dmg=dice['8r']+stats['magic']/10
                    print('You did %f damage!'%dmg)
                    estats['health']-=dmg
                    if estats['health']<=0:
                        print('You killed it!')
                        estats['c']=0
                        travelchoice()
                        ###------------------------------------------------
                    else:
                        orcact(estats)
                elif astr==estr:
                    print("It's a draw!")
                    orcact(estats)
                elif astr<=estr:
                    print("You miss!")
                    orcact(estats)
        elif b==3:
            astr=dice['8r']*stats['accuracy']
            estr=dice['8r']*estats['speed']
            if astr>estr:
                dmg=dice['8r']+stats['accuracy']/10
                print('You did %f damage!'%dmg)
                estats['health']-=dmg
                if estats['health']<=0:
                    print('You killed it!')
                    estats['c']=0
                    travelchoice()
                    ###------------------------------------------------
                else:
                    orcact(estats)
            elif astr==estr:
                print("It's a draw!")
                orcact(estats)
            elif astr<=estr:
                print("You miss!")
                orcact(estats)
            else:
                print('CODE ERROR!')
                orcact(estats)
    elif a==2:
        crun=dice['20r']
        if crun>=16:
            print('You escaped!')
            travelchoice()
        else:
            print('The enemy catches you!')
            estats['c']=1
            orcact(estats)
    elif a==3:
        print('While defending, you gain life!')
        estats['c']=1
        stats['health']+=random.randint(1,10)
        orcact(estats)
    elif a==4:
        orcact(estats)

        
def goblin(estats):
    print('----------------------------------------\n\n')
    if estats['health']<=0:
        print('You killed it!')
        estats['c']=0
        treasure()
        travelchoice()
 
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if estats['c']==0:
        nume=1
        print('You have met %i goblins!'%nume)
        
        estats={'health':10,'strength':5,'magic':5,'stamina':3,'accuracy':12,'speed':random.randint(6,18),'c':1}
    print('Your health=%r          Enemy health=%r'%(stats['health'],estats['health']))
    a=act()#get action
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if a==1:
        dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
        b=atype()
        if b==1:#melee
            astr=dice['8r']*stats['strength']
            estr=dice['8r']*estats['strength']
            if astr>estr:
                dmg=dice['8r']+stats['strength']/10
                print('You did %f damage!'%dmg)
                estats['health']-=dmg
                gobact(estats)
                if estats['health']<=0:
                    print('You killed it!')
                    estats['c']=0
                    treasure()
                    travelchoice()
                    ###------------------------------------------------
                else:
                    gobact(estats)
            elif astr==estr:
                print("It's a draw!")
                gobact(estats)
            elif astr<=estr:
                print("You miss!")
                gobact(estats)
        elif b==2:#magic
            dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
            astr=dice['8r']*stats['magic']
            estr=dice['8r']*estats['magic']
            if astr>estr:
                dmg=dice['8r']+stats['magic']/10
                print('You did %f damage!'%dmg)
                estats['health']-=dmg
                if estats['health']<=0:
                    print('You killed it!')
                    estats['c']=0
                    travelchoice()
                    ###------------------------------------------------
                else:
                    gobact(estats)
            elif astr==estr:
                print("It's a draw!")
                gobact(estats)
            elif astr<=estr:
                print("You miss!")
                gobact(estats)
        elif b==3:#shoot
            dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
            astr=dice['8r']*stats['accuracy']
            estr=dice['8r']*estats['speed']
            if astr>estr:
                dmg=dice['8r']+stats['accuracy']/10
                print('You did %f damage!'%dmg)
                estats['health']-=dmg
                if estats['health']<=0:
                    print('You killed it!')
                    estats['c']=0
                    travelchoice()
                    ###------------------------------------------------
                else:
                    gobact(estats)
            elif astr==estr:
                print("It's a draw!")
                gobact(estats)
            elif astr<=estr:
                print("You miss!")
                gobact(estats)
        else:
            print('CODE ERROR!')
            (estats)
    elif a==2:
        dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
        crun=dice['20r']
        if crun>=16:
            print('You escaped!')
            travelchoice()
        else:
            print('The enemy catches you!')
            estats['c']=1
            gobact(estats)
    elif a==3:
        dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
        print('While defending, you gain life!')
        estats['c']=1
        stats['health']+=random.randint(1,10)
        gobact(estats)
    elif a==4:
        dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
        gobact(estats)
        
        
def act():
    print('----------------------------------------\n\n')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    print('''
Attack
Run
Defend
''')
    a=input('What do you want to do?').lower()
    if a=='attack':
        return 1
    elif a=='run':
        return 2
    elif a=='defend':
        return 3
    else:
        print('Invalid entry')
        return 4
        act()
def gobact(estats):#enemy action
    print('----------------------------------------\n\n')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if estats['health']<3:
        if dice['20r']>=18:
            print('They escaped!')
    m=estats['magic']*dice['8r']
    a=estats['strength']*dice['8r']
    s=estats['accuracy']*dice['8r']
    if m>=a and m>=s:#magic
        print('Enemy casts a spell!')
        estr=dice['8r']*stats['magic']
        astr=dice['8r']*estats['magic']
        if astr>estr:
            dmg=dice['8r']+estats['magic']/10
            print('They did %f damage!'%dmg)
            stats['health']-=dmg
            if stats['health']<=0:
                print('You died!')
                time.sleep(3)
                quit()
                ###------------------------------------------------
            else:
                goblin(estats)
        elif astr==estr:
            print("It's a draw!")
            goblin(estats)
        elif astr<=estr:
            print("They miss!")
            goblin(estats)
    elif a>=m and a>=s:#melee
        estr=dice['8r']*stats['strength']
        astr=dice['8r']*estats['strength']
        if astr>estr:
            dmg=dice['8r']+estats['strength']/10
            print('They did %f damage!'%dmg)
            stats['health']-=dmg
            if stats['health']<=0:
                print('They killed you!')
                estats['c']=0
                time.sleep(5)
                quit()
                ###------------------------------------------------
            else:
                goblin(estats)
        elif astr==estr:
            print("It's a draw!")
            goblin(estats)
        elif astr<=estr:
            print("They miss!")
            goblin(estats)
    elif s>=a and s>=m:#shoot
        estr=dice['8r']*stats['accuracy']
        astr=dice['8r']*estats['speed']
        if astr>estr:
            dmg=dice['8r']+estats['accuracy']/10
            print('They did %f damage!'%dmg)
            stats['health']-=dmg
            if stats['health']<=0:
                print('They killed you!')
                time.sleep(5)
                quit()
                ###------------------------------------------------
            else:
                goblin(estats)
        elif astr==estr:
            print("It's a draw!")
            goblin(estats)
        elif astr<=estr:
            print("They miss!")
            goblin(estats)
    else:
        estr=dice['8r']*stats['accuracy']
        astr=dice['8r']*estats['speed']
        if astr>estr:
            dmg=dice['8r']+estats['accuracy']/10
            print('They did %f damage!'%dmg)
            stats['health']-=dmg
            if stats['health']<=0:
                print('They killed you!')
                time.sleep(5)
                quit()
                ###------------------------------------------------
            else:
                goblin(estats)
        elif astr==estr:
            print("It's a draw!")
            goblin(estats)
        elif astr<=estr:
            print("They miss!")
            goblin(estats)
def orcact(estats):#enemy action
    print('----------------------------------------\n\n')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if estats['health']<3:
        if dice['20r']>=18:
            print('They escaped!')
    m=estats['magic']*dice['8r']
    a=estats['strength']*dice['8r']
    s=estats['accuracy']*dice['8r']
    if m>=a and m>=s:#magic
        print('Enemy casts a spell!')
        estr=dice['8r']*stats['magic']
        astr=dice['8r']*estats['magic']
        if astr>estr:
            dmg=dice['8r']+estats['magic']/10
            print('You did %f damage!'%dmg)
            stats['health']-=dmg
            if stats['health']<=0:
                print('You died!')
                time.sleep(3)
                quit()
                ###------------------------------------------------
            else:
                orc(estats)
        elif astr==estr:
            print("It's a draw!")
            goblin(estats)
        elif astr<=estr:
            print("They miss!")
            orc(estats)
    elif a>=m and a>=s:#melee
        estr=dice['8r']*stats['strength']
        astr=dice['8r']*estats['strength']
        if astr>estr:
            dmg=dice['8r']+estats['strength']/10
            print('They did %f damage!'%dmg)
            stats['health']-=dmg
            if stats['health']<=0:
                print('They killed you!')
                estats['c']=0
                time.sleep(5)
                quit()
                ###------------------------------------------------
            else:
                goblin(estats)
        elif astr==estr:
            print("It's a draw!")
            orc(estats)
        elif astr<=estr:
            print("They miss!")
            orc(estats)
    elif s>=a and s>=m:#shoot
        estr=dice['8r']*stats['accuracy']
        astr=dice['8r']*estats['speed']
        if astr>estr:
            dmg=dice['8r']+estats['accuracy']/10
            print('You did %f damage!'%dmg)
            stats['health']-=dmg
            if stats['health']<=0:
                print('They killed you!')
                time.sleep(5)
                quit()
                ###------------------------------------------------
            else:
                orc(estats)
        elif astr==estr:
            print("It's a draw!")
            orc(estats)
        elif astr<=estr:
            print("They miss!")
            orc(estats)
    else:
        estr=dice['8r']*stats['strength']
        astr=dice['8r']*estats['strength']
        if astr>estr:
            dmg=dice['8r']+estats['strength']/10
            print('They did %f damage!'%dmg)
            stats['health']-=dmg
            if stats['health']<=0:
                print('They killed you!')
                estats['c']=0
                time.sleep(5)
                quit()
                ###------------------------------------------------
            else:
                goblin(estats)
        elif astr==estr:
            print("It's a draw!")
            orc(estats)
        elif astr<=estr:
            print("They miss!")
            orc(estats)
def atype():
    print('----------------------------------------\n\n')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    print('''
Melee
Magic
Shoot
''')
    a=input('What do you want to do?').lower()
    if a=='melee':
        print('You swing!')
        return 1
    elif a=='magic':
        print('You cast a spell!')
        return 2
    elif a=='shoot':
        print('You take aim and fire!')
        return 3
    else:
        print('Invalid entry')
        act()


maingreeting()
