import math

def prompt_user():
    number_of_people = input("how The number of people ? ")
    num_ppl = int(number_of_people)
    number_of_slice_each_person_will_eat = input("what is The number of slice each person will eat ? ")
    slice_per_person = float(number_of_slice_each_person_will_eat)
    slice_in_each_pizza = input("what is The number of slice in each pizza ? ")
    slice_per_pizza = float(slice_in_each_pizza)
    return(num_ppl, slice_per_person, slice_per_pizza)

def how_many_pizza_is_need_for_everyone( *args):
    total_slice_share = args[0][0] * args[0][1]
    number_of_pizza = math.ceil(total_slice_share/args[0][2])
    leftover = (number_of_pizza * args[0][2]) - total_slice_share
    return (args[0][0], number_of_pizza, leftover)
    

def print_report( *args):
    print("you need "+ str(args[0][1]) + " pizza to feed "+  str(args[0][0])+ ", ")
    print("there will be "+ str(int(args[0][2])) + " lefttover slices.")

    

def main():
    info = prompt_user()
    pizza = how_many_pizza_is_need_for_everyone(info)
    print_report(pizza)


main()

