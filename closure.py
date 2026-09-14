# Closure
# a function that returns another function

def create_multiplier(x):

    def multiply(number):
        return number * x
    return multiply

double = create_multiplier(2)
print(double(5))
