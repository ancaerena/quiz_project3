def welcome_message():
    print("~~~~~~~~~~~~~~")
    print("welcome to F.R.I.E.N.D.S trivia, where your knowledge about your favorite TV show is tested!")
    print("Choose the right answer and find out your score at the end")
    print("~~~~~~~~~~~~~~")
    name = input("Enter your name to start the game:\n")
welcome_message()

"""
Add the structure for questions and answers. Add lists and tuples to store all questions and answers so the code isn't repetitive
"""
QUESTIONS = [
    ("How many seasons F.R.I.E.N.D.S TV show has", "10"),
    ("What is the name of Phoebe's twin sister", "Ursula"),
    ("Who was the previous tendent of Ross's new appartment", "Ugly naked guy"),
    ("What was the occupation of Rachel's fiancé Barry Farber", "Orthodontist"),
    ("In which season Ross and Rachel get together for the first time", "2"),
    ("What is Chandler Bing's middle name", "Muriel"),
    ("What was the profession of Joey's imaginary friend", "Space cowboy"),
    ("Which of the Friends characters broke a swing as a child", "Monica"),
    ("What piece was missing from Rachel's plane when leaving for Paris", "Left phalange"),
    ("What year does Ross imply Rachel hasn't cooked since in 'The one with Phoebe's Birthday Dinner'", "1996"),
    ("How many times does Ross get divorced", "3"),
    ("Who mistakingly threw a woman's wooden leg into a fire", "Joey"),
    ("In which season does Phoebe get married", "10")
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Well done you! You sure know your friends!")
    else:
        print(f"You've been bamboozled!The asnwer is {correct_answer!r}, not {answer!r}")
