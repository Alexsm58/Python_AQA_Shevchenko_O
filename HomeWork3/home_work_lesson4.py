notes = []
while True:
    print('\nКоманди:')
    print('add - Додати нотатку')
    print('earliest - Вивести нотатки в хронологічному порядку (від найстарішої до найновішої)')
    print('latest - Вивести нотатки в хронологічному порядку (від найновішої до найстарішої)')
    print('longest - Вивести нотатки за довжиною (від найдовшої до найкоротшої)')
    print('shortest - Вивести нотатки за довжиною (від найкоротшої до найдовшої)')
    print('Exit - Вихід')
    command = input('Введіть команду: ')
    if command == 'add':
        note_text = input('Введіть текст нотатки: ')
        notes.append(note_text)
        print('Нотатка додана.')
    elif command == 'latest':
        print(notes)
    elif command == 'earliest':
        notes.reverse()
        print(notes)
    elif command == 'longest':
        sorted_list = sorted(notes, reverse=True, key=len)
        print(sorted_list)
    elif command == 'shortest':
        sorted_list = sorted(notes, key=len)
        print(sorted_list)
    elif command == 'Exit' or command == 'exit':
        print('Exit in notes')
        break
    else:
        print('Невідома команда. Спробуйте ще раз.')