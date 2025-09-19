from datetime import date 

def write_entry():
    with open("journal.txt","a") as f:
        entry=input("What's on your mind Today?\n")
        f.write(f"\nEntry Date: {date.today()}\n")
        f.write(entry + "\n")

def read_entries():
    try:
        with open("journal.txt","r") as f:
            print("Your journal entries:\n")
            print(f.read())
    except FileNotFoundError:
        print("\nNo journal entries found.\n")
    
def main():
    print("Welcome to your Personal Digital Journal!\n")
    while True:
        print("What would you like to do?")
        print("1. Write a new entry.")
        print("2. Read all entries.")
        print("3. Exit.")

        choice=int(input("Enter your choice ( 1 | 2 | 3 ) >>> "))

        if choice==1:
            write_entry()
        elif choice==2:
            read_entries()
        elif choice==3:
            print("See You Again with the deepest thought to discuss ;) \n")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")



if __name__ =="__main__":
    main()
