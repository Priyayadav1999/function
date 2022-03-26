def voting_age(x):
    if x>=18:
        print("Eligible for vote")
    else:
        print("Not Eligible")

age=int(input("enter the age="))
voting_age(age)