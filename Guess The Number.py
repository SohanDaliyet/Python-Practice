from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def player_guess():

    guess = ''

    while guess not in ['0','1','2']:
        guess = input('''Pick A Number ['0';'1';'2'] :''')

