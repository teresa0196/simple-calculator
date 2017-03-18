print "Hi! This is a simple calculator.\nYou need to type two numbers.\n"

n1 = input("Type your first number: ")
n2 = input("Type your second number: ")

addition = n1 + n2
subtraction = n1 - n2
multiplication = n1 * n2
division = n1 / n2

print "\nThe results are:\n"
print "%r + %r = " % (n1, n2), addition
print "%r - %r = " % (n1, n2), subtraction
print "%r * %r = " % (n1, n2), multiplication
print "%r / %r = " % (n1, n2), division
