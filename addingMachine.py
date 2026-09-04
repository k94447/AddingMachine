# COPYRIGHT 1997 k94447 Inc. DONUT STEEL
print("ADDINGMACHINE v3.0")
print("==================")
print('\n')
def nogimmick():
    try:
        appendage = float(input('Enter a number: '))
    except ValueError:
        print('You must enter a number.')
        return None
    else:
        return appendage
x=[]
opt = 'y'
opt2 = True
appendage = None
while opt == 'y' or opt == 'Y':
	while opt2 == True and appendage == None:
		appendage = nogimmick()
	if appendage <= 0:
		print('You must enter a positive non-zero floating point number.')
		appendage = None
	else:
		x.append(appendage)
		opt = input('Do you want to include a new figure? \n[(Y)es/(N)o][N] ')	# ANNOYING POPUP
		appendage = None
hmset=[]
naturfreq=[]
avg = (sum(x))/len(x)
koefficient = 1
for i in x:
   koefficient *= i
geomord = (koefficient)**(1/len(x))
for j in x:
        hmterm = 1/j
        hmset.append(hmterm)
op2 = 'gamma'
while op2 == 'gamma':
	print('\n')
	print('Supported Operations:')
	print('=====================')
	print('\n')
	print('1. Average (A or a)')
	print('2. Summate (S or s)')
	print('3. Find Geometric Mean (G or g)')
	print('4. Find Harmonic Mean (H or h)')
	print('5. Add/Subtract number to/from sum (M or m)')
	print('6. Show Frequency (F or f)')
	print('7. Add new numbers (N or n)')
	print('8X. Remove data (R or r)')
	print('\n')
	print('Exit program (X or x)')
	print('\n')
	addoravg = input('Enter your choice: ')
	if addoravg == 'S' or addoravg == 's' or addoravg == '2':
		print('The sum is: ', sum(x))
		input('\n(Press Enter to return to selection.)')
	elif addoravg == 'A' or addoravg == 'a' or addoravg == '1':
		for ifnegexists in x:
			if ifnegexists < 0:
				input('One or more negative entries have been found. Remove them, and then try again.\n(Press Enter to return to selection.)')
		else:
			print("The average is: ", avg)
			input('(Press Enter to return to selection.)')
	elif addoravg == 'G' or addoravg == 'g' or addoravg == '3':
		for ifnegexists in x:
			if ifnegexists < 0:
				input('One or more negative entries have been found. Remove them, and then try again.\n(Press Enter to return to selection.)')
		else:
			print("The Geometric Mean is: ",geomord)
			input('(Press Enter to return to selection.)')
	elif addoravg == 'H' or addoravg == 'h' or addoravg == '4':
		for ifnegexists in x:
			if ifnegexists < 0:
				input('One or more negative entries have been found. Remove them, and then try again.\n(Press Enter to return to selection.)')
		else:
			print("The Harmonic Mean is: ",len(x)/sum(hmset))
			input('(Press enter to return to selection.)')
	elif addoravg == 'M' or addoravg == 'm' or addoravg == '5':
		subtr = float(input('(Use positive numbers to add and negative numbers to subtract)\nEnter the number:  '))
		print('The required answer is: ', sum(x)+subtr)
		input('(Press Enter to return to selection.)')
	elif addoravg == 'F' or addoravg == 'f' or addoravg == '6':
		for k in x:
			if k not in naturfreq:
				naturfreq.append(k)
				print('Frequency of ', k, ': ', x.count(k))
		input('(Press Enter to return to selection.)')
	elif addoravg == 'N' or addoravg == 'n' or addoravg == '7':
		opt = 'y'
		appendage = None
		while opt == 'y' or opt == 'Y':
			while opt2 == True and appendage == None:
				appendage = nogimmick()
			if appendage <= 0:
				print("You must enter a postitve non-zero floating point number. Can't you see?")
				appendage = None
			else:
				x.append(appendage)
				opt = input('Do you want to include a new figure?(Y/N)[N]')	# ANNOYING POPUP
				appendage = None
	elif addoravg == 'X' or addoravg == 'x':
		op3 = 'n'
		if op3 == 'n':
			opt = input('Do you REALLY wish to exit? All values will be lost!(Y/N)[N]')
			if opt == 'y' or opt == 'Y':
				import sys
				sys.exit()
	else:
		op2 == 'gamma'
		input("Invalid choice.\n(Press Enter to return to selection.)")
