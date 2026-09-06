import time
import asyncio

# advanced functions
# 1. Callbacks

# def greet():
#     print(f'Hello!')


# def doing_something(callback):
#     print(f'Running first')
#     callback()

# doing_something(greet)

def greet(name, cb):
    print(f'Hello, {name}')
    cb(name)

def say_bye(name):
    print('bye!')
    

def shout(name):
    for i in range(5):
        print('Goodbye!!!')
    

greet('Tim', say_bye)
greet('Gee', shout)

print('continuing main')

# more statements




# def task_one():
#     print("Task one started")
#     time.sleep(3)
#     print("Task one finished")


# def task_two():
#     print("Task two started")
#     time.sleep(2)
#     print("Task two finished")


# task_one()
# task_two()





# async def task_one():
#     print("Task one started")
#     await asyncio.sleep(3)
#     print("Task one finished")


# async def task_two():
#     print("Task two started")
#     await asyncio.sleep(2)
#     print("Task two finished")


# async def main():

#     start = time.time()

#     await asyncio.gather(
#         task_one(),
#         task_two()
#     )

#     end = time.time()

#     print(f"Total time: {end - start:.2f} seconds")


# asyncio.run(main())



