def calculator():
    try:
        n1=int(input("Enter First No: "))
        n2=int(input("Enter Second No: "))


        print("What kinda operation you wanna perform\nPress \'+\' for addition\nPress \'-\' for Substraction\nPress \'*\' for Multiplication\nPress \'/\' for division")

        o=input("Enter the Operation You wanna Perform: ")

        match o:
            case("+"):
                print(f"Result is {n1+n2}")
            case("-"):
                print(f"Result is {n1-n2}")
            case("*"):
                print(f"Result is {n1*n2}")
            case("/"):
                if(n2==0):
                    print("error:cant divide by zero")
                else:
                    print(f"Result is {n1/n2}")
            case default:
                print("Please Give A valid Operation")

    except Exception as e:
        print("Enter Valid number")




while True:
    calculator()
    if(input("Do you wanna continue? (Y?N): ").lower()=="n"):
        break

print("Thanks For Using My Calculator")