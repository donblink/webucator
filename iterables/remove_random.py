import random

def remove_random():
    list = [ 1,2,7,"blue","red","green",{"a":1}]
    print("Element in the list are : " + str(list))
    choice = random.choice(list)
    print("the element from the list to be delete is :" + str(choice))
    index = list.index(choice)
    del list[index]
    print("remaining element in the list are post random delete : " + str(list))
    return list 

def main ():
    new_list_post_random = remove_random()

main()
