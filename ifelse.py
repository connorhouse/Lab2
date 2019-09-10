x = int(input("Enter a score here: "))

def score_var(score):
    if score >= 90:
        return "4"
    elif (score <= 89) and (score >= 80):
        return "3"
    elif (score <= 79) and (score >= 70):
        return "2"
    elif (score <= 69) and (score >= 60):
        return "1"
    else:
        return "0"
print("Your gradepoint is:", score_var)

            # Create a file called ifelse.py. (2.30) Write a nested selection using ifelse that sets the value of a variable gradepoint to 4 if a variable named score is greater than 90,
            # 3 if score is between 80 and 89,
            # 2 if score is between 70 and 79,
            # 1 if score is between 60 and 69,
            # and 0 otherwise.




