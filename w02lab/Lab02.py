# 1. Name:
#      Emily McGovern
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      There are usernames and passwords in a json file. This code will read the json file.
#      Then the code will prompt the user to input their username and password, the code will then
#      decide if the user has inputted the correct username and password that matches the username and 
#      password in the json file. If the user inputted the correct username and password then they will
#      be authenticated.
# 4. What was the hardest part? Be as specific as possible.
#      I struggled with this assignment. I have not worked with a json files before. I tried completing this
#      assignment before class, but struggled with having the code read the json file. When I went to class
#      I was able to get an idea on how to open the json file, and then learned that I had to import json to 
#      the code. The next problem I had was figuring out how to find and make the usernames and passwords
#      line up together. After multiple tries, I had a thought to try turning the list into an index. After some
#      trial and error, I was able to make the usernames and passwords match each other. I thought the instructions
#      for this assignment were well written and clear to understand. 
# 5. How long did it take for you to complete the assignment?
#      My total time with completing this assignment was 3 hours and 25 minutes.

# Importing json to code.
import json

# Using 'try' to test if there are any errors with the file.
try:

    # Open Lab02.json and read the data.
    with open("C:/Users/lover/OneDrive/Documents/BYUI/CSE 130/w02lab/Lab02.json", "r") as file:
        text = file.read()
            
        # Convert the string into a JSON object.
        json_data = json.loads(text)

    # Convert the username and password components in JSON object to two lists.
    usernames_data = json_data["username"]
    passwords_data = json_data["password"]

    # Asking user for the password and username.
    user_username = input('\nUsername:')
    user_password = input('Password:')

    # Using 'if' statement to decide if user input matches with json list.
    if user_username in usernames_data and user_password in passwords_data:

        # Using index to find matching index between usernames_data and passwords_data.
        username_index = usernames_data.index(user_username)
        password_index = passwords_data.index(user_password)

        # 'If' statement to decide if indexs match with user input.
        if username_index == password_index:
            print('You are authenticated!')
        else:
            print('You are not authorized to use the system.')

    else:
        print("You are not authorized to use the system.") 

# If the file is not found or there is an error.
except:
    print("\nUnable to open file Lab02.json.\n")