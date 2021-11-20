def all_true(iterable):
    result = False 
    for item in iterable:
        if bool(item):
            result = True 
            continue 
        else: 
            result = False
            break
    return result 

def any_true(iterable):
    result = False
    for item in iterable:
        if bool(item):
            result = True
            break
        else:
            continue
    return result    


def main():
    a = all_true([1,0,1,1,1])
    b = all_true([1,1,1,1,1])
    c = any_true([0,0,0,1,1])
    d = any_true([0,0,0,0,0])
    
    print(a,b,c,d)

main()    