import datetime as dt

#завдання 1
def add_day_func():
    year_date = dt.datetime(2023, 5, 3,14,5,6)
    and_date = dt.timedelta(weeks=7, days=10, seconds=4)
    delta_date = dt.timedelta(days=3)
    result_year_delta = year_date - delta_date
    result_day_delta = and_date - delta_date
    print(result_year_delta)
    print(result_day_delta)
    if result_year_delta < 0 or result_day_delta < 0:
        print(True)
    else:
        print(False)
add_day_func()

'''def add_day_func():
    year_date = dt.datetime(2023, 5, 3)
    and_date = dt.timedelta(weeks=7, days=10)
    delta_date = dt.timedelta(days=3)
    result_year_delta = year_date - delta_date
    result_day_delta = and_date - delta_date
    print(result_year_delta)
    print(result_day_delta)

add_day_func()'''


'''    if i in result_day_delta >= 0:
        print(True)
    else:
        print(False)'''

#завдання 2
'''def birthday_day():
    print(dt.date(year=2011,month=1,day=23))
    #print(dt.datetime.now())
    today = dt.datetime.now()
    my_birthday = dt.datetime(year=1989,month=6,day=1)
    print(today)
    print(my_birthday)
    return today - my_birthday
birthday_day()'''

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