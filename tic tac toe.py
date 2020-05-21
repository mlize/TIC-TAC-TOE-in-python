#################
#Tic Tac Toe -Game
#################


#####################################
# Build Functions: 
import random 
import csv



# Display board 
def display_board(board):
    print('  {}  |  {}  |  {}  '.format(board[7],board[8],board[9]))
    print('-------------------')
    print('  {}  |  {}  |  {}  '.format(board[4],board[5],board[6]))
    print('-------------------')
    print('  {}  |  {}  |  {}  '.format(board[1],board[2],board[3]))

#  
def player_input(marker):
    marker = str(input('Player 1 choose "X" or "O" : ' ))
    while  marker.lower() not in ['x','o'] :
        print('{} not a valid entry.'.format(marker))
        marker = str(input('Player 1 choose "X" or "O" : ' ))              
    return marker.upper() 
#
def place_marker(board, marker, position):
    board[position] = marker.upper()
    return  board
#
def win_check(board, marker):
    
    winning_positions = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
    check = False
    
    for pos in winning_positions:
        if grab_position(board,pos) == [marker]*3:
            check = True
    return check    
#    
def grab_position(lst,position):
    # grab only  the elements of the lst 
    newlist = []
    for i in range(0, len(lst)):
        if i  in position:
            newlist.append( lst[i])
    return newlist    
#
def choose_first():
    return random.randint(1,2)    
#
def space_check(board, position):
    return board[position] == ' ' or board[position] == '' 
#
def full_board_check(board):
    for char in board:
        if char == ' ':
            return False
    else: 
        return True

#
def player_choice(board):
    position = int(input('Enter your next move: '))
    
    # Check if the number is valid input
    # while position not in range(1,9):
    #    position = int(input('{} is not a valid position, please enter a number from (1-9):  '.format(position) ))
    #    
    #    # check if the spot if free, if is not free, ask again:
    while  not space_check(board,position):
        position = int(input('{} is not free, please enter a free space:  '.format(position) ))
        
    return position  
#
def replay():
    answear = input('Do you want to play again? Type "yes" or "no": ' )
    # test if the answear is yes or no.
    while answear.lower() not in ['yes','no']:
        print('{} is not a valid answear'.format(answear))
        answear = input('Do you want to play again? Type "yes" or "no": ' )
        

    return answear == 'yes' 
#
def nextPlayer(num):
    return num%2 +1

def computer_input(board):
    # computer position is random 
    pos = random.randint(1,9)
    while  not space_check(board,pos):
        pos = random.randint(1,9)
    return pos




####################################
# Game structure: 
####################################

print('Welcome to Tic Tac Toe!')
number_of_players = int(input('Choose how many players (1-2) '))

play = True
player_Marker = ['#','X','O']
computer = False

if number_of_players  == 1 :
    computer = True
    
while play:
    
        
    # Setting  the game here
    
    player_Marker[1] = player_input(player_Marker[1])
    if player_Marker[1] == 'X':
        print('Player1 is X' )
        print('Player2 is O' )
    else:
        player_Marker[2] = 'X'
        print('Player1 is O ' )
        print('Player2 is X ' )
    
    # Set the instructions: 
    print('\n'*2)
    print('Use the number grid(1-9) to place "X" or "O" :')
    print('\n'*2)
    board = ['#','1','2','3','4','5','6','7','8','9']
    display_board(board)
    # clear the board
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print('\n'*2)

    # Select randomly which player starts 
    first_player = random.randint(1,2)

    if  computer and first_player == 2 :
        position = computer_input(board)
    else:
        position = int(input('Player {} starts. Enter you move: '.format(first_player)))
    print('\n'*2)
    board[position] = player_Marker[first_player] 
    display_board(board)
    print('\n'*2)
    Next_Player = nextPlayer(first_player)
    
    game_on = True
    
    while game_on:
        
    # Player  Turn
        if computer and Next_Player == 2:
            position = computer_input(board)
        else:
            print('Player {} Turn: \n'.format(Next_Player))
            position = player_choice(board) 
        print('\n'*2)
        board[position] = player_Marker[Next_Player]
        display_board(board)
        print('\n'*2)
        
        
    # Check if some one won the game:
        if win_check(board,player_Marker[Next_Player]):
            print('Player {} won!!:'.format(Next_Player))
            break
        
    # Check if the board is Full 
        game_on = not full_board_check(board)
        
    # Select the next player
        Next_Player = nextPlayer(Next_Player)
        
        
        
        
    print('\n'*2)
    ############################# Saving the game in a  cvs file ###############################
    
    # a+ append to a the file, and create one if the file does not exist. 
    with open('tic_tac_toe_game.csv', mode='a+') as tic_tac_toe_game:      
        tic_tac_toe_game = csv.writer(tic_tac_toe_game, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tic_tac_toe_game.writerow(board)

    play = replay()
    if not play:
        break