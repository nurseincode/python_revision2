# higher-order functions

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

def greet(name):
    print(f'Hello, {name}')

def do_something(callback):
    callback('Mary')

do_something(greet)


    




