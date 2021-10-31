import random

list_temp = []
opt = int()

def menu():
    print('''
Menu:
1. Fill the list manually
2. Fill the list automatically with random values
3. Display data
4. Obtain maximum and minimum temperature
5. Display data in ascending order
6. Display data in descending order
7. Exit
''')

    while True:
        try:
            global opt
            opt = int(input('Select an option: '))
        except:
            print('Invalid command, please try again.')
            continue
        break

menu()

if (opt == 1):
    for i in range(15):
        while True:
            try:
                temp = int(input('Enter the temperature of element #' + str(i + 1) + ': '))
                if (temp <= 40):
                    list_temp.append(temp)
                else:
                    print('The temperature entered must not be higher than 40')
                    continue
            except ValueError:
                print('Error, please enter an integer')
                continue
            break         
    menu()

if (opt == 2):
    list_temp.clear()
    for i in range(15):
        list_temp.insert(i, random.randint(-88, 40))
    menu()

if (opt == 3):
    print(list_temp)
    menu()

if (opt == 4):
    maxima = max(list_temp)
    minima = min(list_temp)
    print('The maximum temperature is of ' + str(maxima) + ' degrees')
    print('The minimum temperature is of ' + str(minima) + ' degrees')
    menu()

if (opt == 5):
    list_temp.sort()
    print(list_temp)
    menu()

if (opt == 6):
    list_temp.sort(reverse = True)
    print(list_temp)
    menu()

if (opt == 7):
    print('Program closed')

if(opt > 7 or opt < 1):
    print('The option selected is not in the menu.')