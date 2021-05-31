def divide(numerator, denominator):
    if (denominator!= 0):
        quotient = numerator/denominator
        remainder = numerator % denominator
    else :
        print("Error : can not divide by zero")    
    return( quotient, remainder)

def print_report():
    num = input("Enter the numerator for the division:")
    den = input("Enter the number for the denominator: ")
    print("================================================")
    report = divide(int(num), int(den))
    print(str(num) + " divide by " + str(den) + " equal " + str(int(report[0])) + " with a remainder of " + str(report[1]))


print_report()    