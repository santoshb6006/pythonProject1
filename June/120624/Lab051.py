# Write a program that calculates and displays the results of the students

score = float(input("Enter the scores secured by candidate\n"))
if score >= 85 and score <=100:
    print("The candidate has secured A grade")
elif score >= 70 and score <=85:
    print("The candidate has secured B grade")
elif score >= 60 and score<=70:
    print("The candidate has secured C grade")
elif score >= 35 and score <=60:
    print("The candidate has secured D grade")
else:
    print("The candidate has secured HOUSE grade")
