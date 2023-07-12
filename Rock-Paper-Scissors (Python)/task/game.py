import random
import itertools


def getchoice():
    global choices
    choice = input()
    if choice == '!exit':
        print("Bye!")
        exit()
    elif choice == '!rating':
        rating()
        return getchoice()
    elif not choices:
        if choice == "":
            choices = set_default
        elif len(choice.split(',')) > 1:
            choices = choice.split(',')
            print(choices)
        generatewindic()
        print("Okay, let's start")
        return getchoice()
    elif choice not in choices:
        print('Invalid input')
        return getchoice()
    return choice


def result(choice, response):
    prompts = {'Loss': f'Sorry, but the computer chose {response}',
               'Draw': f'There is a draw ({response})',
               'Win': f'Well done. The computer chose {response} and failed'}
    global score
    if (choice, response) in wins:
        return prompts['Loss']
    if choice == response:
        score += 50
        return prompts['Draw']
    if (response, choice) in wins:
        score += 100
        return prompts['Win']


def game():
    choice = getchoice()
    response = random.choice(choices)
    print(result(choice, response))
    return game()


def greetings():
    global score
    score = 0
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    rating = open('rating.txt', 'r')
    for line in rating:
        if line.split()[0] == name:
            score = int(line.split()[1])
            break
    rating.close()


def rating():
    print(f'Your rating: {score}')


def generatewindic():
    quantity = len(choices)
    for i, j in itertools.product(range(quantity), repeat=2):
        if (0 < (j-i) < quantity/2) or (quantity/2 < (i-j)):
            wins.append((choices[i], choices[j]))
    return wins


set_default = ['rock', 'paper', 'scissors']
choices = []
wins = []

greetings()
game()
