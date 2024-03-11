def check_voting_eligibility(age):
    if age >= 18:
        return True
    else:
        return False

# Input age
age = int(input("Enter your age: "))

# Check if eligible to vote
if check_voting_eligibility(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
