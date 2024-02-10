import random
#завдання 1
def list_100():
    # Use list comprehension to create a list that
    list_new = [random.randint(0, 99) for _ in range(100) if len(str(random.randint(0, 99))) < 3]
    print(list_new)

list_100()


#завдання 2
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