# higher-order functions
# Wrapper

# def greet(name):
#     print(f"Hello, {name}")

# def do_something(callback):
#     callback("Mary")

# do_something(greet)


# def calculate(operation):
#     return(operation(10, 5))

# def add(x, y):
#     return(x + y)

# def multiply(x, y):
#     return(x * y)

# print(calculate(add))
# print(calculate(multiply))

# def my_callback(text):
#     print("Callback says:", text)
    
# def process_data(callback_func):
#     print("Processing task...")
#     callback_func("Hello from inside!")

# Pass the function as an argument
# process_data(my_callback)





# def create_greeting():

#     def greet():
#         print('hello')
#     return greet

# my_function = create_greeting()
# my_function()

# def greet(name):
#     print(f'Hello, {name}')

# def do_something(callback):
#     callback('Mary')

# do_something(greet)

#  A list of numbers

numbers = [10, 25, 30, 40]

# def squares(nums):
#     result = []
#     for n in nums:
#         result.append(n ** 2)

# Builds a new list with the result of 
# calling cb on each item in the list

# def with_list(nums, cb):
#     result = []
#     for n in nums:
#         result.append(cb(n))

#     return result

def square(n):
    return n * n

def cube(n):
    return n ** 3
# Main
# print(with_list(numbers, square))
# print(with_list(numbers, cube))


# Map
# print(list(map(square, numbers)))
# print(list(map(cube, numbers)))

# Lambda

print(list(map(lambda x: x ** 2, numbers)))



    

# people = [
#     ("Mary", 30),
#     ("Tom", 20),
#     ("Alice", 25)
# ]

# sorted(people, key=lambda person: person[1])




