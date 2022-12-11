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
    "How many seasons F.R.I.E.N.D.S TV show has": [
        "10", "8", "6", "12",
    ],
    "What is the name of Phoebe's twin sister": [
        "Ursula",
        "Muriel",
        "Una",
        "Angela",
    ],
    "Who was the previous tendent of Ross's new appartment": [
        "Ugly naked guy",
        "Cute dressed guy",
        "The Fat neighbour",
        "Mike",
    ],
    "What was the occupation of Rachel's fiancé Barry Farber": [
        "Orthodontist",
        "Doctor",
        "Dentist",
        "Gynecologist",
    ],
    "In which season Ross and Rachel get together for the first time": [
        "2", "8", "1", "3",
    ],
    "What is Chandler Bing's middle name": [
        "Muriel", "Eric", "Mathew", "John",
    ],
    "What was the profession of Joey's imaginary friend": [
        "Space cowboy", "Cowboy", "Penguin", "Actor",
    ],
    "Which of the Friends characters broke a swing as a child": [ 
        "Monica", "Phoebe", "Janice", "Joey",
    ],
    "What piece was missing from Rachel's plane when leaving for Paris": [
        "Left phalange", "A wing", "Left engine", "Right engine",
    ],
    "What year does Ross imply Rachel hasn't cooked since": [
        "1996", "2022", "1990", "2001",
    ],
    "How many times does Ross get divorced": [
        "3", "4", "1", "5",
    ],
    "Who mistakingly threw a woman's wooden leg into a fire": [
        "Joey", "Ross", "Mike", "Phoebe",
    ],
    "In which season does Phoebe get married": [
        "10", "She doesn't get married", "8", "9",
    ],
    "What was the name of Ross' pet monkey": [
        "Marcel", "Monkey", "Monica", "Susan",
    ],
    "What do you need to have in order to always be prepared for an attack": [
        "Unagi", "A knife", "Good lungs to scream", "A sword",
    ],
    "How many characters wore a raw turkey on their head": [
        "2", "All 6", "1", "None",
    ],
    "What are the names of Rachel's sisters": [
        "Jill and Amy", "Amy and Monica", "Amelia and Joleen", "Judy and Ana",
    ],
    "What is the only appropriate word to use when moving a couch": [
        "Pivot", "Ready, steady, go", "Unagi", "Green means go",
    ],
    "Who was Rachel's prom date": [
        "Chip Matthews", "Matthew Chips", "Ross Geller", "Monica Geller",
    ],
    "How many pages was Rachel's letter to Ross": [
        "18 pages", "10 pages front and back", "12", "20",
    ],
    "In an effort to get over Richard, Monica started making what": [
        "Jam", "Pancakes", "Pie", "Origami",
    ],
    "What was Joey's fake name": [
        "Ken Adams", "Drake Ramoray", "Chandler Bing", "Troy Ribbianni",
    ],
    "Phoebe thought 'Kenny the Copy Guy' was who": [
        "Ralph Lauren", "Bruce Willis", "Brad Pitt", "Her brother",
    ],
    "Monica could not tell time until what age": [
        "13", "6", "20", "30",
    ],
    "Who is the youngest Friend": [
        "Rachel", "Monica", "Phoebe", "Joey",
    ],
    "Which of Monica's boyfriends wanted to become a Fighting Champion": [
        "Pete", "Chandler", "Richard", "Julio",
    ],
    "Ross and Rachel's daughter Emma would have turned 18 what year": [
        "2020", "2010", "2000", "2030",
    ],
    "What kind of bed did the Mattress King deliver to Monica": [
        "A racecar bed", "A princess bed", "A single bed", "A couch",
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
    while (answer_label := input("\n Your answer is:\n")) not in labeled_options:
        print(f"Please choose one of {', '.join(labeled_options)}")
    answer = labeled_options[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print(f"Well done, {name}! You sure know your friends!")
    else:
        print("You've been bamboozled!")
        print(f"The answer is {correct_answer!r}, not {answer!r}\n")
        
print(f"\n You got {num_correct} correct out of 30")
