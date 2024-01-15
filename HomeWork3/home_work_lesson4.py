notes = []
while True:
        print("\nКоманди:")
        print("add - Додати нотатку")
        print("earliest - Вивести нотатки в хронологічному порядку (від найстарішої до найновішої)")
        print("latest - Вивести нотатки в хронологічному порядку (від найновішої до найстарішої)")
        print("longest - Вивести нотатки за довжиною (від найдовшої до найкоротшої)")
        print("shortest - Вивести нотатки за довжиною (від найкоротшої до найдовшої)")
        print("Exit - Вихід")

        command = input("Введіть команду: ")

        if command == "add":
            note_text = input("Введіть текст нотатки: ")
            #notes_manager.add_note({"timestamp": len(notes_manager.notes) + 1, "text": note_text})
            notes.append(note_text)
            print("Нотатка додана.")
        elif command == "earliest":
            print(sorted(notes))

        elif command == "latest":
            print(sorted(notes, reverse=True))

        elif command == "longest":
            sorted_list = sorted(notes, reverse=True, key=len)
            print(sorted_list)

        elif command == "shortest":
            sorted_list = sorted(notes, key=len)
            print(sorted_list)

        elif command == "Exit":
            print('Exit in notes')
            break

        else:
            print("Невідома команда. Спробуйте ще раз.")

