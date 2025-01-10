# 1. Name:
#      Emily McGovern
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program will take two dates that are not the same
#      and calculate the days in between them. The years need to be before
#      1753. The program will also account for leap years. It will go through 
#      each month and calculate the number of days in the months. It will also
#      calculate the number of years and how many days are in a year. Then
#      it will decide if it needs to be added or subtracted to get the total
#      days between the two dates.
# 4. What was the hardest part? Be as specific as possible.
#      I felt like this assignment was pretty simple after we 
#      created pseudocode and did a ton of traces. I felt like once
#      I understood what the pseudocode was doing I was able to easily
#      convert it to python. I did have a bit of trouble in the amount_of_days_in_year
#      function. While I was following along with the pseudocode and converting it
#      to python I accidentally put if year == is_leap. This caused the program not
#      to account the 366 days for a leap year. I kept getting a day short in my 
#      final output. Thankfully after looking through my code multiple times I
#      found that it needed to be if is_leap(year). I also struggled coming up
#      with good asserts. I will say the assert I made in the elif start_year != end_year. Before
#      I did not have elif I had an else statement and then an assert that was start_year != end_year.
#      The assert popped up when I tried to do an input that included same year and month. It helped me
#      fix my code so that else statement does add more days than needs to.
# 5. How long did it take for you to complete the assignment?
#      Took me about an two hours.

def is_leap(year):
    """
    Checks if a year is a leap year.
    Parameters:
        year: The year to check.
    Returns: True if the year is a leap year, False otherwise.
    """
    # Making sure the year is an integer and greater than 1753.
    assert type(year) == int
    assert year > 1753

    # Calculating the leap year.
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def amount_days_in_month(month, year): 
    """
    Finds the amount of days in each month.
    Parameters:
        month: Which month is in a year.
        year: Checking if the year is a leap year.
    Returns: the number of days in the month.
    """
    # Making sure month and year are integers.
    assert type(month and year) == int

    # Making sure the month is bigger than 1 and less than or equal to 12.
    assert 1 <= month <= 12
    assert year > 1753 

    # Looking through the months and figuring out where they go.
    if month in [4, 6, 9, 11]:
        return 30 
    elif month == 2: 

        # Using is_leap to make sure that month has 29 days.
        if is_leap(year): 
            return 29 
        else: 
            return 28 
    else: 
        return 31 
    
def amount_of_days_in_year(year): 
    """
    Finds the amount of days in a year.
    Args:
        year: The year to check.
    Returns: The amount of days in a year.
    """
    # Making sure the year is an integer and greater than 1753.
    assert year > 1753
    assert type(year) == int

    # Finding if the year is 366 days or 365 days.
    if is_leap(year): 
        return 366 
    else:
        return 365

# The main function that will calculate and output info.
def main():

    # Stating the total days starting at 0.
    total_days = 0

    # Stating that the start_year_loop is false to start the while loop.
    start_year_loop = False

    # The inputs from the user for start year, month, and day.
    while start_year_loop != True:
        start_year = int(input("Please enter a start year: "))

        # Using an if statement to repeat through the while loop.
        if start_year < 1753:
            start_year_loop = False
            print("\nPlease enter a date before 1753")
        else:
            start_year_loop = True

    # Stating that the start_month_loop is false to start the while loop.        
    start_month_loop = False
    while start_month_loop != True:
        start_month = int(input("Please enter a start month: "))

        # Using an if statement to repeat through the while loop.
        if start_month > 12:
            print("\nThere are not more than 12 months in a year. Please try again.")
            start_month_loop = False
        elif start_month < 1:
            print("\nThere are not negative or 0 months in a year. Please try again.")
            start_month_loop = False
        else:
            start_month_loop = True

    # Stating that the start_day_loop is false to start the while loop.
    start_day_loop = False
    while start_day_loop != True:       
        start_day = int(input("Please enter a start day: "))

        # Using an if statement to repeat through the while loop.
        if start_day > 31:
            print("\nThere are not more than 31 days in a month.")
            start_day_loop = False
        elif start_day < 1:
            print("\nThere are not negative or 0 days in a month. Please try again.")
            start_day = False
        else:
            start_day_loop = True

    # The inputs from the user for end year, month, and day.
    # Stating that the end_year_loop is false to start the while loop.
    end_year_loop = False
    while end_year_loop != True:
        end_year = int(input("Please enter an end year: "))

        # Using an if statement to repeat through the while loop.
        if start_year > end_year:
            print("\nstart_year must be before end_year")
            end_year_loop = False
        else:
            end_year_loop = True

    # Stating that the end_month_loop is false to start the while loop.
    end_month_loop = False
    while end_month_loop != True:
        end_month = int(input("Please enter an end month: "))

        # Using an if statement to repeat through the while loop.
        if end_month > 12:
            print("\nThere are not more than 12 months in a year.")
            end_month_loop = False
        elif end_month < 1:
            print("\nThere are not negative or 0 months in a year. Please try again.")
            end_month = False
        else:
            end_month_loop = True
    
    # Stating that the end_day_loop is false to start the while loop.
    end_day_loop = False
    while end_day_loop != True:
        end_day = int(input("Please enter an end day: "))

        # Using an if statement to repeat through the while loop.
        if end_day > 31:
            print("There are not more than 31 days in a month.")
            end_day_loop = False
        elif end_day < 1:
            print("\nThere are not negative or 0 days in a month. Please try again.")
            end_day = False
        else:
            end_day_loop = True

    # Asserts to make sure the type is correct for both start and end date.
    assert type(end_day and end_month and end_year) == int
    assert type(start_day and start_month and start_year) == int
    assert start_year and start_day and start_month > 0
    assert end_year and end_day and end_month > 0


    # All error messages if the user inputs something wrong.
    if start_year > end_year:
        raise Exception("The end date needs to be higher than start date.")
    if end_year == start_year and end_month < start_month:
        raise Exception("End month needs to be higher than start month.")
    if end_year == start_year and end_month == start_month:
        if end_day <= start_day:
           raise Exception("End day needs to be higher than start day.")
        else:

            # Finding the total days if the dates have same month and year.
            total_days = end_day - start_day
            assert total_days > 0

    # Calculating the days in between if the years are the same.
    if start_year == end_year and end_month != start_month:
        total_days = amount_days_in_month(start_month, start_year) - start_day

        # Going through the months in between start day and end day.
        for month in range(start_month + 1, end_month):
            total_days += amount_days_in_month(month, start_year)

        # Adding the end day to the total days.
        total_days += end_day

        # checking to make sure total_days is not a negative.
        assert total_days > 0
   
    # Calculating the days in between if the years are not the same. 
    elif start_year != end_year:

        # Making sure it's not adding this if year and months are same.
        assert start_year != end_year

        total_days = amount_days_in_month(start_month, start_year) - start_day

        # checking to make sure total_days is not a negative.
        assert total_days > 0

        # Going through the months from start date to the end of start date year.
        for month in range(start_month + 1, 13):
            total_days += amount_days_in_month(month, start_year)
            assert total_days > 0

        # Going through the years between start date and end date.
        for year in range(start_year + 1, end_year):
            total_days += amount_of_days_in_year(year)
            assert total_days > 0

        # Going through the months of the end date from start of end year to end date day.
        for month in range(1, end_month):
            total_days += amount_days_in_month(month, end_year)
            assert total_days > 0

        # Adding the end date day to the total of days.
        total_days += end_day

    # Outputting the total amount of days between the start and end dates.
    print(f"Total days between the start date and end date: {total_days}")

main()
