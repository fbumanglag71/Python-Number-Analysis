## Author: Francisco Bumanglag
## Project: Number Analysis
## Assignment: Module 4 Project 1
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: July 2, 2023



def main():                             #define main function (number analysis)
    numbers = []                        #create empty list to store 20 numbers
                                            
    for i in range(20):                 #for loop and user imputs 20 numbers
        number = float(input(f"Enter number {i + 1}: "))   #show the current iteration # (1-based indexing) of the loop
        numbers.append(number)          #append the number after each loop -- 20 max

    
    lowest = min(numbers)               #find the min number from numbers list
    highest = max(numbers)              #find the max number from numbers list
    total = sum(numbers)                #calc the total of the numbers from numbers list
    average = total / len(numbers)      #calc average based on total and len(numbers)

    print("Lowest number:", lowest)     #display results on console -- min number
    print("Highest number:", highest)   #display results on console -- max number
    print("Total:", total)              #display results on console -- total of numbers
    print("Average:", average)          #display results on console -- average of numbers

main()                                  #call the main function (number analysis)




