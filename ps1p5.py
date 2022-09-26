#comment input
A = float(input("Please enter the amount of an item purchased"))

#process phase
tax = (A/100) * 7
Total = A + tax

#output
print ("Your tax to be 7% is", tax)
print ("Your total of purchase is", Total)
