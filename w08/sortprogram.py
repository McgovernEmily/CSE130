# 1. Name:
#      Emily McGovern
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program will read through a file of Json full of names
#      and will then sort them alphabetically. The user will be asked
#      which file they would like to have sorted and the code will then 
#      find that file and sort it alphabetically. 
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was coding out the algorithm for 
#      the sorting process. I ran into trouble with figuring out how to get the    
#      range right on the for loops. I kept running into the problem of the for
#      loops skipping certain names. After awhile of problem solving and trying 
#      different way to fix it, I was able to correct the code. I also had trouble
#      coming up with asserts. In order to get better at coming up with asserts, I need
#      to keep practicing. I will go back to my older code and come up with asserts.
# 5. How long did it take for you to complete the assignment?
#      It took me about 2 hours to complete this assignment.

# Importing json module.
import json

# Asking the user for the file they want to sort.
filename = input("What file would you like to look through? ")

# Opening the file the user chose.
try:
    with open(f'C:/Users/lover/OneDrive/Documents/BYUI/CSE 130/w08/{filename}', "r") as file:
        text_names = file.read()
        json_data = json.loads(text_names)

        # Adding an assert to check if file has array in it.
        assert "array" in json_data, "json_data does not contain 'array'."
        names_list = json_data["array"]

except Exception as no_file:
    print(f"Error loading file: {no_file}")

# Starting the sort algorithm.
def sort_list(names_list):

    # Inputting assert to check if the file is a list.
    assert type(names_list) == list, "names_list is not a list"

    # Getting the length of the list.
    len_list = len(names_list) 

    # Adding an assert to check if there is anything in the list.
    assert len_list >= 0, "len_list has nothing in it"

    # Starting the for loop to go throughout the list.
    for number in range(len_list - 1, 0, - 1):
        i_largest = 0
        for i_number in range(1, number + 1):

            # Seeing if the current item is larger than the largest item found.
            if names_list[i_largest] <= names_list[i_number]:
                i_largest = i_number

        # Implementing the switch in the list.
        names_list[number], names_list[i_largest] = names_list[i_largest], names_list[number]

# Stating the def in order for the code to recognize that names_list is named.
sort_list(names_list)

# Using items as an item to add a tab and a new line after each item.
for items in names_list:

    # Adding assert to check if items is a string.
    assert type(items) == str, "items is not a string"
    print("\t", items)