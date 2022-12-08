# 00089345
import random

def get_number_dials():
    num_dials = (input('Each lock has how many dials? '))
    print(num_dials)

def get_how_many_to_list(): # accepts nothing
    num_lock_combos = int(input('How many lock combintations should be displayed: '))
    print(num_lock_combos)

def get_number(): # accepts two integers
    min = random.randrange(0, 9)
    mid = random.randrange(0, 9)
    max = random.randrange(0, 9)
    while min and max <= 4:
        print("Number 1", min, mid, max)
        min += 1
        mid =+ 1
        max += 1

def next_combo_number():
    pass

print('This application generates possible lock combinations; assuming that the numbers will be from 0 to 9(inclusive). Please enter the quantity of dials on the combinations locks. And then enter how many combinations you would like to generate.')
print('')

get_number_dials()
get_how_many_to_list()
get_number()
