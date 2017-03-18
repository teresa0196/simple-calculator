print "Hi! This is a simple calculator.\nYou need to type two numbers.\n" # print the string

n1 = input("Type your first number: ") # set n1 to the input from the user
n2 = input("Type your second number: ") # set n2 to the input from the user

addition = n1 + n2  # set addition as the sum of n1 and n2
subtraction = n1 - n2 # set subtraction as the difference of n1 and n2
multiplication = n1 * n2 # set multiplication as the product of n1 and n2
division = n1 / n2 # set division as the quotient of n1 and n2

print "\nThe results are:\n" # print the string
print "%r + %r = " % (n1, n2), addition # print the string and addition
print "%r - %r = " % (n1, n2), subtraction # print the string and subtraction
print "%r * %r = " % (n1, n2), multiplication # print the string and multiplication
print "%r / %r = " % (n1, n2), division # print the string and division
