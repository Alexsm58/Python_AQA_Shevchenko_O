import re

#Завдання 1
def check_string():
    # сhecking a string for uppercase, lowercase letters, digits, and underscores
    my_string = '1_Ahfg_erjf_rfrerrf_r_rfrfre_eJJJ_JJJJ_0_9'
    pattern = r'^[a-zA-Z0-9_]+$'
    my_regular = re.search(pattern, my_string)   #I used the 'search' function to search throughout the entire string
    print(my_regular)
    if my_regular is not None:
        print(True)
    else:
        print(False)

check_string()


#Завдання 2
def delete_brackets():
    # to remove the content within parentheses, including the parentheses and the domain
    text_with_brackets = ['example (.ua)', 'github (.com)', 'stackoverflow (.com)']
    pattern = [re.sub(r'[(). ]|com|ua', '', items) for items in text_with_brackets]
    print(pattern)
    for item in pattern:    #displayed in a column
        text = item.split()
        print(item)

delete_brackets()


#Завдання 3
def space_after_uppercase():
    #to add a space after uppercase letters
    text = "Alex, Yurii, Gregor, Stefan, HANNA"
    result_text = re.sub(r'([A-Z])', r'\1 ', text)
    print(result_text)

space_after_uppercase()