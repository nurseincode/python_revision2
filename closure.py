# Closure
# a function that returns another function
# The returned function retains a copy of the scope of the outer function

# def create_multiplier(x):
    
#     def multiply(number):
#           return number * x
#     return multiply

# double = create_multiplier(2)
# print(double(5))

# def greet(name):
#     print('Hello')

#     def display_name():
#         print(name)
#     return display_name

# spam = greet('Dee')
# spam()

# functions that apply different taxes 

# def create_tax_calculator(tax_rate):

#     def calculate(price):
#         return price * (1 + tax_rate)
#     return calculate

# gst = create_tax_calculator(0.10)
# luxury_tax = create_tax_calculator(0.20)

# print(gst(100)) # 110.0
# print(luxury_tax(100)) # 120.0

# keeping track of number of times a button is clicked

def create_click_tracker(button_name):
    clicks = 0

    def track_click():
        nonlocal clicks
        clicks += 1
        print(f'{button_name} clicked {clicks} times')
    return track_click

login_tracker = create_click_tracker('Login')
download_tracker = create_click_tracker('Download')

login_tracker()
login_tracker()
download_tracker()
login_tracker()

     



  

