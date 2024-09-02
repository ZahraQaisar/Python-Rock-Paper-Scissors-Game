from random import choice

game = ['Rock', 'Paper', 'Scissors']

game_choice = True

while(game_choice):
    player_input = input("Select one ROCK / PAPER / SCISSORS: ")
    player = player_input.lower()
    generate = choice(game)
    generated = generate.lower()
    
    print('User: ',player)
    print('Computer: ', generated)
    

    if player == generated:
        print("Tie!")
        
    elif player != generated:
        if player == 'rock' and generated == 'paper':
            print("Player won!")
        elif player == 'rock' and generated == 'scissors':
            print("Player won!")
        elif player == 'scissors' and generated == 'paper':
            print("Player won!")
        elif player == 'scissors' and generated == 'rock':
            print("Computer won!")
        elif player == 'paper' and generated == 'scissors':
            print("Computer won!")
        elif player == 'paper' and generated == 'rock':
            print("Computer won!")
        else:
            print("invalid input")
            
    again = input("Do you want to continue? yes/ no : ")
    again.islower()
    
    if again == 'no':
        game_choice = False
        
