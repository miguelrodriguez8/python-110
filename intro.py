
def test():
    print('Im a function')

def separator():
    print("---------------")


print("Hello Python")

# variables
name = 'Miguel'
last = "Rodriguez"
age = 44
found = False
total = 23.43
products = []

print(name)
print(name + " " + last)

print(age + age)
print(name + str(age))

separator()

# math operations
print(age - 10)
print(age + 10)
print(age * 10)
print(age / 2)
print(age - 2) 
print(age % 2) #mod operator

separator()

# if statements
if(age < 80):
    print('You are still young!')
    print('something else')
elif(age == 80):
    print('you are on the border line')    
else:
    print('Sorry your ass is old:( ')    