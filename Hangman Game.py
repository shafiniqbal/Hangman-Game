import csv
import random
from string import ascii_letters


def rand_word():
    rndm = random.randint(1,92238)
    with open(r'Custom Words mid range.csv') as fd:
        read=csv.reader(fd)
        for i,j in enumerate (read):        
            if i==rndm:
                return j[0]

            
def user_input():
    c = input("Guess a character  : ")
    if c not in ascii_letters or len(c)>1:
        print('Enter a single valid letter')
        return user_input()
    else:
        return c.lower()


def curr_state(word,error,char,hidden):
    if char in word:
        for i,j in enumerate(word):
            if j==char:
                hidden=hidden[:(i*2)+1]+j+hidden[(i*2)+2:]
        
    else:
        print('\n~~~Wrong answer. Try another...\n\n')
        error+=1
    return error, hidden
        
    
    
    
while True:
    
    word = rand_word()
#     print(word)           ###delete.............................
    print(f'A {len(word)} lettered word...')
    hidden = '\'' + "_ " * len(word) + '\''
    
    error = 0
    tried = []
    
    while error < 6:
        
        print(hidden)
        print(f'\nYou have {6-error} chances: Error--- {error}')  
        char = user_input()
        if char in tried:
            print('\n~~~You have already entered this letter. Try another...\n')
        else:
            tried.append(char)
            error,hidden = curr_state(word,error,char,hidden)
        if '_' not in hidden:
            print('\n\n\n   ~~~~Congratulations!!!    You got it~~~~ \n')
            break
            
    if '_' in hidden:
        print(f'\n\n   ~~~Correct answer was :   \'{word.upper()}\'   Better Luck next time~~~')
        
        
        
        
    playagain = input("\n\nPlay again?? press \'n\' to cancel :")
    if playagain == 'n':
        break
    else:
        print("\n\n\n\nNew Game\n\n")

