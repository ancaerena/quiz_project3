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


def add_name():
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
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def user_choice(question, options):
    print(f"{question}?\n")
    labeled_options = dict(zip(ascii_lowercase, options))
    for label, option in labeled_options.items():
        print(f"  {label}) {option}")


    """
    Use a while loop to check the validity of inputed data
    """    
    while (answer_label := input("\n Your answer is:\n").lower()) not in labeled_options:
        print(f"Please choose one of {', '.join(labeled_options)}")
    return labeled_options[answer_label]


def show_questions(question, options):
    correct_answer = options[0]
    shuffled_options = random.sample(options, k=len(options))

    answer = user_choice(question, shuffled_options)
    if answer == correct_answer:
        print(f"Well done! You sure know your friends!")
        return True
    else:
        print("You've been bamboozled!")
        print(f"The answer is {correct_answer!r}, not {answer!r}\n")
        return False


def start_quiz():
    questions = organise_questions(QUESTIONS, TOTAL_QUESTIONS)

    num_correct = 0
    """
    for loop to iterate through questions and answers
    used sorted() to randomly display the answers
    """
    for num, (question, options) in enumerate(questions, start=1):
        print(f"\nQuestion {num}: ")
        num_correct += show_questions(question, options)
    print(f"\n You got {num_correct} correct out of {num}\n")
      

def main():
    welcome_message()
    add_name()
    start_quiz()

main()

def play_again():
    playAgain = input("Would you like to play again? 1 for Yes, 2 for No\n")
    if playAgain == "1":
        playing = start_quiz()
    else:
        print("Thank you for playing our game")
    
play_again()