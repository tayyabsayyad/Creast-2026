# Session 4: Voting age check
age = int(input("Enter age: "))
if age < 18:
    print("go home")
elif age == 18:
    print("congrats")
else:
    print("go vote")
