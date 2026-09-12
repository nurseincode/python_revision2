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

# def square(n):
#     return n * n

# def cube(n):
#     return n ** 3
# Main
# print(with_list(numbers, square))
# print(with_list(numbers, cube))


# Map
# print(list(map(square, numbers)))
# print(list(map(cube, numbers)))

# Lambda

# print(list(map(lambda x: x ** 2, numbers)))



    

# people = [
#     ("Mary", 30),
#     ("Tom", 20),
#     ("Alice", 25)
# ]

# sorted(people, key=lambda person: person[1])

# filter

# numbers = [2, 3, 5, 8, 12, 7]

# evens = filter(lambda x: x % 2 == 0, numbers)
# print(list(evens))

# or

# print(list(filter(lambda x: x % 2 == 0, numbers)))


# filter and map together

# numbers = [4, 7, 3, 8, 10]

# evens = filter(lambda x: x % 2 == 0, numbers)

# result = map(lambda x: x * 2, evens )

# print(list(result))



# using map to open a file called numbers.txt

# - 4 
# - 7 
# - 3 

# with open("numbers.txt") as file:
#     result = map(int, file)
#     print(list,(result)) 

#     for number in result:
#         print(number * 2)

# you have a file called numbers.txt that contains 4, 2, 5, 6, 8



# hof and cb 

numbers = [1, 2, 3, 4]

def double(x):
    return x * 2


result = map(double, numbers) # map is a hof bc it takes another func as an argument
print(list(result))

# hof returns another function

def create_multiplier(x):

    def multiply(number):
        return number * x
    return multiply

double = create_multiplier(2)
print(double(5))



