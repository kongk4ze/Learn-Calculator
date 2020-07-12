# This calculator is created by Phusit Haengphosakul
# This is an attempt to create a continuous calculator that may require the use of the previous answer for the next calculation

###Def DoOperation recognizes the operator and then do the operation that the user desire
def DoOperation(FirstValue, SecondValue, Operator):
	if Operator == '+':
		Answer = int(input1)+int(input2)
		Answer = x
		
	elif Operator == '-':
		Answer = int(input1)-int(input2)
		Answer = x

	elif Operator == '*':
		Answer = int(input1)*int(input2)
		Answer = x

	elif Operator == '/':
		if input2 == '0':
			print('Value of input2 cannot be 0 with this Operator')
			quit()
		Answer = int(input1)/int(input2)
		Answer = x
		
###Value to be printed
SavedValue = x
print('To quit at anypoint of this program, Enter F'/n)
###Value input1 is outside in case of a continue, if the user quit the program this will come into use again
input1 = input('First value:')
###Check if user would like to quit
if input1 == 'F':
	quit()
###Under while in case the user would like to continue their usage
while(true):
	Operator = input('Operator(+,-,*,/)')
	###Check if user would like to quit
	if Operator == 'F':
		quit()
	input2 = input('Second value:')
	###Final check if user would like to quit
	if input1 == 'F' or input2 == 'F' or Operator == 'F':
		quit()
	###Use the Def DoOperation
	else:
		DoOperation(input1, input2, Operator)
		print x
	###While loop for the user to continue with their previous answer
	while(true):
		Operator = input('To continue using the last value input an operator or choose a number to continue using the calculator:')
		###Check if user wants to quit
		if Operator == 'F':
			quit()
		###Check if user wants to start over with new numbers, this bring the user back to the original while loop
		if type(Operator) == int:
			input1 = Operator
			break
		input2 = input('Second value:')
		###Check if the user wants to quit before doing the operation
		if input1 == 'F' or input2 == 'F' or Operator == 'F':
			quit()
		else:
			DoOperation(x, input2, Operator)
			print x

