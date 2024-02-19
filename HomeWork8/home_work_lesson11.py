import random

#завдання 1
def show_func(func):
    #calling a function using a decorator
    def inner(*args, **kwargs):    #created a decorator
        print("Function call:", func.__name__)
        return func(*args, **kwargs)
    return inner

@show_func    #added decorator functions
def add_sum(x, y):
    items_sum = x + y
    return items_sum

@show_func
def add_multiplication(x, y):
    items_multiplication = x * y
    return items_multiplication

x = 2
y = 6

result_sum = add_sum(x, y)
result_multiplication = add_multiplication(x, y)
print(f'Your sum is: ', result_sum)
print(f'Your multiplication is: ', result_multiplication)


#завдання 2
def list_100():
    #сreating a list of 100 items, each in the range 0 to 10
    random_numbers = [random.randint(0, 10) for _ in range(100)]

    #сounting the number of each element
    count_dict = {index: count for index, count in enumerate(random_numbers)}
    for index, count in count_dict.items():
        print(f"{index} - {count} pieces")

list_100()