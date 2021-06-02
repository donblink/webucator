def main():
    phrase = input("please enter a phrase ? ")
    print("your phrase is ' " + phrase + " ' ")
    start = input("What character would you like to start with ? [Enter a number] ")
    end = input("What character would you like to end with ? [Enter a number] ")
    output = phrase[int(start):int(end)+1]
    print("your substring is " + output )

def challenge():
    phrase = input("please enter a phrase ? ")
    print("your phrase is ' " + phrase + " ' ")
    start = input("What character would you like to start with ? [Enter a number] ")
    end = input("What character would you like to end with ? [Enter a number] ")
    output = phrase[(int(start)-1):(int(end))]
    print("your substring is " + output )

#main()   
challenge() 