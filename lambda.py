#  callback

# def calculate(operation): 
#     print(operation(3, 4))

# # give it a normal function

# def add(x, y):
#     return x + y

# def multiply(x, y):
#     return x * y

# # calculate(add)

# # But what if you only need that tiny function once?

# calculate(lambda x, y: x + y)
# calculate(lambda x, y: x * y)



# def doing_something(callback):
#     print(f'Running first')
#     callback()

# # doing_something(greet)

# # with callback
# doing_something(lambda: print("Hello!"))






# add_this = lambda num: num + 10

# print(add_this(5))

def add_ten(num):
    return num + 10


add_this = lambda num: num + 10

print(add_ten(5))
print(add_this(5))










