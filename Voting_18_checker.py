import datetime

year = datetime.datetime.today().year

print("Check to see if you can vote in the UK (age wise) \n")

answer_year = int(input("Enter the year you were born \n"))

vote_answer = year - answer_year

if (vote_answer == 18):
    print("You are too young to vote! \n")

if (vote_answer =! 18):
    print("You can vote! \n")
