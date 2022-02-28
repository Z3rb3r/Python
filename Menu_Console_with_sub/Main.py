import os
import subprocess
clear = lambda: os.system('cls')

menu_options = {
    1: 'Utilitaires',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

sub_menu_options_1 = {
    1: 'Calculatrice',
    2: 'Sub Option 2',
    3: 'Sub Option 3',
    4: 'Exit',
}

menu_program = {
    1: 'Close',
    2: 'Return',
    3: 'Go to main menu',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def sub_print_menu():
    for key in sub_menu_options_1.keys():
        print (key, '--', sub_menu_options_1[key] )

def sub_memu_program():
    for key in menu_program.keys():
        print (key, '--', menu_program[key] )

def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False

def option1():
    clear()
    print('Choose second option...')
    sub_print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    #Check what choice was entered and act accordingly
    if option == 1:
        calculatrice()
    elif option == 2:
        print('You choose sub menu option 2')
    elif option == 3:
        print('You choose sub menu option 3')
    elif option == 4:
        print('Go to main menu')
        return
    else:
        print('Invalid option. Please enter a number between 1 and 4.')

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')


def calculatrice():
    clear()
    if not process_exists('Calculator.exe'):
        from subprocess import call
        call(["calc.exe"])
    sub_memu_program()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    #Check what choice was entered and act accordingly
    if option == 1:
        os.system("taskkill /F /IM Calculator.exe")
        option1()
    elif option == 2:
        print('Go back')
        option1()
    elif option == 3:
        print('Go to main menu')
        return
    else:
        print('Invalid option. Please enter a number between 1 and 2.')


if __name__=='__main__':
    while(True):
        clear()
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')