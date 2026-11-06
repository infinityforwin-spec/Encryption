Years_of_experience=int(input("Enter the number of years of experience: "))
Rating=int(input("Enter the Rating: "))

if Years_of_experience>=2:
    if Rating>=4:
        bonus= 5000
        print("Congratulations you qualify fotr a bonus")
    elif Rating==3:
        bonus= 2000
        print("Youve goten a small bonus")
    else:
        bonus= 0
        print('You dont qualify for a bonus')
else:
    bonus= 0
    print("Not eligible for bonus")

print(f"Years of experience: {Years_of_experience}")
print(f"Rating: {Rating}")
print(f"Bonus: {bonus}")
