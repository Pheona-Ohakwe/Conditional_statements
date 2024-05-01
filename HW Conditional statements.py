 push  ocd# QUESTION 1 DECISIONS AT CROSSROADS


#Task 1: Code Correction

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    number < 0
    print("The number is negative.")

#========================2. The Greatest Showdown==========================

#Task 1.

input_number_first = int(input("Enter random number "))
input_number_second = int(input("Enter another random number "))
input_number_third = int(input("Enter a third random number "))

if input_number_first < input_number_second > input_number_third:
   print("The largest number is ", input_number_second) 
elif input_number_second < input_number_first >  input_number_third:
   print("The largest number is", input_number_first) 
else: 
    input_number_second < input_number_third > input_number_first
    print("The largest number is", input_number_third)
if input_number_third > input_number_first < input_number_second:
    print("The smallest number is",input_number_first )
elif input_number_first > input_number_second < input_number_third:
    print("The smallest number is",input_number_second )
else:
    input_number_second > input_number_third > input_number_first
    print("The smallest number is", input_number_third)