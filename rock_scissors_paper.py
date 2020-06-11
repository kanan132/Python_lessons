import random
game, comp, human, draw = 0, 0, 0, 0
l = ('Rock', 'Scissors', 'Paper')
while True:
    selection = input('Make your choice: Rock or Scissors or Paper or press q to finish the game: ')
    comp_choice = random.choice(l)
    if selection !='q':
        s = selection.capitalize()
        game+=1
        print(f'Human Choice: {s}\nComputer Choice: {comp_choice}')
        
        if comp_choice=='Rock':
            if s == 'Paper':
                human+=1
                print('Human Wins!')
            elif s == 'Scissors':
                comp+=1
                print('Computer Wins!')
            else:
                draw+=1
                print('Draw!')
        elif comp_choice=='Scissors':
            if s == 'Rock':
                human+=1
                print('Human Wins!')
            elif s == 'Paper':
                comp+=1
                print('Computer Wins!')
            else:
                draw+=1
                print('Draw!')
        elif comp_choice == 'Paper':
            if s == 'Paper':
                draw+=1
                print('Draw!')
            elif s == 'Scissors':
                human+=1
                print('Human Wins!')
            else:
                comp+=1
                print('Computer Wins!')

        print(f'Game: {game}, Computer: {comp}, Human: {human} Draw: {draw}')
        print('-'*40)
    else:
        print('Ending the game')
        break
    

