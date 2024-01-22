'''
def name_greeter():
    your_name= input('hi please tell me what`s tour name ')
    print(f'henlo {your_name}')

a = 'sgsrgh'.isdigit()
name_greeter()
name_greeter()
name_greeter()
'''

def new_cool_function(value):
    print(value**2)

new_cool_function(2)

def second_cool_function(value, value2):
    print(value**value2)

second_cool_function(3, 3)

def you_cool_function(value, value2):
    print(value**value2)

you_cool_function(value=4,value2=2)
def print_full_name(first_name, last_name):
    print(f'Full name is {first_name} {last_name}')

print(print_full_name(first_name='Alex', last_name='Shevchenko'))

def my_favorite_language(name, language='Python'):
    print(f'My name is {name}, and my favorite landuage is {language}')

my_favorite_language('Alex', 'Java')
my_favorite_language('Alex')


def mr_sum_two_numbers(first_number=1, second_number=4)->int:
    return first_number+second_number

new_value = mr_sum_two_numbers(124352463, 68567634523)
print(new_value)

def make_pizza(*ingridients):
    for ingr in ingridients:
        print(f'{ingr} is a {ingridients.index(ingr)} number ingridient in pizza cooking')

make_pizza('cheese')
make_pizza('cheese', 'cheese', 'cheese', 'cheese')
make_pizza('pineapple', 'curse')

def dogs(**dog_info):
    for key, value in dog_info.items():
        print(f'{key} : {value}')


def sum_and_diff(first_number, second_number):
    return first_number+second_number, first_number-second_number


if __name__ == '__main__':
    sum_result, diff_result = sum_and_diff(5, 10)
    print(sum_result)
    print(diff_result)

    sum_and_diff_result = sum_and_diff(20, 10)
    print(sum_and_diff_result)
    dogs(first_name='patron', required_amount=1000000, cooler_than='iphon')

    # *args
    # **kwargs

    dog_dict = {'1': 1, '2': 2}
    dog_items = dog_dict.items()
    print()

