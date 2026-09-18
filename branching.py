kilowattHours = int(input("Enter the KW hours used: "))

if kilowattHours <= 1000:
    amountOwed = kilowattHours * 0.07633
else:
    amountOwed = (1000 * 0.07633) + ((kilowattHours - 1000) * 0.09259)

print("Amount owed is $" + str(amountOwed))