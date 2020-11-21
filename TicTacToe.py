def game_setup():
    global win
    win=0
    player=''
    ready = 'wrong'
    print("Hello! Time to play tic, tac, toe. Take turns with a friend entering the position you want to set your X or O to using 1-9. 1 will be the top left corner and 9 will be the bottom right corner. Player 1 will always be X and player 2 is always O.")
    while ready.upper() not in ['YES','NO']:
        ready = input('Are you ready to play? ')
        if ready.upper() not in ['YES','NO']:
            print("I don't know what you said. Please type in yes or no.\n")
    if ready.upper() == 'YES':
        print("Excellent! Let's get started.\n")
        player = 1
        return True, player
    else:
        return False,player

def draw_board(board):
    for i in range(5):
        if i % 2==0:
            if i == 0:
                print(board[0] + ' | ' + board[1] +' | ' +board[2])
            elif i == 2:
                print(board[3] + ' | ' + board[4] +' | ' +board[5])
            else:
                print(board[6] + ' | ' + board[7] +' | ' +board[8])
        else:
            print('-- '*3)
    print('\n')

def player_choice(board,player):
    global turns
    if player == 1:
        count = board.count('X')
        marker = 'X'
    else:
        count = board.count('O')
        marker='O'
    count_map={0:'first',1:"second",2:"third",3:"fourth",4:"fifth"}
    answer = 'wrong'
    acceptable = ['1','2','3','4','5','6','7','8',']
    while answer not in acceptable:
            answer=input(f"Player {player}, where will you place your {count_map[count]} {marker}? (1-9) ")
            if answer not in acceptable:
                print("That's not a valid answer.\n")
            elif board[int(answer)] != ' ':
                answer='wrong'
                print('That spot is already taken!\n')
    turns += 1
    answer = int(answer) - 1
    return answer

def change_board(board, player, answer):
    if player == 1:
        marker = 'X'
        board[answer] = marker
        player = 2
    else:
        marker = 'O'
        board[answer] = marker
        player=1
    return board, player


def check_win(board):
    global win
    win_patterns = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    if board.count('X') >=3 or board.count('O') >=3:
        for pat in win_patterns:
            if board[pat[0]] == board[pat[1]] == board[pat[2]] == 'X':
                win=True
                print('We have a winner!! Player 1 wins the game.\n')
            elif board[pat[0]] == board[pat[1]] == board[pat[2]] == 'O'::
                win=1
                print('We have a winner!! Player 2 wins the games.\n')
            elif board.count(' ') == 0:
                print('It\'s a draw! \n')
                win=2
    return win

def main():
    game_on = True
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    win = 0
    turns = 0
    while game_on:
        game_on, player = game_setup()
        while (win==0) & (game_on):
                draw_board(board)
                position = player_choice(board, player)
                board, player = change_board(board, player, position)
                if turns > 3:
                    win = check_win(board)
                    if win > 0:
                        draw_board(board)
                        game_on=False
                turns += 1
    print('Goodbye!\n')

if __name__ == '__main__':
    main()
