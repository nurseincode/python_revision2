def greet(name, cb):
    print(f'Hello, {name}')
    cb()

# def say_bye():
#     print('bye!')
    
# say_bye = lambda: print('bye!!')
# greet('Dee', say_bye)

# refine the lambda further


greet('Dee', lambda: print('bye!!'))









