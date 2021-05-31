def add_variable_arg(*args):
    print("the total is the sum of :")    
    for arg in args:
        print(" + " + str(arg) )
    print("---------")    
    total = sum(args)    
    print("  " + str(total) )
    return total    

def separator(sep="================"):
    print(2*sep)   
     
