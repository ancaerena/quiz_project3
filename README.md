<h1>F.R.I.E.N.D.S Trivia Quiz Game</h1>
<br>
<br>
Friends Trivia is a Python terminal game, which runs in Code Institute mock terminal on Heroku
Users are asked to answer questions about Friends TV show to test their knowledge about the series. 
Each question comes with options from which the user can choose.
At the end, the user finds out their score.
<br>
<img src="assets/images/responsive.jpg" alt="multiple screen sizes diplaying the website">
<br>
<br>
<h2>How to play</h2>
This quiz has 10 questions about the F.R.I.E.N.D.S. TV series <br>
The game starts with a few instructions and asks the user for their name.<br>
Once the name is added, the game starts with the first question. All questions have 4 options to choose from.<br>
After each answer, the user receives a feedback to highlight if their answer was correct or not. The correct answer then is counted for the final result.<br>
After all 10 questions are answered, the user receives his total score.<br>
The user is then asked if he would like to give it another try one more time. If he agrees, the game starts with the first question.
<br>
<h2>Plan</h3>
<br>
- using LucidChart to frame out the code plan for the game. Maping out helped to see where I should start and where the game ends
<br>
<img src="assets/images/workflowchart" alt="chart with the game plan">
<br>
<h2>Features</h2>
<hr>
<h3>Existing Features</h3>
<br>
- It is featured on all 4 pages of the website, it is identical on all to allow easy navigation. It includes links to all pages, marking them active when lading on one of them, to keep track of the page the user is on.
- This will allow the user to navigate through the pages easily, without needing to use the "back" button of a browser.
<img src="assets/images/nav-bar.jpg" alt="navigation bar for little musketeers page">
<br>
<h3>Features left to implement</h3>
<br>
<h4>Registration form</h4>
- A form where users can register for the programme, with starting date, type of service(before-school or after-school), days of the week, with or without transport. This feature will also give the price at the end, depending on services selected
<br>
<h2>Fixed Bugs</h2>
- User's answer was in the same line as the question. Resolved by adding \n at the end of the question.<br>
- Printing the delimitation symbol ~ gave an error: SyntaxError: invalid syntax. Fixed it by adding quotation marks around the symbols to make it a string.<br>
- Error running run.py because of an indentation error. Found that ":" was missing from the last question before the list of answers<br>
- Answers were showing in lists for each lowercase letter enumeration. The issue was a typo in print statement for printing the answers, instead of {option} it was {options}<br>
- Input to add the name after some questions to continue the game - I was calling the add_name function in the choices feedback.<br>
Trying to use the name from add_name function into a future function: using the global var option for name variable returned the error: global name = input("Enter your name to start the game:\n")
                ^
SyntaxError: invalid syntax<br>
I sorted the issue by taking the name input out of the function<br>
- Validate user answer if using uppercase - using lower() have transformed the answer to lowercase<br>
<br>
<h2>Testing</h2>
<br>
- I've tested in my terminal and Heroku Terminal<br>
- Passed the code through PP8 liner
- 
<h3>Validator testing</h3>
<br>
-No errors were returned when passing through the PP8 
<br>
<h2>Deployment</h2>
<br>
- This project was deployed using Code Institute mock terminal for Heroku
<br>
A. In the Github repository, navigate to the Settings tab
<br>
B. From there, select Pages from the left side
<br>
C. From the source section drop-down menu select Main as a branch and then save
<br>
D. Once the main branch was selected, the page provided the link to the completed website
<br>
<h2>Credits</h2>
<br>
- My mentor Jubril Akolade for overviewing the project and suggesting a few changes to be more user-friendly
- StockFlow - in finding the string to import for lowercase enumeration
- Realpython.com in helping organising my code in functions