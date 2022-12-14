import random
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


while True:
    name = input("Enter your name to start the game:\n")
    if name.strip() != '':
        break
    

"""
Add the structure for questions and answers
Add dictionary to store all questions and answers so the code isn't repetitive
Added multiple choices for valid correct answer
"""
TOTAL_QUESTIONS = 10
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


def organise_questions(questions, num_questions):
    """
    function to organise the questions and shuffle them 
    so they are displayed in different order every time the player starts the game
    """
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def user_choice(question, options):
    """
    function to display questions and add lowecase letters to enumerate the options 
    """
    print(f"{question}?\n")
    labeled_options = dict(zip(ascii_lowercase, options))
    for label, option in labeled_options.items():
        print(f"  {label}) {option}")

    """
    Use a while loop to check the validity of inputed data
    added lower() to transform an uppercase input
    """    
    while (answer_label := input("\n Your answer is:\n").lower()) not in labeled_options:
        print(f"Please choose one of {', '.join(labeled_options)}")
    return labeled_options[answer_label]


def show_questions(question, options):
    """
    function to check for the right answer which is written as the first one, [0], in the QUESTION var
    display feedback on each answer and shuffle through options with random
    """
    correct_answer = options[0]
    shuffled_options = random.sample(options, k=len(options))

    answer = user_choice(question, shuffled_options)
    if answer == correct_answer:
        print(f"Well done, {name}! You sure know your friends!")
        return True
    else:
        print("You've been bamboozled!")
        print(f"The answer is {correct_answer!r}, not {answer!r}\n")
        return False


def start_quiz():
    """
    function to play the game, using the two var set at the start
    """
    questions = organise_questions(QUESTIONS, TOTAL_QUESTIONS)

    num_correct = 0
    """
    for loop to iterate through questions and answers
    """
    for num, (question, options) in enumerate(questions, start=1):
        print(f"\nQuestion {num}: ")
        num_correct += show_questions(question, options)
    print(f"\n You got {num_correct} correct out of {num}\n")
      

def main():
    """
    function to hold the starting of the game
    """

    start_quiz()


main()

"""
while loop to offer option to start the game again
"""
while True:
    answer = input("Do you want to play again? Reply with yes or no\n")
    if answer == 'yes':
        start_quiz()
    elif answer == 'no':
        print("Thank you for playing the game")
        break
    else:
        print("Please write 'yes' or 'no'")

