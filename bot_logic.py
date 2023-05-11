import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def roll_dice():
    roll = random.choice (['1', '2', '3', '4', '5', '6'])
    if roll == '1':
        return "1"
    if roll == '2':
        return "2"
    if roll == '3':
        return "3"
    if roll == '4':
        return "4"
    if roll == '5':
        return "5"
    if roll == '6':
        return "6"

def guess_number():
    number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    return number
