number = 1
while number <= 5:
    if number == 3:
        pass
    print(number)
    number =  number + 1    

number = 1
while number <= 10:
    if number == 5:
        pass
    print(number)
    number = number + 1

names  = ["victoria", "joy", "peter", "temple", "stephen"]
for name in names:
    if name == "temple":
        pass
    print(name)    

student_score = {
    "Grace": [4, 9],
    "Bryan": [2, 0, 8],
    "Sophie": [1, 2, 3, 6]
}
for name in student_score:
      print(name, student_score[name])
print()

name_score = {
    "David": [7, 8],
    "Mary": [5, 9, 6],
    "Alex": [10, 4]
}      
for name in name_score:
    print(name, name_score[name])
print()

products = {
    "Phone": 120000,
    "Laptop": 450000,
    "Headphones": 35000
}
for product in products:
    print(product, products[product])
print()  

players = {
    "Temple": 12,
    "David": 7,
    "John": 15,
    "Mary": 9
}
for player in players:
    if players[player] >= 10:
        print(player, players[player])
print() 

students = {
    "Grace": 14,
    "Bryan": 6,
    "Sophie": 18,
    "Daniel": 9,
    "Micheal": 12
}
for student in students:
    if students[student] < 10:
        print(student, students[student])
print()    

players = {
    "Temple": 12,
    "David": 7,
    "John": 15,
    "Mary": 9,
    "Alex": 20
}   
for player in players:
    if players[player] >= 10:
        print(player, players[player])
for player in players:
    if players[player] < 10:
        print(player, players[player])
for player in players:
    if players[player] == 15:
        print(player, players[player])
print() 

student_score = {
    "Grace": [4, 9],
    "Bryan": [2, 0, 8],
    "Sophie": [1, 2, 3, 6]
}
for student in student_score:
    for score in student_score[student]:
        print(student, score)
print()      
       
Nerds = {
    "David": [7, 8],
    "Mary": [5, 9, 6],
    "Alex": [10, 4]
}
for name in Nerds:
    for score in Nerds[name]:
        print(name, score)
print() 

Community = {
    "Ada": [12, 5, 8],
    "John": [3, 15],
    "Mike": [9, 7, 11, 4]
}
for member in Community:
    for amount in Community[member]:
        print(member, amount)  
print()
