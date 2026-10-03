try:
    number = int(input("Enter number: "))
except:
    print("invalid input")
print("number accepeted")

try:
    number = int(input("Enter number: "))
except ValueError:
    print("invalid number")
print("program finished")   

try:
    number = int(input("Enter number: "))
except ValueError:
    print("invalid number")   
else:
    print("number accepted")   

try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid number")
else:
    print("Number accepted")
finally:
    print("program complete")  

age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age must be 18 or older")
else:
    print("Age accepted")
