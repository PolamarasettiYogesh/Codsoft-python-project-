def calculator():
    print("welcome to calculator")
    while True:
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")

        choice = input("enter your choice:").strip()

        if choice == "5":
            print("calculator closed")
            break 
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == "1":
            print("result: ", num1 + num2)
        elif choice == "2":
            print("result: ", num1 - num2)
        elif choice == "3":
            print("result: ", num1 * num2)
        elif choice == "4":
           if num2 == 0:
               print("cannot divide by zero")
           else:
               print("Result: ", num1/num2)
        else:
            print("Invalid choice")
calculator()    
              