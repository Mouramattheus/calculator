def welcome():
    print('''
Welcome to Calculator
''')
...
# Don’t forget to call the function
welcome()


# Define our function
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')



number_1 = int  (input('Enter your first number here:'))
number_2 = int  (input('Enter your second number here:'))


#adição
if operation == '+':
 print('{} + {} = '.format(number_1, number_2))
 print(number_1 + number_2)

#subtração
elif operation == '-':
 print('{} - {} = '.format(number_1, number_2))
 print(number_1 - number_2)

#multiplicação
elif operation == '*':
 print('{} * {} = '.format(number_1, number_2))
 print(number_1 * number_2)

#divisão
elif operation == '/':
 print('{} / {} = '.format(number_1, number_2))
 print(number_1 / number_2)

else:
 print('You have not typed a valid operator, please run the program again.')

 #add again()function to calculate function
 again()


#Define again () function to task user if they want to use the calculator again
def again():

	# take input from user
	calc_again = input('''
		Do you want to calculate again ?
		Please type Y for YES or N for NO.''')

	#if user type y run the calculate () function
	if calc_again.upper() == 'y':
	   calculate()

	#if user type N say "good bye"to the user and end the program
	elif calc_again.upper() == 'N':
		print("see you later.")


	#if user types another key, run the function again 
	else:
		again()

	#Call calculate() outside of the function
	calculate()