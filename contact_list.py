contact_list = {'Ayaz':{
        'name':'Ayaz',
        'phone':5686667,
        'occupation': 'IT Specialist'}, 
    'Arif':{
        'name':'Arif',
        'phone':3464646464,
        'occupation':'Seller'},
    'Bakhtiyar':{
        'name':'Bakhtiyar',
        'phone':43448484,
        'occupation':'Driver'},
    'Javanshir': {
        'name':'Javanshir',
        'phone':4368683653,
        'occupation':'Engineer'},
    'Elman': {
        'name':'Elman',
        'phone':43656565656,
        'occupation':'Administrator'},
    'Elshan':{
        'name':'Elshan',
        'phone':3636436346,
        'occupation':'Sportsman'},
    'Farhad':{
        'name':'Farhad',
        'phone':43436536563,
        'occupation':'Scientist'}
    }
def add_person(nick, name, phone, occupation):
    contact_list[nick] = {
        'name':name,
        'phone':phone,
        'occupation':occupation
    }
def print_person_info(nick):
    return 'Name: {}\nPhone: {}\nOccupation: {}'.format(contact_list[nick]['name'],contact_list[nick]['phone'], contact_list[nick]['occupation'])

while True:
    nick = input('Type about whom you want to see information: ')
    a = nick.capitalize()
    if contact_list.get(a, 'DEFAULT') == 'DEFAULT':
        print('There is no information about this person.\n')
        question = input(f'Do you want to add information about {a} ? [yes/no] ')
        if question == 'yes':
            name = input('Please enter the name: ')
            phone = int(input('Please enter the phone number: '))
            occupation = input('Please enter the occupation: ')
            add_person(a, name.capitalize(), phone, occupation.capitalize())
            print(print_person_info(a))
        else:
            print('Exiting program')
            break
    else:
        print(print_person_info(a))
            

l_question = input('Do you want to see entire contact list? [yes/no] ')
if l_question == 'yes':
    for v in contact_list.values():
        for key, value in v.items():
            print(f'{key} : {value}')
        print('-'*40)
else:
    print('Good Bye')



