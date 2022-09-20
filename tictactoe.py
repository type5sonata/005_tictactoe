def construct_empty_board():
    return [[0,0,0],[0,0,0],[0,0,0]]


def print_board(board):
    print("   [1][2][3]")
    for value, line in enumerate(board):
        print(f"[{value+1}]", end='')
        for square in line:
            if square == 0:
                print ("[ ]", end='')
            elif square == 1:
                print ("[X]", end='')
            elif square == 2:
                print ("[O]", end='')
        print('\n')
    return None

def print_round_number(round, player):
    print(f"ROUND {round}, PLAYER {player}'S TURN")
    return None

def validate_move(move):
    if move in [0,1,2]:
        return True
    else:
        return False

def read_move(row_or_column, player):
    if row_or_column == 'row':
        move = int(input(f'Write in a row number to put down your {player}:'))-1
    elif row_or_column == 'column':
        move = int(input(f'Write in a column number to put down your {player}:'))-1
    if validate_move(move):
        return move
    else:
        print("The number you entered is invalid (it must be 1, 2, or 3).")
        return read_move(row_or_column, player)
    
    
def run_turn(board, player, round):
    print_round_number(round, player)
    
    if player == 'X':
        value = 1
    elif player == 'O':
        value = 2
    
    move_row = read_move('row', player)
    move_column = read_move('column', player)
    
    #Update board
    board[move_row][move_column] = value

    
    return board

def check_state(board):
    state = None
    #1 if X wins
    #2 if O wins
    #check if there is a column with 1s or 2s only
    columns = [[0,0,0],[0,0,0],[0,0,0]]
    
    for column in range(3):
        for row_number, row in enumerate(board):
            columns[column][row_number] = row[column]
    #Diagonals
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
        ]
    #Lines
    if [1,1,1] in board:
        state = 1
    elif [2,2,2] in board:
        state = 2
    elif [1,1,1] in columns:
        state = 1
    elif [2,2,2] in columns:
        state = 2
    elif [1,1,1] in diagonals:
        state = 1
    elif [2,2,2] in diagonals:
        state = 2
    elif 0 not in (item for sublist in board for item in sublist):
        state = 3 #draw
    else:
        state = 0 #continue
        
    return state

def run_round(board, round, game_state):
    board = run_turn(board, 'X', round)
    print_board(board)
    game_state = check_state(board)
    if game_state in [1,2,3]:
        return board, round, game_state
    board = run_turn(board, 'O', round)
    print_board(board)
    game_state = check_state(board)
    if game_state in [1,2,3]:
        return board, round, game_state
    else:
        round += 1
        return board, round, game_state

def game():
    board = construct_empty_board()
    game_round = 1
    state = 0
    
    print_board(board)
    
    while state == 0:
        board, game_round, state = run_round(board, game_round, state)
   
    state_dict = {
        1 : 'X wins!',
        2 : 'O wins!',
        3 : "It's a draw!"
    }
    
    print(state_dict[state])
    
    another_game = input('Another game? [Y/N]')
    if another_game == 'Y':
        game()
    else:
        return None
    

if __name__ == '__main__':
    game()

      
    
    
    
    
    