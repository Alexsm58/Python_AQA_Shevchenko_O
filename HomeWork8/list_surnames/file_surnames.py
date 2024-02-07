#завдання 3
def users_data():
    #display user names
    parameters_user_name = []
    with open('names.txt', 'w') as user_names:
        user_names.writelines('1,Shevcenko,USA\n2,Babich,Ukraine\n3,,Canada')
    with open('names.txt', 'r') as user_names:
        for item in user_names:
            if len(item) > 0:
                parameters_user_name.append(item.split(',')[1])  #add name in list[]

    return parameters_user_name

print(users_data())

user_names_list = users_data()
for user in user_names_list:
    print(user)