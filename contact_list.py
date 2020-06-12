contact_list = {'Ayaz':5686667, 'Arif':3464646464, 'Bekhtiyar':43448484, 'Javanshir': 4368683653, 'Elman': 43656565656, 'Elshan':3636436346, 'Farhad':43436536563}
while True:
    name = input('Type whose phone number you want to see: ')
    n = name.capitalize()
    if n in contact_list.keys():
        print(f'{n}\'s phone number is {contact_list[n]}')
    else:
        question = input('Do you want to add this person\'s number?: ')
        if question == 'yes' or question == 'Yes' or question == 'YES':
            phone = int(input('Please enter the phone number: '))
            contact_list[n] = phone
            print(f'{n}\'s phone number is {contact_list[n]}')
        else:
            print('Ending program')
            break
