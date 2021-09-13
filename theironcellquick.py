#===IMPORTS===#
import time
from time import sleep
import keyboard
import sys


#===GLOBAL_VARIABLES===#
global textSpeed
textSpeed = 0

global currentRoom
currentRoom = 'cell'

global availableRooms
availableRooms = ['dungeon']


#=====FUNCTIONS=====#

#---rooms---#
def enterCell():
    write('> You walk into the small cell. Then you wonder why you walked in. There is nothing here.')
    global currentRoom
    global availableRooms
    currentRoom = 'cell'
    availableRooms = ['dungeon']

def enterDungeon():
    write('> You emerge into a dank dungeon. Sickly sweet smells emanate from the dark corners of the room.')
    write('> There is a small staircase bunched into the corner leading upwards.')
    global currentRoom
    global availableRooms
    currentRoom = 'dungeon'
    availableRooms = ['cell', 'storageRoom']

def enterStorageRoom():
    write('> The room is small and stuffy. It looks like some sort of Storage room.')
    write('>The only light source is a flickering bulb hanging from the ceiling by it\'s cord.')
    write('> A staircase winds downward to the dungeon and lone door leads elsewhere.')

    global currentRoom
    global availableRooms
    currentRoom = 'storageRoom'
    availableRooms = ['dungeon', 'entranceHall']

def enterEntranceHall():
    write('> You walk into a colossal entrance hall. The entrance to the manor has been boarded up.')
    write('> There are 3 doors leading to different rooms, and a staircase leading upward.')
    global currentRoom
    global availableRooms
    currentRoom = 'entranceHall'
    availableRooms = ['storageRoom', 'diningHall', 'livingRoom', 'secondFloor']

def enterLivingRoom():
    write('> You enter what appears to be a Living room. Chairs and tables lay thrown about the room.')
    write('> You can see two doors, one leading to the Dining room and another to the Entrance Hall.')
    global currentRoom
    global availableRooms
    currentRoom = 'livingRoom'
    availableRooms = ['diningHall', 'entranceHall']

def enterDiningHall():
    write('> You walk into a huge dining hall. It was obviously meant to host many dozens of guests, but it now lies empty.')
    write('> There is a door leading to a Kitchen, the Entrance Hall and the Living room.')
    global currentRoom
    global availableRooms
    currentRoom = 'diningHall'
    availableRooms = ['entranceHall', 'kitchen', 'livingRoom', 'secondFloor']

def enterKitchen():
    write('> A deathly smell seeps from the Kitchen. Rotten foods are strewn across the blood soaked floor. You feel sick.')
    global currentRoom
    global availableRooms
    currentRoom = 'kitchen'
    availableRooms = ['diningHall']

def enterSecondFloor():
    write('> The second floor is a balcony level above the entrance hall.')
    write('> The two sides are lined with servant quarters and the Library entrance sits along the front wall.')
    global currentRoom
    global availableRooms
    currentRoom = 'secondFloor'
    availableRooms = ['sq1', 'sq2', 'sq3', 'sq4', 'sq5', 'sq6', 'sq7', 'sq8', 'greatLibrary']

def entersq1():
    write('> This Servant Quarter is immaculate. Perfectly neat, not even a crease in the bed. The cabinet shows no traces of dust.')
    global currentRoom
    global availableRooms
    currentRoom = 'sq1'
    availableRooms = ['secondFloor']

def entersq2():
    write('> This Servant Quarter looks to have been quickly abandoned. The bedside cabinet was knocked over by someone in a hurry.')
    global currentRoom
    global availableRooms
    currentRoom = 'sq2'
    availableRooms = ['secondFloor']

def entersq3():
    write('> This Servant Quarter\'s bedsheet has been ripped in half and left on the floor.')
    global currentRoom
    global availableRooms
    currentRoom = 'sq3'
    availableRooms = ['secondFloor']

def entersq4():
    write('> This Servant Quarter has nothing out of the ordinary.')
    global currentRoom
    global availableRooms
    currentRoom = 'sq4'
    availableRooms = ['secondFloor']

def entersq5():
    write('> This Servant Quarter has an empty glass laying on the bare mattress.')
    global currentRoom
    global availableRooms
    currentRoom = 'sq5'
    availableRooms = ['secondFloor']

def entersq6():
    write('> This Servant Quarter has bloodstains on the roof.')
    global currentRoom
    global availableRooms
    currentRoom = 'sq6'
    availableRooms = ['secondFloor']

def entersq7():
    write('> This Servant Quarter is empty, save for the pools of blood and abandoned tools.')
    write('> It is more a cell than a Servant Quarter. You wonder what happened here. ')
    global currentRoom
    global availableRooms
    currentRoom = 'sq7'
    availableRooms = ['secondFloor']

def entersq8():
    write('> This Servant Quarter has a crack in the wall as if hit with a heavy tool.')
    global currentRoom
    global availableRooms
    currentRoom = 'sq8'
    availableRooms = ['secondFloor']

def enterLibrary():
    write('> You walk into the Great Library. It contains thousands of books, displayed on countless shelves that reach in to the roof.')
    global currentRoom
    global availableRooms
    currentRoom = 'greatLibrary'
    availableRooms = ['secondFloor']

def enterWaitingChamber():
    write('> The Waiting Chamber consists of a small desk with ink and a ledger.')
    write('> A chair rests in the centre of the room laying on it\'s side')
    write('> There are three wooden doors with the words, "Luther", "Hans" and "Klaus" engraved on to each respectively.')
    global currentRoom
    global availableRooms
    currentRoom = 'waitingChamber'
    availableRooms = ['scientist', 'officer', 'overseer', 'secondFloor']

def enterScientist():
    global currentRoom
    global availableRooms
    currentRoom = 'scientist'
    availableRooms = ['waitingChamber']
    write('> You walk into the room lableed "Luther"')
    write('> [REDACTED]')

def enterOfficer():
    global currentRoom
    global availableRooms
    currentRoom = 'officer'
    availableRooms = ['waitingChamber']
    write('> You walk into the room labelled "Hans"')
    write('> [REDACTED]')

def enterOverseer():
    global currentRoom
    global availableRooms
    currentRoom = 'overseer'
    availableRooms = ['waitingChamber']
    write('> You walk into the room labelled "Klaus"')
    write('> [REDACTED]')


#---commands---#
def error():
    write('> Type "help" for a list of commands.')

def help():
    #when the user types help this will display all the commands available
    write('> Type "look" to see a description of your surroundings.'), sleep(0.2)
    write('> Type "inspect" and then an object to obtain a description of it.'), sleep(0.2)
    write('> Type "use" followed by a door or stairs to walk through it, E.G. "use cell door, use dungeon stairs.".'), sleep(0.2)
    write('> Type "save" to save your progress. [WIP]'), sleep(0.2)
    write('> Type "load" to load your previous save. [WIP]'), sleep(0.2)
    write('> Type "quit" to exit the game.'), sleep(0.2)
    write('> type "help" to see these options again.')

def look():
    #defines what is around the player
    if currentRoom == 'cell':
        write('> You are sitting against a cold cement wall.')
        write('> Through the darkness you see heavy iron chains dangling from the roof. There is nothing in the room.')
        write('> A small iron door sits in the corner of the room, leading to the dungeon.')

    elif currentRoom == 'dungeon':
        write('> The cold concrete walls of the small dungeon press the room together.')
        write('> There is dried blood and other stains all over the floor.')
        write('> There are various tools on the floor. A bloodstained hammer, A syringe and an empty vial.')
        write('> There is a small staircase bunched into the corner leading upwards.')

def inspect():
    #the users current available objects to inspect
    write('> Inspect is [WIP]')  #need to make a list of every object interactable with the user

def save():
    #will save the game
    write('> Save is [WIP]')

def load():
    #will load the latest save
    write('> Load is [WIP]')

def quit():
    #exits the program
    write('> Later Loser')
    sys.exit()

def userinput():
    #This function will be called anytime input is required from the user (a lot)

    #begins a loop so that the program will ask for input over and over for the game.\
    loop = True
    while loop == True:
        userInput = input('> ').lower()

        #checks if the user asks for any of the commands.
        if userInput == 'help':
            help()


        elif userInput == 'look':
            look()

        elif userInput == 'inventory':
            inv()

        elif 'inspect' in userInput:
            inspect()

        elif 'use' in userInput:

            if 'door' in userInput:

                #--single door rooms--#
                if currentRoom == 'cell':
                    enterDungeon()

                elif currentRoom == 'dungeon':
                    enterCell()

                elif currentRoom == 'storageRoom':
                    enterEntranceHall()

                elif currentRoom == 'kitchen':
                    enterDiningHall()

                elif currentRoom == 'greatLibrary':
                    enterSecondFloor()

                elif currentRoom == 'sq1':
                    enterSecondFloor()

                elif currentRoom == 'sq2':
                    enterSecondFloor()

                elif currentRoom == 'sq3':
                    enterSecondFloor()

                elif currentRoom == 'sq4':
                    enterSecondFloor()

                elif currentRoom == 'sq5':
                    enterSecondFloor()

                elif currentRoom == 'sq6':
                    enterSecondFloor()

                elif currentRoom == 'sq7':
                    enterSecondFloor()

                elif currentRoom == 'sq8':
                    enterSecondFloor()

                elif currentRoom == 'scientist':
                    enterWaitingChamber()

                elif currentRoom == 'officer':
                    enterWaitingChamber()

                elif currentRoom == 'overseer':
                    enterWaitingChamber()

                #--multi door rooms --#
                elif currentRoom == 'entranceHall':

                    if 'dining' in userInput:
                        enterDiningHall()

                    elif 'living' in userInput:
                        enterLivingRoom()

                    elif 'storage' in userInput:
                        enterStorageRoom()

                    else:
                        write('> You can see the Dining Hall door, the Living Room door and the Storage Room door')

                elif currentRoom == 'livingRoom':

                    if 'entrance' in userInput:
                        enterEntranceHall()


                    elif 'dining' in userInput:
                        enterDiningHall()

                    else:
                        write('> You can see the Dining Hall door and the Entrace Hall door')

                elif currentRoom == 'diningHall':

                    if 'living' in userInput:
                        enterLivingRoom()

                    elif 'entrance hall' in userInput:
                        enterEntranceHall()

                    elif 'kitchen' in userInput:
                        enterKitchen()

                    else:
                        write('> You can see the Entrance Hall door, the Kitchen door and the Living Room door')

                elif currentRoom == 'waitingChamber':

                    if 'luther ' in userInput:
                        enterScientist()

                    elif 'hans' in userInput:
                        enterOfficer()

                    elif 'klaus' in userInput:
                        enterOverseer()

                    else:
                        write('> You can see the Scientist\'s door, the Officer\'s door and the Overseer\'s door.')

                elif currentRoom == 'secondFloor':

                    if 'library' in userInput:
                        enterLibrary()

                    elif 'sq1' in userInput:

                        entersq1()

                    elif 'sq2' in userInput:
                        entersq2()

                    elif 'sq3' in userInput:
                        entersq3()

                    elif 'sq4' in userInput:
                        entersq4()

                    elif 'sq5' in userInput:
                        entersq5()

                    elif 'sq6' in userInput:
                        entersq6()

                    elif 'sq7' in userInput:
                        entersq7()

                    elif 'sq8' in userInput:
                        entersq8()

                    else:
                        write('> There are 8 servant quarters lined against the walls of the balcony floor. Type "sq1" - "sq8" to enter them')
                        write('> There is also a large oak door leading to the Library')

                else:
                    error()



            elif 'stair' in userInput:

                if currentRoom == 'dungeon':
                    write('> You climb up the old wooden stairs. They creak beneath your feet.')
                    enterStorageRoom()

                elif currentRoom == 'storageRoom':
                    write('> You step down into the darkness.')
                    enterDungeon()

                elif currentRoom == 'entranceHall':
                    write('> You walk over to the illustrious stairwell and climb up the gold laced steps.')
                    enterSecondFloor()

                elif currentRoom == 'secondFloor':
                    write('> There are two staircases, one leads upward, the other downward. Type "up" to move up or "down" to move down.')
                    stairChoice = input('> ')

                    if stairChoice == 'up':
                        write('> You ascend the dazzling staircase to the third floor.')
                        enterWaitingChamber()

                    elif stairChoice == 'down':
                        write('> You take the glorious staircase down to the first floor.')
                        enterEntranceHall()

                    else:
                        error()

                elif currentRoom == 'waitingChamber':
                    write('> You walk down the lavish staircase to the second floor.')
                    enterSecondFloor()

                else:
                    error()

            else:
                error()

        elif userInput == 'save':
            save()

        elif userInput == 'load':
            load()

        elif userInput == 'quit':
            quit()

        else:
            error()


#---other---#
def write(text):
    #creates the function for text speed
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(textSpeed)
    print('')


#---game---#
def intro():
    # displays the introduction information and commands, and asks the user for a type speed
    areYouSure = 'n'
    while areYouSure == 'n':
        global textSpeed
        textSpeed = 0.08
        write('> Select a type speed: ')
        write('> Type "speed 1" to select this typing speed for the rest of the game.')

        textSpeed = 0.04
        write('> Type "speed 2" to select this typing speed for the rest of the game.')

        textSpeed = 0.01
        write('> Type "speed 3" to select this typing speed for the rest of the game.')
        textSpeedAnswer = input('> ').lower()

        if textSpeedAnswer == 'speed 1':
            textSpeed = 0.08
            write('> This will be the speed of the text for the rest of the game. Are you sure? (y/n)')
            areYouSure = input().lower()

        elif textSpeedAnswer == 'speed 2':
            textSpeed = 0.04
            write('> This will be the speed of the text for the rest of the game. Are you sure? (y/n)')
            areYouSure = input().lower()

        elif textSpeedAnswer == 'speed 3':
            textSpeed = 0.01
            write('> This will be the speed of the text for the rest of the game. Are you sure? (y/n)')
            areYouSure = input('> ').lower()

        if areYouSure == 'y':
            print(' ')
            write('> Welcome to The Iron Cell version 0.0.1')
            write('> The game is still in development so many aspects are works in progress [WIP].')
            write('> Rule 1. Never highlight any area of the CMD line, the program will stop.')
            write('> Rule 2. Never press any button when the game is typing. Only press button when prompted.')
            write('> Rule 3. If you find any bugs, plot holes or other issues please let me know.')
            write('> This is only a test build, any [WIP] commands will do nothing.')
            write('> The commands are as follows:')
            help()
            write('> Good luck. \n'),
            print('---------------------')
            write('Press Enter to begin.')
            print('---------------------')

            #press enter to begin
            while True:
                if keyboard.is_pressed('Enter'):
                    main()

def main():
    #game opening sequence
    write('\n> You awake.'), sleep(0)
    write('> Your head hurts.'), sleep(0)
    write('> You cannot remember anything.'), sleep(0)
    write('> It is dark.'), sleep(0)
    write('> You realise you are not wearing any clothes.')

    userinput()


#===ARRAYS===#

#---objects---#
'''
cell fakewall
cell chains
cell wall
dungeon hammer
dungeon syringe
dungeon vial
storage room supplies
entrance hall chandelier
entrance hall paintings
'''


#---rooms---#
cell = 0
dungeon = 0
storageRoom = 0
entranceHall = 0
livingRoom = 0
diningHall = 0
diningKitchen = 0
greatLibrary = 0
secondFloor = 0
sq1 = 0
sq2 = 0
sq3 = 0
sq4 = 0
sq5 = 0
sq6 = 0
sq7 = 0
bloodiedRoom = 0
waitingChamber = 0
scientist = 0
officer = 0
overseer = 0


#===EXECUTE===#


main()







#===NOTES===#

#Livingroom look
#write('> You enter into a large carpeted space with tables and chairs sprawled as if the occupants had left in a hurry.')
#write('> There are display cabinets lined with dozens of trophies and awards that have no meaning to you. Many of them are smashed and broken.')
#write('> A window takes up most of one wall. You see large cracks as if someone had tried to break it. There are blood splatters on the carpet.')
#write('> Beyond the window, the sun shines upon an endless feild yeilding dying crops.')

#---known_issues---#
#if a room has a single door, typing 'use' and 'door' will always use the door, no matter if there are other words like a door specification

#---testing---#
#first time entry vs standard entry. does that detract from the experience.
#is writing text too slow, is it worth having. what speeds are good.
#spelling errors, full stops, ect.
#is navigation too fiddly? I obviously know the map well and I cant judge how easy it is to navigate and remember rooms
#anytime i reference a room it needs to be capitalised


#---credits---#
#created by Will Olijnyk
#special thanks to playtesters and creative associates Jordan McDonald and Daniel Bowering
#project started on 16/4/19
