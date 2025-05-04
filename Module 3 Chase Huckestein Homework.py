#Module 3 Chase Huckestein Homework
#Part 1 - calculate total for the meal
def calculateMealTotal():
    # Get the meal cost from the user
    meal_cost = float(input("Enter the meal cost: "))
    
    # The problem tax percentage is 7%
    tax_percentage = 7/100  
    
    # The tip percentage was given at 18%
    tip_percentage = 18/100 
    
    # Calculate the tax amount
    tax_amount = meal_cost * (tax_percentage)
    
    # Calculate the tip amount
    tip_amount = (meal_cost + tax_amount) * (tip_percentage)
    
    # Calculate the total cost of the meal
    total_cost = meal_cost + tax_amount + tip_amount
    
    # Print the total cost of the meal
    print(f"The total cost of the meal is: ${total_cost:.2f}")
    # print the tax amount
    print(f"The tax amount is: ${tax_amount:.2f}")
    # print the tip amount
    print(f"The tip amount is: ${tip_amount:.2f}")
    return total_cost

calculateMealTotal()

#Part 2 - Calculate the 24 hour time of alarm
def calculateAlarmTime():
    # Get the 24 hour current time from the user
    currentTime = int(input("enter the current time in 24 hour format (HHMM): "))   
    

    # Get the number of hours until the alarm goes off
    hours_til_alarm = int(input("Enter how many hours until the alarm goes off: "))

    # Calculate the alarm time
    alarm_time = (currentTime + hours_til_alarm*100) % 2400

    # Print the new time in 24-hour format
    print(f"The alarm will go off at {alarm_time:02}")

    return alarm_time

calculateAlarmTime()

