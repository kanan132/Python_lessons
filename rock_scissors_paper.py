import random
game, comp, human, draw = 0, 0, 0, 0
l = ('Rock', 'Scissors', 'Paper')
while True:
    selection = input('Make your choice: Rock or Scissors or Paper or press q to finish the game: ')
    comp_choice = random.choice(l)
    if selection !='q':
        selection.capitalize()
        game+=1
        
        if comp_choice=='Rock':
            if selection == 'Paper':
                human+=1
            elif selection == 'Scissors':
                comp+=1
            else:
                draw+=1
        elif comp_choice=='Scissors':
            if selection == 'Rock':
                human+=1
            elif selection == 'Paper':
                comp+=1
            else:
                draw+=1
        elif comp_choice == 'Paper':
            if selection == 'Paper':
                draw+=1
            elif selection == 'Scissors':
                human+=1
            else:
                comp+=1

        print(f'Game: {game}, Computer: {comp}, Human: {human} Draw: {draw}')
    else:
        print('Ending the game')
        break
    

