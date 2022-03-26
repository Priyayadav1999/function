def eligible_for_vote(a):
    if a>=18:
        print("eligible for vote")
    else:
        print("not eligible")
x=int(input("enter your age"))
eligible_for_vote(x)