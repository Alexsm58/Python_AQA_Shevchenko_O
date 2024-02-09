import re

#завдання 2
def domains():
    #get domain names in column, don't display dots
    domains_file = open('domains.txt', 'r')
    domain_name_read = domains_file.readlines()
    print(domain_name_read)
    domains_file.close()
    pattern = [re.sub(r'[.\n]', '', items) for items in domain_name_read]   #remove the dots
    for item in pattern:    #displayed in a column
        text = item.split()
        print(item)

domains()