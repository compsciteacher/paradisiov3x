##HCD Final Fantasy test v .3 last update 2/12/16
#Added melee,archery weapons and their bonuses

##Multi character, mapped, simple AI, single weapon, 4 race, single ability
#tested with two enemy types (goblin/orc), attack, defend, run all work, melee, magic, defend all work
#going to add more enemies, more full location list, better user interaction
#mapgen created, gives map, and a separate file with sorted locations to make easier to test, hit 50 or -50 boots you to 0,0
#try created to check for file in two places before kicking an error
#created inventory, will add items as needed, deciding on weight calc
#Added audio, mp3s. One plays at start. Other plays during attacks. Volume set to 70%
#audio does not reboot on attacks now, just keeps playing



import math, sys, random, time, cmd, textwrap, string,os, mp3play
sw=80
pname=""#primary name
sname=""#secondary name
tname=""#third name
race=""
race2=''
race3=''
stats={'health':0,'strength':0,'magic':0,'stamina':0,'accuracy':0,'speed':0} #stats dictionary starts at 0
estats={'health':1,'strength':0,'magic':0,'stamina':0,'accuracy':0,'speed':0,'c':0} #estats dictionary starts at 0
gold=1000 #starting global gold
loc={'x':0,'y':0}#location by dictionary
lvl=1#difficulty level, will be increased over time
exp=0
dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}#first roll of dice, rolled at the beginning of all functions to see if needed
inv=[]#inventory starts empty
clip=mp3play.load(r'ffmain.mp3')
clip2=mp3play.load(r'Retribution.mp3')
firstplay=0

    
def maingreeting():
    
    clip.volume(7)
    clip2.volume(7)
    clip.play()#only on game open
    
    #main audio file, plays until fight. Starts again at end of fight.
    print('''
---------------------------------
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

def newg():
    
    #start new game, player name and race globalized
    global pname, race
    welcome=('''

You have awoken in a land that is new to you, feeling as though you have been
forgotten, as you have forgotten all of your life. You are clothed in simple
rags, hungry, and without defense. You are greeted by a child from a nearby village
who found you on the roadside.

''')
    for line in textwrap.wrap(welcome,sw):
        print (line)
    time.sleep(2)
    pname=input('Young girl: What is your name traveler? ')
    pname=pname.strip("'")
    human_choice=input('Greetings %s, you look different than the rest of us? Are you even human? (y/n)'%pname) #change pname and greet
    if human_choice=='y': #if human change race and call human function
        time.sleep(1)
        print('Young girl: Oh, it must have just been how dirty you were. Good luck on your travels.')
        race='h'
        time.sleep(1)
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
        time.sleep(1)
        race='h'
        human()
    elif r_choice=='2':
        print("""Young girl: I've never met an Elf before, you look strange... yet kind of beautiful. I hope you won't hurt us

              """)
        time.sleep(1)
        race='e'
        elf()
    elif r_choice=='3':
        print("Young girl: AHHHH!!!")
        time.sleep(1)
        resp=('''The young girl runs away. She seems frightened by your appearance.
It may be difficult to make friends here,
this land is not used to evil creatures like you. At least they won't bug you either.

''')
        time.sleep(1)
        for line in textwrap.wrap(resp,sw):
            print(line)
        race='t'
        troll()
    elif r_choice=='4':
        resp=("""Young girl: Explains why you are so short.
You look silly, I'm going to go tell my friends I saw a silly creature!

""")
        
        for line in textwrap.wrap(resp,sw):
            print(line)
        time.sleep(1)
        race='d'
        dwarf()
    else:
        racechoice()
    travelchoice()
def human():#human race chosen, update global stats dictionary with random rolls
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global stats#use global stats
    print('Human')
    stats['strength']=random.randint(3,18)
    if stats['strength']<8:#if strength less than 8, they at least get a 1 bonus
        stats['strength']+=1
    stats['magic']=random.randint(3,18)
    stats['stamina']=random.randint(3,18)#not sure what to use stamina for
    if stats['stamina']<8:
        stats['stamina']+=2#if stamina less than 8, auto add two to bring it up
    stats['accuracy']=random.randint(3,18)
    stats['speed']=random.randint(3,18)
    stats['health']=100
    print('Your character has the following stats:')
    
    for (s,v) in stats.items():#show full stats
            print(s.title(),": ",v)
    print('----------------------------------------')
    time.sleep(3)
def elf():#elf race chosen, update global stats dictionary with random rolls
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global stats
    print('Elf')
    stats['strength']=random.randint(3,18)
    stats['magic']=random.randint(3,18)
    if stats['magic']<8:
        stats['magic']+=1
    stats['stamina']=random.randint(3,18)

    stats['accuracy']=random.randint(3,18)
    if stats['accuracy']<8:#if they get less than an 8, auto add 3
        stats['accuracy']+=3
    stats['speed']=random.randint(9,18)#speed has an auto 9, crazy high
    stats['health']=110
    print('Your character has the following stats:')#show stats
    for (s,v) in stats.items():
            print(s.title(),": ",v)
    print('----------------------------------------')
    time.sleep(3)
    
def troll():#troll race chosen, update global stats dictionary with random rolls
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global stats
    print('Troll')
    stats['strength']=random.randint(9,18)#troll only one with predetermined ranges for their stats, no plusses. goes low and high
    stats['magic']=random.randint(1,15)#magic is very limited
    
    stats['stamina']=random.randint(9,18)

    stats['accuracy']=random.randint(1,14)
    stats['speed']=random.randint(1,10)
    stats['health']=125
    print('Your character has the following stats:')
    for (s,v) in stats.items():
            print(s.title(),": ",v)
    print('----------------------------------------')
    time.sleep(3)
    
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
    for (s,v) in stats.items():
            print(s.title(),": ",v)
    print('----------------------------------------')
    time.sleep(3)
def levelcheck():
    global exp,lvl
    nlvl=0
    try:
        check=open('level.txt','r')
        for line in check:
            n=line.split()
            if exp>=int(n[0]):
                nlvl=int(n[1])
        if nlvl>lvl:
            print('LEVEL UP!')
            lvl=nlvl
            levelup()
        check.close()
    except:
        print('LEVEL ERROR')
def levelup():
    global stats
    points=1
    print('''
You have gained one point to use to increase your stats! Choose carefully...
''')
    for (x,y) in stats.items():
        print(x.title(),': ',y)
    c=input('What stat do you want to increase? ').lower()
    if c in stats.keys():
        stats[c]+=1
        print('You have increased ',c.title(),' one point')
    else:
        print('THAT IS NOT A CHOICE!')
        levelup()

def travelchoice():
    #this is to choose direction, and speed. gives location first, also shows health and gold
    levelcheck()
    global firstplay
    firstplay=0
    if clip.isplaying()==True:
        clip.play()#check if playing, if not then play file
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('----------------------------------------')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global loc,pname,race,exp,lvl
    print('''%s
Health:  %s    Gold: %i    Experience: %i    Level: %i'''%(pname.strip("'"),stats['health'],gold,exp,lvl))
    print('%s, your current location is %r'%(pname.strip("'"),loc))
    print('''

Actions:
N: Move North
E: Move East
S: Move South
W: Move West
I: Get Inventory
H: Use Heal Potion
Save: Save file
Quit: Quit game
''')
    
    d=input('What action would you like to take?: ').lower()
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
    elif d=='save':
        save()
    elif d=='cheat':
        x=int(input('Which x?'))
        y=int(input('Which y?'))
        loc['x']=x
        loc['y']=y
        print(loc)
        locchk()
    elif d=='quit':
        yn=input('Are you sure (y/n)? ')
        if yn=='y':
            quit()
        else:
            travelchoice()
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
            s=1
        elif s==2:
            s=2
        elif s==3:
            s=3
        elif s==4:#only available for elves
            if race=='e':
                print('SUPERSPEED!')
            else:
                print("You can't go that fast!")
                s=3
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
    
def locchk():
    global loc
    for val in loc.values():#check edge of map
        if val>=50:
            print('''You have reached the edge of the island!
By some magic you are forced back
to the center of the island!''')
            loc={'x':0,'y':0}
            travelchoice()
        elif val<=-50:
            print('''You have reached the edge of the island!
By some magic you are forced back
to the center of the island!''')
            loc={'x':0,'y':0}
            travelchoice()
            #check loccheck.txt file for encounters, if nothing found then random result that can be nothing or anything else
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
#if current location not found in loccheck file, random event is pulled
    
    randevent()
    
    travelchoice()
    ref.close()
def event(etype):#if an event is found, a letter is passed that determines the event type
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if etype=='a':#a calls enemy, b is treasure, c is trap, d is merchant, e is random for now (will have friend and city
        print('You have encountered an enemy!')
        time.sleep(2)
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
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if 'Health Potion' in inv:
        stats['health']=stats['health']+dice['20r']
        inv.remove('Health Potion')
    else:
        print('NO HEALTH POTIONS!')
        travelchoice()
    print('You healed! Your new health is %i'%stats['health'])
    travelchoice()

    
    
def treasure():#gives treasure based on d20 roll, you can actually lose gold on a 1, on 19 or 20 you get nothing
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global gold
    chance=dice['20r']
    print("You rolled a "+ str(chance))
    if chance<19 and chance>=2:
        print('You found treasure!')
        tre=dice['20r']*chance
        print('You found %i gold!'%tre)
        gold+=tre
        travelchoice()
    elif chance<2:
        print('You unfortunately have lost some of your gold!')
        tre=dice['20r']*chance
        print('You lost %i gold!'%tre)
        gold-=tre
        travelchoice()
    else:
        print('You thought you saw something, but must have just been your imagination')
        time.sleep(4)
        travelchoice()

    
def randevent():#random event, most likely nothing, then enemy, then treasure
    num=random.randint(1,10)
    if num<=7:
        print('An uneventful day ends')
        print('----------------------------------------\n\n')
    elif num<=9:
        enemy()
    elif num==10:
        treasure()
    time.sleep(4)
    travelchoice()

    
def merchant():#find a sales person
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
    time.sleep(1)
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
                          gold-=int(info['cost'])
                          inv.append(info['name'])
                          store(level)
                      else:
                          print('NOT ENOUGH MONEY!')
                          store(level)
  
            line=ref.readline()

        print('Not found')
        store(level)
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
          
def orc(estats):
    clip.stop()
    global firstplay
    if firstplay==0:
        clip2.play()
        firstplay+=1
    
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
    print('Your health=%f          Enemy health=%f'%(stats['health'],estats['health']))
    act(estats,'orc1')

        
def goblin(estats):
    clip.stop()
    global firstplay
    if firstplay==0:
        clip2.play()
        firstplay+=1
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
    print('Your health=%f          Enemy health=%f'%(stats['health'],estats['health']))
    act(estats,'goblin1')
        
def act(estats,etype):#generic action
    
    print('----------------------------------------\n\n')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    print('''
Attack
Run
Defend
''')
    a=input('What do you want to do?').lower()
    
    if a=='attack':
        a=1
    elif a=='run':
        a=2
    elif a=='defend':
        a='h'
    else:
        print('Invalid entry')
        act(estats,etype)#get action
          
    if a==1:
        b=atype()
        time.sleep(1)
        if b==1:
            melee(estats,etype)
        elif b==2:
            magic(estats,etype)
        elif b==3:
            shoot(estats,etype)
    elif a==2:
        crun=dice['20r']
        if crun>=16:
            print('You escaped!')
            time.sleep(1)
            clip2.stop()
            clip.play()
            travelchoice()
        else:
            print('The enemy catches you!')
            time.sleep(1)
            estats['c']=1
            eact(estats,etype)
    elif a=='h':
        print('While defending, you gain life!')
        time.sleep(1)
        estats['c']=1
        stats['health']+=dice['20r']
        if dice['20r']>(estats['speed']):
            if etype=='orc1':
                print('You stopped them!')
                orc(estats)
            elif etype=='goblin1':
                print('You stopped them!')
                goblin(estats)
            else:
                print('code error')
                act(estats,etype)
        eact(estats,etype)
    else:
        act(estats,etype)
def mweaponcheck(a,i):
    if 'Sword4' in i:
        print('You use your Sword4!')
        a+=15
        return a
    elif 'Sword3' in i:
        print('You use your Sword3!')
        a+=10
        return a
    elif 'Sword2' in i:
        print('You use your Sword2!')
        a+=5
        return a
    else:
        print('You use your bare hands!')
        return a
def sweaponcheck(a,i):
    if 'Bow2' in i:
        print('You use your Bow2!')
        a+=5
        return a
    elif 'Bow3' in i:
        print('You use your Bow3!')
        a+=10
        return a
    elif 'Bow4' in i:
        print('You use your Bow4!')
        a+=15
        return a
    else:
        print('You use your sling shot!')
        return a
def melee(estats,etype):
    global exp,inv
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    astr=dice['8r']*stats['strength']
    estr=dice['8r']*estats['strength']
    print(astr,' ',estr)
    astr=mweaponcheck(astr,inv)
    print('With weapon: ',astr)
    if astr>estr:
        dmg=astr/10
        print('You did %f damage!'%dmg)
        estats['health']-=dmg
        if estats['health']<=0:
            print('You killed it!')
            treasure()
            time.sleep(1)
            estats['c']=0
            if etype=='orc1':
                exp+=random.randint(1,10)
            elif etype=='goblin1':
                exp+=random.randint(1,5)
            clip2.stop()
            clip.play()
            travelchoice()
            ###------------------------------------------------
        else:
            eact(estats,etype) #enemy action passing stats and enemy type
    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        eact(estats,etype)
    elif astr<=estr:
        print("You miss!")
        time.sleep(1)
        eact(estats,etype)
def magic(estats,etype):
    global exp,inv
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global exp
    astr=dice['8r']*stats['magic']
    estr=dice['8r']*estats['magic']
    if astr>estr:
        dmg=dice['8r']+stats['magic']/10
        print('You did %f damage!'%dmg)
        time.sleep(1)
        estats['health']-=dmg
        if estats['health']<=0:
            print('You killed it!')
            treasure()
            if etype=='orc1':
                exp+=random.randint(1,10)
            elif etype=='goblin1':
                exp+=random.randint(1,5)
            time.sleep(1)
            estats['c']=0
            exp+=random.randint(1,10)
            clip2.stop()
            clip.play()
            travelchoice()
            ###------------------------------------------------
        else:
            eact(estats,etype)
    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        eact(estats,etype)
    elif astr<=estr:
        print("You miss!")
        time.sleep(1)
        eact(estats,etype)
def shoot(estats,etype):
    global exp,inv
    astr=dice['8r']*stats['accuracy']
    estr=dice['8r']*estats['speed']
    astr=sweaponcheck(astr,inv)
    print('new ',astr)
    if astr>estr:
        dmg=dice['8r']+stats['accuracy']/10
        print('You did %f damage!'%dmg)
        time.sleep(1)
        estats['health']-=dmg
        if estats['health']<=0:
            print('You killed it!')
            treasure()
            if etype=='orc1':
                exp+=random.randint(1,10)
            elif etype=='goblin1':
                exp+=random.randint(1,5)
            time.sleep(1)
            estats['c']=0
            clip2.stop()
            clip.play()
            travelchoice()
            ###------------------------------------------------
        else:
            eact(estats,etype)
    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        eact(estats,etype)
    elif astr<=estr:
        print("You miss!")
        time.sleep(1)
        eact(estats,etype)
    else:
        print('CODE ERROR!')
        act(estats,etype)

def edecision(m,a,s,estats,etype):
    if a>=s:
        emelee(estats,etype)
    elif s>=m:
        eshoot(estats,etype)
    elif m>=a:
        emagic(estats,etype)
    elif a==s==m:
        if etype=='orc1':
            emelee(estats,etype)
        elif etype=='goblin1':
            eshoot(stats,etype)
def emelee(estats,etype):
    print('The enemy takes a swing!')
    time.sleep(.5)
    estr=dice['8r']*stats['strength']
    astr=dice['8r']*estats['strength']
    print(estr, astr)
    if astr>estr:
        dmg=dice['8r']+estats['strength']/10
        print('They did %f damage!'%dmg)
        time.sleep(1)
        stats['health']-=dmg
        if stats['health']<=0:
                print('They killed you!')
                estats['c']=0
                time.sleep(5)
                quit()
                ###------------------------------------------------
        else:
                if etype=='orc1':
                        orc(estats)
                elif etype=='goblin1':
                        goblin(estats)
                else:
                        print('code error')
                        eact(estats,etype)
    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        if etype=='orc1':
                orc(estats)
        elif etype=='goblin1':
                goblin(estats)
        else:
                print('code error')
                eact(estats,etype)
    elif astr<=estr:
        print("They miss!")
        time.sleep(1)
        if etype=='orc1':
                orc(estats)
        elif etype=='goblin1':
                goblin(estats)
        else:
                print('code error')
                eact(estats,etype)
def eshoot(estats,etype):
    print('The enemy shoots at you!')
    time.sleep(.5)        
    estr=dice['8r']*stats['accuracy']
    astr=dice['8r']*estats['speed']
    print(estr, astr)
    if astr>estr:
        dmg=dice['8r']+estats['accuracy']/10
        print('They did %f damage!'%dmg)
        time.sleep(1)
        stats['health']-=dmg
        if stats['health']<=0:
                print('They killed you!')
                time.sleep(5)
                quit()
                ###------------------------------------------------
        else:
                if etype=='orc1':
                        orc(estats)
                elif etype=='goblin1':
                        goblin(estats)
                else:
                        print('code error')
                        eact(estats,etype)

    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        if etype=='orc1':
                orc(estats)
        elif etype=='goblin1':
                goblin(estats)


    elif astr<=estr:
        print("They miss!")
        time.sleep(1)
        if etype=='orc1':
                orc(estats)
        elif etype=='goblin1':
                goblin(estats)
def emagic(estats,etype):
    print('Enemy casts a spell!')
    time.sleep(.5)
    estr=dice['8r']*stats['magic']
    astr=dice['8r']*estats['magic']
    print(estr, astr)
    if astr>estr:
        dmg=dice['8r']+estats['magic']/10
        print('They did %f damage!'%dmg)
        time.sleep(1)
        stats['health']-=dmg
        if stats['health']<=0:
                print('You died!')
                time.sleep(3)
                quit()
                ###------------------------------------------------
        else:
                if etype=='orc1':
                        orc(estats)
                elif etype=='goblin1':
                        goblin(estats)

    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        if etype=='orc1':
                orc(estats)
        elif etype=='goblin1':
                goblin(estats)

    elif astr<=estr:
        print("They miss!")
        time.sleep(1)
        if etype=='orc1':
                orc(estats)
        elif etype=='goblin1':
                goblin(estats)
                    
def eact(estats,etype):#enemy action
    print('----------------------------------------\n\n')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if estats['health']<3:
        if dice['20r']>=18:
            print('They escaped!')
            clip2.stop()
            clip.play()
            travelchoice()
            
        else:
            print("Enemy tried to run, but they didn't make it")
            time.sleep(.5)
    m=estats['magic']*dice['8r']
    a=estats['strength']*dice['8r']
    s=estats['accuracy']*dice['8r']
    edecision(m,a,s,estats,etype)
    

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
        atype()


def save():#save all important stats and info
    svfile=open('paradisiosave.txt','w')
    svfile.write(pname+'\n')
    svfile.write(str(stats)+'\n')
    svfile.write(str(gold)+'\n')
    svfile.write(str(loc)+'\n')
    svfile.write(str(inv)+'\n')
    svfile.write(str(lvl)+'\n')
    svfile.write(str(exp)+'\n')
    print('Saving.')
    time.sleep(.5)
    print('Saving..')
    time.sleep(.5)
    print('Saving...')
    time.sleep(.5)
    svfile.close()
    travelchoice()
def load():#load last saved info
    global gold, stats, loc,pname,inv,lvl,exp
    try:
        svfile=open('paradisiosave.txt','r')#check for check file in current directory
    except FileNotFoundError:
        svfile=open('paradisiosave'+'.txt','r')
    except:
        print('UH OH!')#check android download folder

    pname=svfile.readline().strip('\n')
    stats=eval(svfile.readline())
    for (x,y) in stats.items():
        print(int(y))
    gold=int(svfile.readline())
    loc=eval(svfile.readline())
    inv=eval(svfile.readline())
    lvl=int(svfile.readline())
    exp=int(svfile.readline())
    svfile.close()
    print('Player name: ',pname)
    print('Stats:')
    for (s,v) in stats.items():
        print(s.title(),": ",v)
    print('Gold: ',gold)
    print('Location: ',loc)
    print('Inventory: ',inv)
    print('Level: ',lvl)
    print('Experience: ',exp)
    travelchoice()
maingreeting()
