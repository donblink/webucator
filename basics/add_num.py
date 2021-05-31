def add(a,b):
    return a+b

def print_total(total):
    print ("the sum of the addition is : " + str(total) )

def query_number():
    number1  = input("enter the first number: ")
    integer1 = int(number1)
    number2  = input("enter the second number: ")
    integer2 = int(number2)
    return (integer1, integer2)

def main():
    (operand1,operand2) = query_number()
    sum = add(operand1, operand2)
    print_total(sum)

main()    