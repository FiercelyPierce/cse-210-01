'''
W02 Prove: Developer - Solo Code Submission
Created by: Pierce
'''

from time import sleep

def main():
    print('\nWelcome to a simple game of Tic-Tac-Toe!')
    sleep(2)
    print('\nThis is a 2 player game, the first player will be "X" while the second player will be "O".')
    sleep(3)

    player = next_player()
    grid = create_grid()

    while not (player_winner(grid) or player_tie(grid)):
        sleep(1)
        display_grid(grid)
        sleep(1)
        make_a_move(player, grid)
        player = next_player(player)
    display_grid(grid)
    print(f"That was a good game. Thanks for playing!") 


def create_grid():
    grid = []
    for square in range(9):
        grid.append(square + 1)
    return grid


def display_grid(grid):

    print('\nHere is the grid:\n')
    print(
        f' {grid[0]} | {grid[1]} | {grid[2]} \n'
        '---+---+---\n'
        f' {grid[3]} | {grid[4]} | {grid[5]} \n'
        '---+---+---\n'
        f' {grid[6]} | {grid[7]} | {grid[8]} \n')


def player_winner(grid):
    return (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6])


def player_tie(grid):
    for square in range(9):
        if grid[square] != 'X' and grid[square] != 'O':
            return False
    return True


def next_player(current=''):
    if current == '' or current == 'O':
        return 'X'
    elif current == 'X':
        return 'O'


def make_a_move(player, grid):
    square = int(input(f'Player {player}, it is your turn to choose a square. Pick a number from 1-9: '))
    grid[square - 1] = player


if __name__ == "__main__":
    main()