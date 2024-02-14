import datetime as dt

#завдання 1
def add_day_func():
    #subtracts a specified number of days from a date
    year_date = dt.datetime(2023, 5, 3,14,5,6)
    and_date = dt.timedelta(weeks=1, days=10, seconds=4)
    delta_date = dt.timedelta(days=1910)
    result_year_delta = year_date - delta_date
    result_day_delta = and_date - delta_date
    print('Received year data: ', result_year_delta)
    print('Received data of the day: ', result_day_delta)
    if result_year_delta.timestamp() > 0:
        print(True)
    else:
        print(False)
    if result_day_delta.total_seconds() > 0:
        print(True)
    else:
        print(False)

add_day_func()


#завдання 2
def my_birthday():
    #calculate the age and return
    my_date = dt.datetime(1999, 6, 1)
    today = dt.datetime.now()
    days_lived = today - my_date
    time_format_string = '%y-%m-%d %I:%M:%S %p'    #custom date format
    format_date = my_date.strftime(time_format_string)    #assigning a new format
    print('Lived for days: ', days_lived)
    print('Lived for seconds: ', today.timestamp() - my_date.timestamp())
    print('Your date of birth in a custom format: ', format_date)

my_birthday()


#завдання 3
def sum_func(a, b):
    #processing 'FileNotFoundError' exception
    try:
        with open('file.txt') as file_test:
            line_red = file_test.readlines()
            print(line_red)
        return a / b
    except TypeError as ex:
        print('Not supported type')
    except FileNotFoundError as ex:    #added the exception that was not used
        print('Fail, this file has not found')
    except ZeroDivisionError as ex:    #the exception will be triggered if the file is found
        print('You try to divide by zero')
    except Exception as ex:
        print('I`m basic Except')
    finally:
        print('Final block')

sum_func(1, 0)