print("welcome to the pattern generate and number Analyzer!")

while True:
    print("select an option")
    print("1.Generate a Pattern")
    print("2.Analyze a Range of number")
    print("3.exit")

    choice=int(input("enter the choise:"))
    
    if choice == 1:
        row=int(input("enter the number of row for the pattern"))

        print("pattern")
        for i in range(1, row+1):
             print("*" * i)

    elif choice == 2:
        start=int(input("enter the start of the range "))
        end=int(input("enter the end of range"))

        total=0
        for num in range(start,end+1):
            if num%2==0:
                print("number",num,"is even")
            else:
                print("number",num,"is odd")

                total=total+num
                print("sum of all number from",start,"to",end,"is",total)
                
    elif choice == 3:
        print("Exiting the program, Goodbye")
        break

else:
    print("Invalid choice.Please try again.")


       