import random
number = random.randint(1, 100)
print(number)

import random
number = random.randint(1, 10)
print("Your lucky number is:", number)

import random

Nigerian_food = ["Egusi", "Jollof", "Akara", "Alele", "Kunu"]
Temple = random.choice(Nigerian_food)
print("Today's food is:", Temple)

import random
name = ["Temple", "Grace", "Bryan", "Sophie", "David"]
random.shuffle(name)
print(name)

import random
programming = ["Python", "Java", "C++", "JavaScript", "Go"]
random.shuffle(programming)
print(programming)
print("The first language is:", programming[0])

import random
States = ["Lagos", "Abuja", "Kano", "Ibadan", "Enugu", "Benin"] 
Selected_states = random.sample(States, 4)
print(Selected_states)

import random
language = ["Python", "Python", "Java", "C++", "JavaScript", "Go"]
selected_languages = random.sample(language, 4)
print(selected_languages)

import random
number = random.random()
print(number)

import random
price = random.uniform(10, 50)
print("The random price is:", price)