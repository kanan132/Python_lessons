import random
game, comp, human, draw = 0, 0, 0, 0
l = ('Rock', 'Scissors', 'Paper')
def result(comp_choice, human_choice):
    global game, human, comp, draw
    human_choice.capitalize()
    
    game+=1
        
    if comp_choice=='Rock':
        if human_choice == 'Paper':
            human+=1
        elif human_choice == 'Scissors':
            comp+=1
        else:
            draw+=1
    elif comp_choice=='Scissors':
        if human_choice == 'Rock':
            human+=1
        elif human_choice == 'Paper':
            comp+=1
        else:
            draw+=1
    elif comp_choice == 'Paper':
        if human_choice == 'Paper':
            draw+=1
        elif human_choice == 'Scissors':
            human+=1
        else:
            comp+=1
    return f'Game: {game}, Computer: {comp}, Human: {human} Draw: {draw}'

while True:
    selection = input('Make your choice: Rock or Scissors or Paper or press q to finish the game: ')
    comp_choice = random.choice(l)
    if selection !='q':
        print(result(comp_choice, selection))
    else:
        print('Ending the game')
        break
    

