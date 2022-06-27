# A game with Python, Lost In Forest
from os import system, name

# Define Variables
actorPosition = 0
actorrow = 1
actorShape = '#'


while(True):
    # IF, else branching to clear the screen and update the actor location in the screen
    # System command to clear the terminal based on nt (windows) or unix (mac, ubuntu, debian, redhat etc)
    if( name == 'nt'):
        system('cls')
    else:
        system('clear')

    # Print * to denote a row of tree tops for 50 times
    print('*'*50)
    
    # Print * to denote a row of tree tops for 50 times
    print('*'*50)

    # Print * to denote a row of tree tops for 50 times
    print('*'*50)

    # Print * to denote a row of tree tops for 50 times
    print('*'*50)
    
    
    # Print \n to denote rows of empty space for 1 times
        #print('\n'* 2)

    # actorPosition is along the horizontal direction
    # Print space characters based on how much the actor has moved and then print the actorShape
    if actorrow == 0:   
        print(' '*actorPosition, actorShape)
        print('\n'*3)    

    elif actorrow == 1:
        print('\n'* 1)
        print(' '*actorPosition, actorShape)
        print('\n'* 1)
    
    elif actorrow == 2:
        print('\n'* 3)
        print(' '*actorPosition, actorShape)


    # Print * to denote a row of tree tops for 50 times
    print('*'*50)
    # Print * to denote a row of tree tops for 50 times
    print('*'*50)
    # Print * to denote a row of tree tops for 50 times
    print('*'*50)
    # Print * to denote a row of tree tops for 50 times
    print('*'*50)
    direction = int(input('Which direction you want to go? (6) Right, (4) Left, UP (8), Down(2) : '))
    
    if direction == 4:
        actorPosition -= 1

    elif direction == 6:
        actorPosition += 1

    elif direction == 8:
        actorrow -= 1 # (-= 1 is same as += -1)
    
    elif direction == 2:
        actorrow += 1
    
    # we can use actorraw = max(0, actorraw)
    # we can use actorraw = min(2, actorraw)
    
    
    if(actorPosition > 48):
        print('\n'*4)
        print('='*50)
        print('Hurray you left the forest')
        print('='*50)
        print('\n'*4)
        break
    if actorrow == 3:
        print('\n'*4)
        print('='*50)
        print('Hurray you Reached the Lower Forest Line')
        print('='*50)
        print('\n'*4)
        break
    if actorrow == -1:
        print('\n'*4)
        print('='*50)
        print('Hurray you Reached the Upper Forest Line')
        print('='*50)
        print('\n'*4)
        break