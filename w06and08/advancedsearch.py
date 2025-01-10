import json

def get_filename():
    return input("What file would you like to look through? ")

def get_name():
    return input("What is the name you are looking for? ")

def load_data(filename):
    try:
        with open(f'C:/Users/lover/OneDrive/Documents/BYUI/CSE 130/w06and08/{filename}', "r") as file:
            return json.load(file)["array"]
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def binary_search(names_list, find_name):
    left, right = 0, len(names_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if names_list[middle] < find_name:
            left = middle + 1
        elif names_list[middle] > find_name:
            right = middle - 1
        else:
            return True
    return False

def main():
    filename = get_filename()
    names_list = load_data(filename)
    if names_list is None:
        return
    find_name = get_name()
    found = binary_search(names_list, find_name)
    if found:
        print(f"I found {find_name} in file {filename}")
    else:
        print(f"I could not find the {find_name} in file {filename}")

if __name__ == "__main__":
    main()