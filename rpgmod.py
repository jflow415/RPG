#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'description' : 'You are in the Hall of the dead. Steal your fears and push onward young champion. To the east is the dining room and to the south is the kitchen.',
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'south' : 'Torture Room',
                  'item'  : 'monster',
                  'description' : 'You hear blades being sharpened around you. Look out for Teddy! To the north is the hall and to the south is the Torture room.'
                },
                #added torture room with chain item
                'Torture Room' :{
                    'north' : 'Kitchen',
                    'item' : 'chains',
                    'description' : 'You made it pass Teddy young champion! Now you are in the torture room. There is no way to go but back up.'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
                  'description' : 'The dining room only has one chair, but four plates are are set? To the west is the Hall. To the south is the pantry and the garden lies below', 
               },
               #added items to garden
            'Garden' : {
                  'north' : 'Dining Room',
                  'item' : 'healthy herb',
                  'description' : 'The garden is a safe haven with plenty of fruits and vegitables. To the north is the dining room and to the south is the freedom room.'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
                  'description' : 'The pantry holds stain clothes that smell like blood and urine. The only way out is south to the Dining room.'
            },
            #added freedom room with items (there is no true escape)
            'Freedom room' : {
                'north' : 'Garden',
                'item' : 'bible',
                'description' : 'You have found the freedom room with an open window that leads to the roads. Wait! There is a shadowy figure in the corner.'
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break