# COPYRIGHT 1922 K94447 CORPS - DONUT STEEL OR ELSE YOU WILL FACE THE WRATH OF JUSTICE
print("ADDINGMACHINE v1.0")
print("==================")
print('\n')
x=[]
hmset=[]
opt = 'y'
while opt == 'y' or opt == 'Y':
	appendage = float(input('Enter a number:'))
	if appendage >= 0:
		x.append(appendage)
		opt = input('Do you want to include a new figure?(Y/N)')	# ANNOYING POPUP
	else:
		input('You cannot enter a negative number.\n(Press enter to start over.)')
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
	print('Supported Operations:')
	print('=====================')
	print('\n')
	print('1. Average (A or a)')
	print('2. Summate (S or s)')
	print('3. Find Geometric Mean (G or g)')
	print('4. Find Harmonic Mean (H or h)')
	print('5. Subtract from sum (- or m)')
	print('6. Add to sum (p or plus)')
	print('\n')
	addoravg = input('Enter your choice: ')
	if addoravg == 'S' or addoravg == 's' or addoravg == '1':
		print('The sum is: ', sum(x))
		input('(Press Enter to exit.)')
		break
	elif addoravg == 'A' or addoravg == 'a' or addoravg == '2':
		print("The average is: ", avg)
		input('(Press Enter to exit.)')
		break
	elif addoravg == 'G' or addoravg == 'g' or addoravg == '3':
		print("The Geometric Mean is: ",geomord)
		input('(Press Enter to exit.)')
		break
	elif addoravg == 'H' or addoravg == 'h' or addoravg == '4':
		print("The Harmonic Mean is: ",len(x)/sum(hmset))
		input('(Press enter to exit.)')
		break
	elif addoravg == '-' or addoravg == 'm' or addoravg == '5':
		subtr = int(input('Enter the number you want to subtract from the sum: '))
		if subtr < 0 :
			input('You cannot subtract negative numbers from the sum.\n(Press Enter to return to selection.)')
		else:
			print('The required answer is: ', sum(x)-subtr)
			input('(Press Enter to exit.)')
			break
	elif addoravg == 'plus' or addoravg == '+' or addoravg == '6':
		addition = int(input('Enter the number you want to add to the sum: '))
		if addition < 0:
			input('You cannot add negative numbers to the sum.\n(Press Enter to return to selection.)')
		else:
			print('The required answer is: ', sum(x)+addition)
			input('(Press Enter to exit.)')
			break
	else:
		op2 == 'gamma'
		input("Invalid choice.\n(Press Enter to return to selection.)")
