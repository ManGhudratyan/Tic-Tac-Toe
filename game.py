import random;

def game_xo(ml, answer):
    player1 = 'X';
    player2 = 'O';

    def show_board(board):
        for row in board:
            print(' '.join(row));

    def check_winner(player):
        if (ml[0][0] == ml[1][1] == ml[2][2] == player or
            ml[0][2] == ml[1][1] == ml[2][0] == player or
            ml[0][0] == ml[0][1] == ml[0][2] == player or
            ml[1][0] == ml[1][1] == ml[1][2] == player or
            ml[2][0] == ml[2][1] == ml[2][2] == player or
            ml[0][0] == ml[1][0] == ml[2][0] == player or
            ml[0][1] == ml[1][1] == ml[2][1] == player or
            ml[0][2] == ml[1][2] == ml[2][2] == player):
            show_board(ml);
            print(f'Player {player} wins!');
            return True;
        return False;

    player = player1;
    while (True):
        show_board(ml);

        if (player == player1):
            row = int(input(f'Player {player}, please enter the row (0, 1, 2): '));
            column = int(input(f'Player {player}, please enter the column (0, 1, 2): '));
        else:
            if (answer == '1'):
                row = int(input(f'Player {player}, please enter the row (0, 1, 2): '));
                column = int(input(f'Player {player}, please enter the column (0, 1, 2): '));
            else:
                empty_spaces = [];
                for i in range(3):
                    for j in range(3):
                        if (ml[i][j] == '-'):
                            empty_spaces.append((i, j));
                if (empty_spaces):
                    row, column = random.choice(empty_spaces);
                    
        if (ml[row][column] == '-'):
            ml[row][column] = player;
        else:
            print('This space is already occupied. Please choose an empty space.');
            continue;

        if (check_winner(player)):
            break;

        if (player == player1):
            player = player2;
        else:
            player = player1;

def main():
    ml = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ];

    answer = input('Play the game with 1. Another person  2. Computer? ');

    if (answer == '1'):
        print("You have chosen to play with another person. Let's start!");
    elif (answer == '2'):
        print("You have chosen to play against the computer. Let's start!");
    else:
        print('Please choose 1 or 2.');

    game_xo(ml, answer);

if __name__ == "__main__":
    main();
