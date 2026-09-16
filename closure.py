# Closure
# a function that returns another function
# The returned function retains a copy of the scope of the outer function

# def create_multiplier(x):
    
#     def multiply(number):
#           return number * x
#     return multiply

# double = create_multiplier(2)
# print(double(5))

def greet(name): 
    print('Hello')

    def display_name():
        print(name)
    return display_name

spam = greet('Dee')

     



  

