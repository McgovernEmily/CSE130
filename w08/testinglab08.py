import json

# Asking the user for the file they want to sort.
filename = input("What file would you like to look through? ")

try:
    # Opening the file the user chose.
    with open(f'C:/Users/lover/OneDrive/Documents/BYUI/CSE 130/w08/{filename}', "r") as file:
        text_names = file.read()
        json_data = json.loads(text_names)
        names_list = json_data["array"]
        
        # Starting the sort algorithm.
        def sort_list(names_list):
            len_list = len(names_list)
            for number in range(len_list - 1, 0, -1):
                i_largest = 0
                for i_number in range(1, number + 1):
                    if names_list[i_largest] <= names_list[i_number]:
                        i_largest = i_number
                names_list[number], names_list[i_largest] = names_list[i_largest], names_list[number]

        sort_list(names_list)
        print(names_list)

except Exception as no_file:
    print(f"Error loading file: {no_file}")