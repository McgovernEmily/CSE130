# 1. Name:
#      Emily McGovern
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program is a monopoly decision helper. If the user is trying to purchase a hotel for Pennsylvania Avenue,
#      this code will help the user find the best way possible to purchase a hotel for Pennsylvania Avenue. If the user
#      has a hotel on a green property already, then it will tell the user to swap. If the user does not have a hotel on
#      either of the green properties, then this code will calculate the best possible way to by a hotel for Pennsylvania 
#      Avenue. 
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part of this project was figuring out how to best ask the questions in the best order for the user.
#      Another part that was hard was figuring out how to organizes all the if statements and not going over the limited amount 
#      of words per line. It was tricky at first, but then I was able to figure out one of the possible ways to fix that problem. 
#      Lastly, this project was a little more complicated than the other projects, but I was able to see the value of having a flow
#      chart before you code a project out. I was going to use my flow chart, but I saw that my instructors flow chart was a bit 
#      easier to read and understand. I would have never thought that flow charts would be very useful in coding projects. 
# 5. How long did it take for you to complete the assignment?
#      It took me a total of 4-5 hours in reading and completing this assignment. It was very helpful going over the assignment in class.

# Prompts for asking what is on each property.
pennsylvania_input = ("What is on Pennsylvania Avenue (0:nothing, 1:one house, ... 5:a hotel)? ")
north_carolina_input = ("What is on North Carolina Avenue (0:nothing, 1:one house, ... 5:a hotel)? ")
pacific_input = ("What is on Pacific Avenue (0:nothing, 1:one house, ... 5:a hotel)? ")

# Outputs for swapping properties.
swap_north_carolina = ("Swap North Carolina's hotel with Pennsylvania's 4 houses")
swap_pacific = ("Swap Pacific's hotel with Pennsylvania's 4 houses.")

# Input and output of amount of hotels.
hotels = ("How many hotels are there to purchase? ")
no_hotels = ("There are not enough hotels available for purchase at this time.")

# Input and output for asking the user for amount of cash.
cash = ("How much cash do you have to spend? ")
not_enough_cash = ("You do not have sufficient funds to purchase a hotel at this time.")

# Input and output for asking user for amount of houses.
houses = ("How many houses are there to purchase? ")
no_houses= ("There are not enough houses available for purchase at this time. ")

# User Purchase outputs for Pennsylvania.
return_houses = ("Put 1 hotel on Pennsylvania and return any houses to the bank.")

# Asking if user has all the green properties.
color_group = input("Do you own all the green properties (yes/no)? ")

# Using an if statement to decide if they have all green properties.
if color_group == 'yes':

    # If user has all green properties then prompt what they have on Pennsylvania.
    pennsylvania_housing = int(input(pennsylvania_input))

    # Using an if statement to asking what is on Pennsylvania.
    if pennsylvania_housing <= 4:
        north_carolina_housing = int(input(north_carolina_input))

        # Using an if statement to ask what is on North Carolina.
        if north_carolina_housing <= 4:
            pacific_housing = int(input(pacific_input))

            # Using an if statement to ask what is on Pacific.
            if pacific_housing <= 4:
                hotel_count = int(input(hotels))

                # Using an if statement to ask if there are enough hotels.
                if hotel_count > 0:
                    
                    # Calculating the number of houses need for each property.
                    num_house_pa_need = 4 - pennsylvania_housing
                    num_house_nc_need = 4 - north_carolina_housing
                    num_house_pc_need = 4 - pacific_housing
                    num_house_total_need = num_house_pc_need + num_house_nc_need + num_house_pc_need

                    # Multiplying the number of houses by 200 and then adding 200 for the hotel.
                    total_money_need = num_house_total_need * 200 + 200
                    
                    # Prompting user for amount of cash they have.
                    user_cash = int(input(cash))

                    # Using if statement to determine if they have enough cash.
                    if user_cash >= total_money_need:
                        house_amount = int(input(houses))

                        # Using an if statement to determine if there are enough houses.
                        if house_amount >= num_house_total_need:

                            # Showing the user how much it is going to cost them and how many
                            # houses they are going to need.
                            print(f"This will cost ${total_money_need}")
                            print(f"Purchase 1 hotel and {num_house_total_need} house(s).")
                            print(return_houses)

                            # Showing the user one of the optimal out comes if they need
                            # houses on North Carolina.
                            if num_house_nc_need > 0:
                                 if pacific_housing == 4:
                                     print(f"Put {num_house_nc_need} house(s) on North Carolina.")
                                 else:
                                     print(f"Put {num_house_nc_need} house(s) on North Carolina.")
                                     print(f"Put {num_house_pc_need} house(s) on Pacific.")

                            # Showing the user another one of the optimal out comes if they need
                            # houses on pacific.   
                            elif num_house_pa_need > 0:
                                if north_carolina_housing == 4:
                                    print(f"Put {num_house_pa_need} house(s) on Pacific.")
                                else:
                                     print(f"Put {num_house_nc_need} house(s) on North Carolina.")
                                     print(f"Put {num_house_pc_need} house(s) on Pacific.")
                               
                        else:
                            print(no_houses)

                    else:
                        print(not_enough_cash)

                elif hotel_count < 0:
                    print(no_hotels)

            elif pacific_housing == 5:
                print(swap_pacific)

        elif north_carolina_housing == 5:
            print(swap_north_carolina)


    elif pennsylvania_housing == 5:
        print("You cannot purchase a hotel if the property already has one.")

elif color_group == 'no':
    print('You cannot purchase a hotel until you own all the properties of a given color group.')