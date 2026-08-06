# COPYRIGHT 1922 K94447 - DONUT STEEL OR ELSE YOU WILL FACE THE WRATH OF JUSTICE
print("ADDINGMACHINE v1.0")
print("==================")
print('\n')
x=[]
opt = 'y'
while opt == 'y' or opt == 'Y':
        appendage = float(input('Enter a number:'))
        if appendage >= 0:
                x.append(appendage)
                opt = input('Do you want to include a new figure?(Y/N)')        # ANNOYING POPUP
        else:
                input('You cannot enter a negative number.\n(Press enter to start over.)')
avg = (sum(x))/len(x)
op2 = 'gamma'
while op2 == 'gamma':
        addoravg = input('Do you wish to summate or find the average(S/A)')
        if addoravg == 'S' or addoravg == 's':
                print('The sum is:', sum(x))
                input('(Press enter to exit.)')
                break
        elif addoravg == 'A' or addoravg == 'a':
                print("The average is:", avg)
                input('(Press enter to exit.)')
                break
        else:
                op2 == 'gamma'
                print("Invalid choice.")
          
