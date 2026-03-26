table = {}

while True:
    print("\n1. Insert 2.Search 3. Display 4.Exit")
    ch = int(input("Enter Choice : "))

    if ch ==1:
        name = input("Enter ideantifer : ")

        if name in table:
            print("Error : Duplicate entry")
        else:
            dtype = input("Enter data type : ")
            loc = input("Enter the location : ")
            table[name] = (dtype,loc)
            print("Inserted successfully")

    elif ch==2:
        name = input("Enter identifer to search : ")

        if name in table:
            print("Found")
            print("Type: ",table[name][0])
            print("Location: ",table[name][1])
        else:
            print("not found")

    elif ch == 3:
        print("\nSymbol Table")
        print("Name\tType\tLocation")

        for name in table:
            print(name,"\t",table[name][0],"\t",table[name][1])
    
    elif ch ==4:
        break

    else:
        print("Invalid choice")