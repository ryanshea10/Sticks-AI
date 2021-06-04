
GAME_RUNNING = True
# TODO add player globals here

print('WElCOME TO STICKS')

input('Would you like to play against the computer or another player\n')

print('There are no computers available to play at the moment')

def player_turn():
    print('It is player BAH\'s turn')
    turn_options()
    # check for a loss

def turn_options():
    turn_option = prompt('You may either: \n  (1) Attack \n  (2) Bump', ['1', '2'])
    if (turn_option == '1'):
        print('Attack!')
    if (turn_option == '2'):
        print('Bump!')

def prompt(promt_arg, expected='EXPECTED_STRING'):
    verify_input = (expected != 'EXPECTED_STRING')
    response = input(promt_arg + '\n')
    while (verify_input):
        if (response in expected): break
        
        print('Your response was not understood.')
        response = input(promt_arg + '\n')
    print()
    return response


while(GAME_RUNNING):
    # promt player 1
    # prompt player 2
    player_turn()
