from string import ascii_lowercase


def welcome_message():
    """
    Welcoming message with instructions and name input
    """
    print("~~~~~~~~~~~~~~")
    print("welcome to F.R.I.E.N.D.S trivia!")
    print("Choose the right answer from the 4 available options!")
    print("Only one answer is correct!")
    print("~~~~~~~~~~~~~~")


welcome_message()

name = input("Enter your name to start the game:\n")

"""
Add the structure for questions and answers
Add dictionary to store all questions and answers so the code isn't repetitive
Added multiple choices for valid correct answer
"""
QUESTIONS = {
    "What piece was missing from Rachel's plane when leaving for Paris": [
        "Left phalange", "A wing", "Left engine", "Right engine",
    ],
    "What year does Ross imply Rachel hasn't cooked since": [
        "1996", "2022", "1990", "2001",
    ],
    "What do you need to have in order to always be prepared for an attack": [
        "Unagi", "A knife", "Good lungs to scream", "A sword",
    ],
    "What is the only appropriate word to use when moving a couch": [
        "Pivot", "Ready, steady, go", "Unagi", "Green means go",
    ],
    "Who was Rachel's prom date": [
        "Chip Matthews", "Matthew Chips", "Ross Geller", "Monica Geller",
    ],
    "What was Joey's fake name": [
        "Ken Adams", "Drake Ramoray", "Chandler Bing", "Troy Ribbianni",
    ],
    "Phoebe thought 'Kenny the Copy Guy' was who": [
        "Ralph Lauren", "Bruce Willis", "Brad Pitt", "Her brother",
    ],
    "Who is the youngest Friend": [
        "Rachel", "Monica", "Phoebe", "Joey",
    ],
    "How much the ticket to Yemen cost": [
        "2100 dolars", "300 dolars", "They were free", "1000 dolars",
    ],
    "Joey was cast as the butt double for which actor": [
        "Al Pacino", "Matthew Perry", "George Clooney", "Alec Baldwin",
    ]
}

"""
Adding counting of correct answers
"""
num_correct = 0
"""
for loop to iterate through questions and answers
used sorted() to randomly display the answers
"""

for num, (question, options) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}: ")
    print(f"{question}?\n")

    correct_answer = options[0]

    labeled_options = dict(zip(ascii_lowercase, sorted(options)))

    for label, option in labeled_options.items():
        print(f"  {label}) {option}")
    """
    Use a while loop to check the validity of inputed data
    """
    while (answer_label := input("\n Your answer is:\n")) not in labeled_options:
        print(f"Please choose one of {', '.join(labeled_options)}")
    answer = labeled_options[answer_label]

    """
    If statement to check the correct answer
    """
    if answer == correct_answer:
        num_correct += 1
        print(f"Well done, {name}! You sure know your friends!")
    else:
        print("You've been bamboozled!")
        print(f"The answer is {correct_answer!r}, not {answer!r}\n")
        
print(f"\n You got {num_correct} correct out of 10")
