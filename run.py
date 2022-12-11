def welcome_message():
    print("welcome to F.R.I.E.N.D.S trivia, where your knowledge about your favourite TV show is tested!")
    print("Choose the right answer and find out your score at the end")
    name = input("Enter your name to start the game:\n")
welcome_message()

"""
Add the structure for questions and answers
"""
answer = input("How many seasons did the F.R.I.E.N.D.S tv series had?\n")
if answer == "10":
    print("Correct, well done for your first question!")
else:
    print(f"The answer is '10' , not {answer!r}")