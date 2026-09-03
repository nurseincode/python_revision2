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

add = lambda x,y: x + y
# is conceptually very similar to:
# def add(x, y):
#     return x + y

# lambda = keyword
# x , y = parameters
# x + y = expression whose result is automatically returned
# the lambda kw tells python to create a function here
# so 
# add = lambda x, y: x + y # creates a func & assigns that func to add
# then add(3, 4) == 7




def add(x, y):
    print(add)

add = lambda x, y: x + y
add(3, 4)








