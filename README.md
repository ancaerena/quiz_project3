Bugs:
User's answer was in the same line as the question. Resolved by adding \n at the end of the question.
Printing the delimitation symbol ~ gave an error: SyntaxError: invalid syntax. Fixed it by adding quotation marks around the symbols to make it a string
Error running run.py because of an indentation error. Found that ":" was missing from the last question before the list of answers
Answers were showing in lists for each lowercase letter enumeration. The issue was a typo in print statement for printing the answers, instead of {option} it was {options}
Question to add the name after some questions to continue the game - I was calling the add_name function in the choices feedback
Trying to use the name from add_name function into a future fucntion: using the global var option for name variable returned the error: global name = input("Enter your name to start the game:\n")
                ^
SyntaxError: invalid syntax
I sorted the issue by taking the name input out of the function
Validate user answer if using uppercase - using lower() have transformed the answer to lowercase



StockFlow - in finding the string to import for lowercase enumeration