##HCD Final Fantasy test v .40 last update 4/24/18
#changing everything to classes to make much easier to keep track of entities, and possibly add more characters
#Added melee,archery weapons and their bonuses
#still some old things carried over in globals, clean up under way with audio errors too


##Multi character, mapped, simple AI, single weapon, 4 race, single ability
#tested with two enemy types (goblin/orc), attack, defend, run all work, melee, magic, defend all work
#going to add more enemies, more full location list, better user interaction
#mapgen created, gives map, and a separate file with sorted locations to make easier to test, hit 50 or -50 boots you to 0,0
#created inventory, will add items as needed, deciding on weight calc
#Added audio, mp3s. One plays at start. Other plays during attacks. Volume set to 70%
#audio does not reboot on attacks now, just keeps playing



import math, sys, random, time, cmd, textwrap, string,os, mp3play
sw=80
pname=""#primary name
sname=""#secondary name
tname=""#third name
race2=''
race3=''
#stats={'health':0,'strength':0,'magic':0,'stamina':0,'accuracy':0,'speed':0} #stats dictionary starts at 0
estats={'health':1,'strength':0,'magic':0,'stamina':0,'accuracy':0,'speed':0,'c':0} #estats dictionary starts at 0
gold=1000 #starting global gold
loc={'x':0,'y':0}#location by dictionary
#lvl=1#difficulty level, will be increased over time

#dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}#first roll of dice, rolled at the beginning of all functions to see if needed
inv=[]#inventory starts empty
clip=mp3play.load(r'ffmain.mp3')
clip2=mp3play.load(r'Retribution.mp3')
firstplay=0

class Enemy:
    def __init__(self,health,strength, magic,accuracy,speed,lvl):
        self.health=health
        self.strength=strength
        self.magic=magic
        self.accuracy=accuracy
        self.speed=speed
        self.lvl=lvl
    def life(self):
        return(self.health)


class Player:
    def __init__(self,strength,magic_att,stamina,accuracy,speed,health,race,exp,lvl):
        self.health=health
        self.strength=strength
        self.magic=magic_att
        self.stamina=stamina
        self.accuracy=accuracy
        self.speed=speed
        self.race=race
        self.exp=exp
        self.lvl=lvl
    def saveit(self):
        return (self.health,self.strength,self.magic,self.stamina,self.accuracy,self.speed,self.race,self.exp,self.lvl)
    def return_stats(self):
        return ('''Strength: %s
Magic: %s
Stamina: %s
Accuracy: %s
Speed: %s
Health: %s'''%(self.strength,self.magic,self.stamina,self.accuracy,self.speed,self.health))

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
    global pname
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
        #race='h'
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
        #race='h'
        human()
    elif r_choice=='2':
        print("""Young girl: I've never met an Elf before, you look strange... yet kind of beautiful. I hope you won't hurt us

              """)
        time.sleep(1)
        #race='e'
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
        #race='t'
        troll()
    elif r_choice=='4':
        resp=("""Young girl: Explains why you are so short.
You look silly, I'm going to go tell my friends I saw a silly creature!

""")
        
        for line in textwrap.wrap(resp,sw):
            print(line)
        time.sleep(1)
        #race='d'
        dwarf()
    else:
        racechoice()
    travelchoice()
def human():#human race chosen, create player object with correct stats
    global player_one
    print('Human')
    #stats['strength']=random.randint(3,18)
    player_one=Player(random.randint(3,18),random.randint(3,18),random.randint(3,18),random.randint(3,18),random.randint(3,18),100,'human',0,1)

    print('Your character has the following stats:')
    print(player_one.return_stats())
    print('----------------------------------------')
    time.sleep(3)
def elf():#elf race chosen, create player object with correct stats
    global player_one
    print('Elf')
    player_one = Player(random.randint(3, 15), random.randint(5, 18), random.randint(3, 18),
                        random.randint(8, 18), random.randint(9, 18), 110, 'elf',0,1)




    print('Your character has the following stats:')#show stats
    print(player_one.return_stats())
    print('----------------------------------------')
    time.sleep(3)
    
def troll():#troll race chosen, create player object with correct stats
    global player_one
    player_one = Player(random.randint(9, 18), random.randint(1, 15), random.randint(9, 18),
                        random.randint(1, 14), random.randint(1, 10), 125, 'troll',0,1)
    print('Troll')

    print('Your character has the following stats:')
    print(player_one.return_stats())
    print('----------------------------------------')
    time.sleep(3)
    
def dwarf():#dwarf race chosen, create player object with correct stats
    global player_one
    print('Dwarf')
    player_one = Player(random.randint(4, 18), random.randint(1, 16), random.randint(9, 18),
                        random.randint(1, 18), random.randint(1, 18), 100, 'dwarf',0,1)

    print('Your character has the following stats:')
    print(player_one.return_stats())
    print('----------------------------------------')
    time.sleep(3)

def orc():
    return(Enemy(20,5, 3,5,2,3))

def goblin():
    return (Enemy(10, 2, 4, 7, 7, 1))

def delf():
    return(Enemy(10,2,7,7,7,2))

def levelcheck():

    nlvl=0
    try:
        check=open('level.txt','r')
        for line in check:
            n=line.split()
            if player_one.exp>=int(n[0]):
                nlvl=int(n[1])
        if nlvl>player_one.lvl:
            print('LEVEL UP!')
            player_one.lvl=nlvl
            levelup()
        check.close()
    except FileNotFoundError:
        print('LEVEL ERROR')

def levelup():
    global stats

    print('''
You have gained one point to use to increase your stats! Choose carefully...
''')
    print(player_one.return_stats())
    c=input('What stat do you want to increase? ').lower()
    #must be a better way, not sure yet
    if c=='strength':
        player_one.strength+=1
    elif c=='magic':
        player_one.magic+=1
    elif c=='accuracy':
        player_one.accuracy+=1
    elif c=='stamina':
        player_one.stamina+=1
    elif c=='speed':
        player_one.speed+=1
    elif c=='health':
        player_one.health+=10
    else:
        print('THAT IS NOT A CHOICE!')
        levelup()

def travelchoice():
    #this is to choose direction, and speed. gives location first, also shows health and gold
    levelcheck()
    global firstplay
    global player_one
    firstplay=0
    if clip.isplaying()==False:
        clip2.stop()
        clip.play()#check if playing, if not then play file
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('----------------------------------------')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    global loc,pname,race,exp,lvl
    print('''%s
Health:  %s    Gold: %i    Experience: %i    Level: %i'''%(pname,player_one.health,gold,player_one.exp,player_one.lvl))
    print('%s, your current location is %r'%(pname,loc))
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
            if player_one.race=='Elf':
                print('SUPERSPEED!')
                s=4
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
        print('Location file not found')
        time.sleep(3)
        quit()

        
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
        time.sleep(1)
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
        goblin_a(None)
    elif e<=8:
        orc_a(None)
    #elif e==9:
    #    delf_a()
    else:
        trap()
    
    travelchoice()


def heal():
    global player_one
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if 'Health Potion' in inv:
        player_one.health+=dice['20r']
        inv.remove('Health Potion')
    else:
        print('NO HEALTH POTIONS!')
        travelchoice()
    print('You healed! Your new health is %i'%player_one.health)
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
        time.sleep(2)
        travelchoice()

    
def randevent():#random event, most likely nothing, then enemy, then treasure
    num=random.randint(1,10)
    if num<=6:
        print('An uneventful day ends')
        print('----------------------------------------\n\n')
    elif num<=9:
        enemy()
    elif num==10:
        treasure()
    time.sleep(1)
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
        player_one.health-=dmg
        travelchoice()
    else:
        print('You found a trap, but were able to avoid it.')
        travelchoice()
          
def orc_a(e):
    if e==None:
        o=orc()
    else:
        o=e
    clip.stop()
    global firstplay
    if firstplay==0:
        clip2.play()
        firstplay+=1
    if o.health<=0:
        print('You killed it!')
        if enemy.lvl >= 3:
            print('You gained experience! ')
            player_one.exp += random.randint(1, 10)
        else:
            print('You gained experience! ')
            player_one.exp += random.randint(1, 5)
        treasure()
        travelchoice()
    print('----------------------------------------\n\n')
    
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    print('You have met orcs!')
    print('Your health=%f          Enemy health=%f'%(player_one.health,o.health))
    act(o)

        
def goblin_a(e):
    if e==None:
        g=goblin()
    else:
        g=e
    clip.stop()
    global firstplay
    if firstplay==0:
        clip2.play()
        firstplay+=1

    print('----------------------------------------\n\n')
    if g.health<=0:
        print('You killed it!')
        if enemy.lvl >= 3:
            print('You gained experience! ')
            player_one.exp += random.randint(1, 10)
        else:
            print('You gained experience! ')
            player_one.exp += random.randint(1, 5)
        treasure()
        travelchoice()
 
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    print('You have met goblins!')
        
    print('Your health=%f          Enemy health=%f'%(player_one.health,g.health))
    act(g)
        
def act(enemy):#generic action
    
    print('----------------------------------------\n\n')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    print('''
Attack
Run
Defend
''')
    a=input('What do you want to do? ').lower()
    
    if a=='attack':
        a=1
    elif a=='run':
        a=2
    elif a=='defend':
        a='h'
    else:
        print('Invalid entry')
        act(enemy)#get action
          
    if a==1:
        b=atype()
        time.sleep(1)
        if b==1:
            melee(enemy)
        elif b==2:
            magic(enemy)
        elif b==3:
            shoot(enemy)
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
            eact(enemy)
    elif a=='h':
        print('While defending, you gain life!')
        time.sleep(1)
        player_one.health+=dice['20r']
        if dice['20r']>(enemy.speed):
            if enemy.lvl>=3:
                print('You stopped them!')
                orc_a(enemy)
            elif enemy.lvl>=0:
                print('You stopped them!')
                goblin_a(enemy)
            else:
                print('code error')
                act(enemy)
        eact(enemy)
    else:
        act(enemy)
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
def melee(enemy):
    global exp,inv
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    astr=dice['8r']*player_one.strength
    estr=dice['10r']*enemy.strength
    print(astr,' ',estr)
    astr=mweaponcheck(astr,inv)
    print('With weapon: ',astr)
    if astr>estr:
        dmg=astr/10
        print('You did %f damage!'%dmg)
        enemy.health-=dmg
        if enemy.health<=0:
            print('You killed it!')

            time.sleep(1)

            if enemy.lvl>=2:
                print('You gained experience! ')
                player_one.exp+=random.randint(1,10)
            else:
                print('You gained experience! ')
                player_one.exp+=random.randint(1,5)
            clip2.stop()
            clip.play()
            treasure()
            travelchoice()
            ###------------------------------------------------
        else:
            eact(enemy) #enemy action passing stats and enemy type
    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        eact(enemy)
    elif astr<=estr:
        print("You miss!")
        time.sleep(1)
        eact(enemy)
def magic(enemy):
    global exp,inv
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    astr=dice['8r']*player_one.magic

    estr=dice['8r']*enemy.magic
    if astr>estr:
        dmg=dice['8r']+player_one.magic/10
        print('You did %f damage!'%dmg)
        time.sleep(1)
        enemy.health-=dmg
        if enemy.health<=0:
            print('You killed it!')

            if enemy.lvl>=3:
                print('You gained experience! ')
                player_one.exp+=random.randint(1,10)
            else:
                print('You gained experience! ')
                player_one.exp+=random.randint(1,5)
            time.sleep(1)
            player_one.exp+=random.randint(1,10)
            treasure()
            clip2.stop()
            clip.play()

            travelchoice()
            ###------------------------------------------------
        else:
            eact(enemy)
    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        eact(enemy)
    elif astr<=estr:
        print("You miss!")
        time.sleep(1)
        eact(enemy)
def shoot(enemy):
    global exp,inv
    dice = {'8r': random.randint(1, 8), '10r': random.randint(1, 10), '20r': random.randint(1, 20)}
    astr=dice['8r']*player_one.accuracy
    estr=dice['8r']*enemy.speed
    astr=sweaponcheck(astr,inv)
    print('new ',astr)
    if astr>estr:
        dmg=dice['8r']+player_one.accuracy/10
        print('You did %f damage!'%dmg)
        time.sleep(1)
        enemy.health-=dmg
        if enemy.health<=0:
            print('You killed it!')


            if enemy.lvl>=3:
                print('You gained experience! ')
                player_one.exp+=random.randint(1,10)
            else:
                print('You gained experience! ')
                player_one.exp+=random.randint(1,5)
            time.sleep(1)
            clip2.stop()
            clip.play()
            treasure()
            travelchoice()
            ###------------------------------------------------
        else:
            eact(enemy)
    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        eact(enemy)
    elif astr<=estr:
        print("You miss!")
        time.sleep(1)
        eact(enemy)
    else:
        print('CODE ERROR!')
        act(enemy)

def edecision(m,a,s,enemy):
    if a>=s:
        emelee(enemy)
    elif s>=m:
        eshoot(enemy)
    elif m>=a:
        emagic(enemy)
    elif a==s==m:
        emelee(enemy)
def emelee(enemy):
    dice = {'8r': random.randint(1, 8), '10r': random.randint(1, 10), '20r': random.randint(1, 20)}
    print('The enemy takes a swing!')
    time.sleep(.5)
    estr=dice['8r']*enemy.strength
    astr=dice['8r']*player_one.strength
    print(estr, astr)
    if astr>estr:
        dmg=dice['8r']+enemy.strength/10
        print('They did %f damage!'%dmg)
        time.sleep(1)
        player_one.health-=dmg
        if player_one.health<=0:
                print('They killed you!')
                time.sleep(5)
                quit()

        else:
                if enemy.lvl>=3:
                        orc_a(enemy)
                elif enemy.lvl>=0:
                        goblin_a(enemy)
                else:
                        print('code error')
                        eact(enemy)
    elif astr==estr:
        if enemy.lvl >= 3:
            orc_a(enemy)
        elif enemy.lvl >= 0:
            goblin_a(enemy)
        else:
            print('code error')
            eact(enemy)
    elif astr<=estr:
        print("They miss!")
        time.sleep(1)
        if enemy.lvl >= 3:
            orc_a(enemy)
        elif enemy.lvl >= 0:
            goblin_a(enemy)
        else:
            print('code error')
            eact(enemy)
def eshoot(enemy):
    dice = {'8r': random.randint(1, 8), '10r': random.randint(1, 10), '20r': random.randint(1, 20)}
    print('The enemy shoots at you!')
    time.sleep(.5)        
    astr=dice['8r']*player_one.accuracy
    estr=dice['8r']*enemy.accuracy
    print(estr, astr)
    if astr>estr:
        dmg=dice['8r']+enemy.accuracy/10
        print('They did %f damage!'%dmg)
        time.sleep(1)
        player_one.health-=dmg
        if player_one.health<=0:
                print('They killed you!')
                time.sleep(5)
                quit()
        else:
                if enemy.lvl>=3:
                        orc_a(enemy)
                elif enemy.lvl>=0:
                        goblin_a(enemy)
                else:
                        print('code error')
                        eact(enemy)

    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        if enemy.lvl >= 3:
            orc_a(enemy)
        elif enemy.lvl >= 0:
            goblin_a(enemy)
        else:
            print('code error')
            eact(enemy)


    elif astr<=estr:
        print("They miss!")
        time.sleep(1)
        if enemy.lvl >= 3:
            orc_a(enemy)
        elif enemy.lvl >= 0:
            goblin_a(enemy)
        else:
            print('code error')
            eact(enemy)
def emagic(estats,etype):
    dice = {'8r': random.randint(1, 8), '10r': random.randint(1, 10), '20r': random.randint(1, 20)}

    print('Enemy casts a spell!')
    time.sleep(.5)
    estr=dice['8r']*enemy.magic
    astr=dice['8r']*player_one.magic
    print(estr, astr)
    if estr>astr:
        dmg=dice['8r']+enemy.magic/10
        print('They did %f damage!'%dmg)
        time.sleep(1)
        player_one.health-=dmg
        if player_one.health<=0:
                print('You died!')
                time.sleep(3)
                quit()
                ###------------------------------------------------
        else:
                if enemy.lvl>=3:
                        orc_a(enemy)
                elif enemy.lvl>=0:
                        goblin_a(enemy)
                else:
                        print('code error')
                        eact(enemy)

    elif astr==estr:
        print("It's a draw!")
        time.sleep(1)
        if enemy.lvl >= 3:
            orc_a(enemy)
        elif enemy.lvl >= 0:
            goblin_a(enemy)
        else:
            print('code error')
            eact(enemy)

    elif astr<=estr:
        print("They miss!")
        time.sleep(1)
        if enemy.lvl >= 3:
            orc_a(enemy)
        elif enemy.lvl >= 0:
            goblin_a(enemy)
        else:
            print('code error')
            eact(enemy)
                    
def eact(enemy):#enemy action
    print('----------------------------------------\n\n')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    if enemy.health<3:
        if dice['20r']>=18:
            print('They escaped!')
            clip2.stop()
            clip.play()
            travelchoice()
            
        else:
            print("Enemy tried to run, but they didn't make it")
            time.sleep(.5)
    m=enemy.magic*dice['8r']
    a=enemy.strength*dice['8r']
    s=enemy.accuracy*dice['8r']
    edecision(m,a,s,enemy)
    

def atype():
    print('----------------------------------------\n\n')
    dice={'8r':random.randint(1,8),'10r':random.randint(1,10),'20r':random.randint(1,20)}
    print('''
Melee
Magic
Shoot
''')
    a=input('What do you want to do? ').lower()
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
    for x in player_one.saveit():
        svfile.write(str(x)+'\n')
    #svfile.write(str(stats)+'\n')
    svfile.write(str(gold)+'\n')
    svfile.write(str(loc)+'\n')
    svfile.write(str(inv)+'\n')


    print('Saving.')
    time.sleep(.5)
    print('Saving..')
    time.sleep(.5)
    print('Saving...')
    time.sleep(.5)
    svfile.close()
    travelchoice()

def load():#load last saved info
    global gold, stats, loc,pname,inv,lvl,exp,player_one
    try:
        svfile=open('paradisiosave.txt','r')#check for check file in current directory
    except FileNotFoundError:
        svfile=open('paradisiosave'+'.txt','r')
    except:
        print('UH OH!')#check android download folder

    withn=svfile.readlines()
    all=[]
    for x in withn:
        x=x.strip('\n')
        all.append(x)
    pname=all[0]
    player_one=Player(int(all[1]),int(all[2]),int(all[3]),int(all[4]),int(all[5]),int(all[6]),all[7],int(all[8]),int(all[9]))
    gold=int(all[10])
    loc=eval(all[11])
    inv=eval(all[12])
    svfile.close()
    print('Player name: ',pname)
    print(player_one.return_stats())
    print('Gold: ',gold)
    print('Location: ',loc)
    print('Inventory: ',inv)
    print('Level: ',player_one.lvl)
    print('Experience: ',player_one.exp)
    travelchoice()
maingreeting()
