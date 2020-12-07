from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def player_guess():

    guess = ''

    while guess not in ['0','1','2']:
        guess = input('''Pick A Number ['0';'1';'2'] :''')
        
    return int(guess)

def check_guess(my_list,guess):

    if my_list[guess] == 'O' :
        print('Correct!!!')
    else:
        print('Wrong Guess!!!')
        print(my_list)

#This is the INITIAL LIST       
my_list = [' ','O',' ']

#This is the SHUFFLED LIST
shuffled_list = shuffle_list(my_list)

#This is the USER GUESS
guess = player_guess()

#This is the CHECK GUESS
check_guess(shuffled_list,guess)

