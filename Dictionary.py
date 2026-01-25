Birthdays = {'Alice': 'April 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    name = input("Enter your name:")
    if name == "":
        break

    if name in Birthdays:
        print(f"{Birthdays[name]}is the birthday of {name}")
    else:
        print(f"I do not have information for {name}")
        print("What is their birthday?")
        bday = input()
        Birthdays[name] = bday
        print("Birthday database updated")
        print(Birthdays)
        break


