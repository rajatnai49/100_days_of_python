import random

def rock_paper_scissor():
    list = ['''
                _______
            ---'   ____)
                (_____)
                (_____)
                (____)
            ---.__(___)
            ''',
            '''
                _______
            ---'   ____)______
                      ________)
                    ___________)
                    __________)
            ---.___________)
            ''',    
             '''
                _______
            ---'   ____)_____
                    _________)
                ____________)
                (____)
            ---.__(___)
           ''']
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2:"))
    computers_choice = random.randint(0,2)
    print(list[player_choice])
    print(list[computers_choice])
    
    if computers_choice == 2 and player_choice == 0:
        print("You win this round!") 
    elif computers_choice == 0 and player_choice == 2:
        print("You loser!!")
    elif player_choice > computers_choice:
        print("You win this round!")
    elif computers_choice == player_choice:    
        print("Tie!!!")
    else:
        print("You loser!!")
    further_choice = input("You want to play another round?\nyes/no")
    if further_choice == "yes":
        return True
    return False
    
flag = True
while flag:
    flag = rock_paper_scissor()