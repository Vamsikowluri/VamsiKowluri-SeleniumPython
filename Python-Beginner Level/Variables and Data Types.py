#Variable assignment#
age = 30
first_name = "Vamsi"
Is_active = False
_user_id = 126
price = 19.99

#multiple assign
a, b, c = 1, 2, 3

#changing variables
x = 10
x = "Ten"

#addition
a = 5
b = 3
sum = a + b

##Variable Scope
global_var = "I am global"
def my_function():
    print(global_var)
my_function()
#Limited to the block of function - local# Accessible throughout the module - global
def another_function():
    local_var = "I am local"
    print(global_var)
    print(local_var)

another_function()

############Data Types#################
x = 10 #Integers
y = -5
a = 3.14 #Floats
b = -0.001
c = 2 + 3j #Complex Numbers
name = "Alice" #String
greeting = 'Hello, World!'
fruits = ["apple", "banana", "cherry"] #Lists
numbers = [1, 2, 3, 4.5]
coordinates = (10, 20)  #Tuples
person = ("Alice", 30)
student = {              #Dictionaries
    "name": "Vamsi",
    "age": 21,
    "courses": ["Math", "Science"]}
unique_numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4} #Sets
frozen_set = frozenset([1, 2, 3, 3, 4])  # frozenset({1, 2, 3, 4})
is_active = True  #Boolean Type
is_complete = False
