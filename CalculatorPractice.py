# This calculator is created by Phusit Haengphosakul
# This is an attempt to create a continuous calculator that may require the use of the previous answer for the next calculation

###Def DoOperation recognizes the operator and then do the operation that the user desire
def DoOperation(FirstValue, SecondValue, Operator):
	if Operator == 1:
		Answer = int(input1)+int(input2)
		return Answer
		
	elif Operator == 2:
		Answer = int(input1)-int(input2)
		return Answer

	elif Operator == 3:
		Answer = int(input1)*int(input2)
		return Answer

	elif Operator == 4:
		if input2 == '0':
			print('Value of input2 cannot be 0 with this Operator')
			return
		Answer = int(input1)/int(input2)
		return Answer
		
###Value to be printed
x = 0
SavedValue = 0
i = 0
Reset = 'W'
print('F to quit / R to reset values')

###Under while in case the user would like to continue their usage
while(True):
	###Check if Reset
	if Reset == 'R':
		i = 0
		SavedValue = 0
		Reset = 'W'
	### Check if this is first run
	if i == 0:
		input1 = input('First value:')
		###Makes sure to skip this step if there is SavedValue
		i = 1
	###Check if user would like to quit
	if input1 == 'F':
		quit()	
	###Takes Operator
	Operator = int(input('Operator(1:+, 2:-, 3:*, 4:/):'))
	###Check if user would like to quit
	if Operator == 'F':
		quit()
	input2 = input('Second value:')
	###Final check if user would like to quit
	if input1 == 'F' or input2 == 'F' or Operator == 'F':
		quit()
	###Use the Def DoOperation
	else:
		SavedValue = DoOperation(input1, input2, Operator)
		input1 = SavedValue
		print SavedValue
	###While loop for the user to continue with their previous answer(might not require)
"""	while(true):
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
"""
