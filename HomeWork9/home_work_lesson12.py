


#завдання 3
def sum_func(a, b):
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