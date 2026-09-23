def greet():
    print("Hello, Temple")
greet()

def welcome(name):
    print("welcome", name)
welcome("Christian")

def add_numbers(a, z):
    print(a + z)
add_numbers(10, 5) 

def multiply(a, b):
    return(a * b)
returned = multiply(6, 4)  
print(returned)

def square(king):
    return(king * king)
square(7)
returned = square(7)
print(returned)

def add(linus, ubuntu):
    return(linus + ubuntu)    
returned_result = add(10, 20)
print(returned_result)

def substract(micro, daemon):
    return(micro - daemon)
answer = substract(20, 8)
print(answer)  

def introduce(name, age, country):
    print(name, age, country)
    print("My name is", name, "I am", age, "years old", "and I am from", country)
introduce("David", 25, "Ghana")
introduce("Sarah", 22, "Kenya") 

def describe(name, hobby):
    print(name, "likes", hobby)
describe("David", "coding") 

def add_numbers(a, b):
    print(a + b)
add_numbers(600, 400) 

def greet(name):
    print("Hello", name)
greet("Christian")    

def country(name= "nigeria"):
    print("I am from", name)
country()

def country(name= "nigeria"):
    print("I am from", name)
country("Ghana")    

def greet(name= "Christian"):
    print("Hello", name)
greet()
greet("David")  

def student(name, course):
    print(name, course)
student(name= "Christian", course="python")

def introduce(name, age, country):
    print(name, age, country)
introduce("Christian", age= 20, country= "Nigeria")

def introduce(name, age, country="Nigeria"):
    print(name, age, country)
introduce("Temple", 79,)

def student_info(name, age, course):
    print(name, age, course)
student_info(name= "Temple", course= "computer", age= 20)    

def show_names(*args):
    print(args[0])
show_names("Temple", "Grace", "Bryan") 


def show_names(*args):
    print(args[1])
show_names("Temple", "Grace", "Bryan")

def show_names(*args):
    for name in args:
        print(name)
show_names("Temple", "Grace", "Bryan")

def show_scores(*args):
    for value in args:
        if value >= 50:
             print(value)
show_scores(35, 72, 48, 90, 61)

def calculate(*args):
    for value in args:
        if value > 100:
            print(value)
calculate(50, 150, 80, 200, 120)

def student(**Kwargs):
    print(Kwargs)
student(name= "Christian", age= 20) 

def student(**Kwargs):
    print(Kwargs)
student(name= "Christian", age= 20, course= "Python")

def show_info(**Kwargs):
    for item in Kwargs:
        print(item)
show_info(name= "Christian", age= 20, country= "Nigeria")

def show_info(**Kwargs):
    for key, value in Kwargs.items():
        print(key, value)
show_info(name= "Christian", age= 20, country= "Nigeria") 

def student_profile(**Kwargs):
    for key, value in Kwargs.items():
        if key == "age":
            print("Age:", 20)
        else:
             print(key, value)
student_profile(name= "Christian", age= 20, country= "Nigeria", course= "Python")  

def greet():
    print("Hello Christian")
def start():
    greet()
    print("Let's start Python")
start()    

def greet(name):
    print("Hello", name)
def welcome(name):
    greet(name)
    print("welcome to Python")
welcome("Christian")        

def welcome():
    print("Welcome to Python")
def greet():
    print("Hello Christian")
    welcome()
def start():
    greet()
start()            