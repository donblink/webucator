def main():
    phrase = input("please enter a phrase ? ")
    print("your phrase is ' " + phrase + " ' ")
    number = input("What character would you like to see? [Enter a number] ")
    output = phrase[int(number)]
    print("character number "+ number + " is " + output )

def challenge():
    phrase = input("please enter a phrase ?")
    print("your phrase is ' " + phrase + " ' ")
    number = input("What character would you like to see? [Enter a number] ")
    output = phrase[int(number) - 1]
    print("character number "+ number + " is " + output )

main()   
challenge() 