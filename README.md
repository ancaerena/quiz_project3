Bugs:
User's answer was in the same line as the question. Resolved by adding \n at the end of the question.
Printing the delimitation symbol ~ gave an error: SyntaxError: invalid syntax. Fixed it by adding quotation marks around the symbols to make it a string
Error running run.py because of an indentation error. Found that ":" was missing from the last question before the list of answers
Answers were showing in lists for each lowercase letter enumeration. The issue was a typo in print statement for printing the answers, instead of {option} it was {options}


StockFlow - in finding the string to import for lowercase enumeration