'''
A refactor from the book: Raspberry Pi Beginner's guide 4th edition. It's productive to iterate that the original code is simple
and intuitive and the target audience seems to be children and adolescents, and is exellent for its intents. The proposed changes are intented
for university students or advanced learners. Engineering is always a matter of ballancing trade-offs. The proposed changes are from the perspective
of a software engineer and they will increase the code complexity, but by exchange it will make it extensible. 

It drew my attention because I regonized it's high teaching potetial, one thing that could be improved from the original is the structure.
How the structure should be improved? I suggest by organizing the code into sections  in a manner that it should be follow a logical 
structural pattern: "A game uses methods, methods can use data"

  1 Data
  2 Methods
  3 Game
  
'''

#Data

#It came to my mind that this is an excellent section to ponder about how data are used in an information system.

#A flag to crontrol the game loop
is_running = True

#Player position, starting at the Hall
current_location = 'Hall'

#An inventory modeled as a list, which is initially empty
inventory = []

#The map modeled as a dictionary linking a room to other rooms, a good exercise would be to draw the map to teach 
rooms = {
            'Dining room':{
                  'west' : 'Hall',
                  'south': 'Garden'
              },
            'Hall' : { 
                  'east' : 'Dining room',
                  'south' : 'Kitchen',
                  'item' : 'key'
                  
                },
            'Garden':{
                'north': 'Dining room',
                'item':'potion'
            },
            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster'
                }

         }

#Methods

def game_instructions():
  """Prints the game's instructions
  """
  print('''
        Maze Explorer

Commands:

  go [direction]
  get [item]
''')

#This here presents another good discussion about modularity.

def display_status():
  #print the player's current status
  print('\n')
  print('You are in the ' + current_location)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[current_location]:
    print('You see a ' + rooms[current_location]['item'])
  print("\n")

#Game loop

game_instructions()

# In the original, it used a while True: which is not a recommended pratice while building software, infinite loops can create problems
#as the software complexity grows.
while is_running:

  display_status()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[current_location]:
      #set the current room to the new room
      current_location = rooms[current_location][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[current_location] and move[1] in rooms[current_location]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[current_location]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!') 
      
  # Player loses if he/she enters in a room with a monster
  if 'item' in rooms[current_location] and 'monster' in rooms[current_location]['item']:
      print("Game over")
      break
  
  # Wining condition
  if current_location == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print("You scaped the house")
    break


