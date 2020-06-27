def datmoney():
    #Initialize variables
    pennies = int(input('How many pennies do you have? '))
    nickels = int(input('How many nickels do you have? '))
    dimes = int(input('How many dimes do you have? '))
    quarters = int(input('How many quarters do you have? '))
    half_dollars = int(input('How many half dollars do you have? '))
    dollars = int(input('How many dollars do you have? '))
    print('')
    print('********************')
    print('')

    #Print how many of each coin we have
    if pennies > 1:
        print('You have', pennies, 'pennies.')
    if pennies == 1:
        print('You have 1 penny.')
    if nickels > 1:
        print('You have', nickels, 'nickels.')
    if nickels == 1:
        print('You have 1 nickel.')
    if dimes > 1:
        print('You have', dimes, 'dimes.')
    if dimes == 1:
        print('You have 1 dime.')
    if quarters > 1:
        print('You have', quarters, 'quarters.')
    if quarters == 1:
        print('You have 1 quarter.')
    if half_dollars > 1:
        print('You have', half_dollars, 'half dollars.')
    if half_dollars == 1:
        print('You have 1 half dollar.')
    if dollars > 1:
        print('You have', dollars, 'dollars.')
    if dollars == 1:
        print('You have 1 dollar.')

    #Calculate total and convert it to dollars
    total = (pennies) + (5 * nickels) + (10 * dimes) + (25 * quarters) + (50 * half_dollars) + (100 * dollars)
    total = total / 100

    #Print total in dollars
    print('The value of all your coins is: $', end='')
    print(total, end='')
    print('.\n')

    #Keep window open for viewing
    input('Press Enter to Exit...')

datmoney()
