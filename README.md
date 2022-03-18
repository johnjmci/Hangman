# HANGMAN

LIVE APP LINK - https://six-hangman.herokuapp.com/ 

This project set out to build a version of the well-known word game, hangman. The game aims to provide a fun challenge aimed at an adult audience based on the variety and lebgth of words. Users should find enjoyment in completing the challenge of the game and it also provides the opportunities for users to build their vocabulary or English language knowledge. 

- __Design__
Planning and design of the game was aided by using Lucidchart. The below visual lays out the user journey and logic flow behind which informed the structure and code utilised in the build of the game. 
This includes mapping of:
- Instructions and other information to be conveyed to players.
- Requests for user input in order to progress game.
- Instances where input needs to be evaluated for validity. 
- Evaluation ot input and decisions on game progression or feedback to players. 

![lucid_hangman_0322](https://user-images.githubusercontent.com/92268504/159069402-f4627a4f-ee1b-4166-a2d5-900bd665c129.png)


## Features 

The game is intentionally simple in design. The project has been completed using Python, with focus on creating code and logic which successfully deals with player input. 

### Existing Features

- __Welcome & Instruction__

  - Players are welcomed with a brief description of how to play the game. Hangman is a well-known game, so explanation has be kept minimal. Hangman can be played with words of varying length, however, this version of the game serves up words of six letters in length. A list of 492 letters being utilised has been sourced from freedictionary.com. 

<img width="800" alt="play_screen_open" src="https://user-images.githubusercontent.com/92268504/159028652-263e3326-8314-4753-83cd-74041f47e2be.png">
HanHangman 
  - In order to personalise the experience of the game to a degree, players are asked for and then greeted by their first name. 
 <img width="798" alt="play_screen_begin " src="https://user-images.githubusercontent.com/92268504/159028866-2ba822eb-5b3e-4387-b199-9b01a41634bb.png">
 
- __Game Play__

  - The main action requested of players is to guess a letter to check if it is contained in the mystery word selected by the computer. Guesses are evaluated to check if the input is:
A valid character it ie a letter from a to z.
A letter which hasn'r been previously guessed. 
A letter contained witin the mystery word. 

<img width="784" alt="play_sreen_check" src="https://user-images.githubusercontent.com/92268504/159029274-10c84111-4fc0-422d-b790-6f8f67285e1b.png">

- __Results__

  - The game is coded to monitor how many wrong answers a player has accumulated and will trigger feedback to the player as t whether they have won or lost the game. 
  - Should the number of wrong answers equal to the number of lives in the game then the player has run out of lives and has lost the game.
  <img width="794" alt="play_screen_lose" src="https://user-images.githubusercontent.com/92268504/159038314-340af241-af6e-4584-b4f4-8fa24887534b.png">

  - Once the number of correct letters is equal to the number of letters in the mystery word, this means that the complete word has been guessed and the player has won.   
 <img width="783" alt="play_screen_winner" src="https://user-images.githubusercontent.com/92268504/159038360-5b83c57d-69ef-4310-80d6-1aa786d234f6.png">

  - In both instances, the player is served a feedback message and graphic informing them of their results. Currently it was decided to not reveal the answer to an incomplete game to a player when the game is over, this will increase the longevity of the current game content. 

### Future Expansion & Build

Game has been created as intended and includes core functionality. Notes of future expansion and improvement areL
- Option to add additonal lists of words. These could be themed by topic and even updated seasonally to coincide with holdays.  
- Adding additional lists of words grouped by difficulty, incorporating the option for users to select whcih group they are served words from. 
- Consider options to restart the game upon completion or to quit and restart midway through a game. 
- Explore options around storing highest score against username. 

## Testing 

User testing was completed by mysel as well as a pool of friends who played the game and have feedback on any errors, quirks of issues that they experienced during the course of play. Key issues adressed:

1. Function of being able to press any key to begin not functioning correctly -> Replaced with function of press Enter to start game.
2. Entering a invalid character found to be costing users a life -> Updated logic of game so that invalid characters were not to be counted as incorrect answers. 
3. Letter entered after in the turn after aninvalid character is entered not being recorded as a guess -> Update order of code to prevent rectify this issue.
4. Not all input functions displaying the users input in uppercase, only the initial prompt to input a letter and not those following invalid or repeated guessed -> .upper action added to remaining input instances. 
5. Some errors and typos in instructional code also flagged and corrected.

### Validator Testing 

- Python
Code tested using the PEP 8 online code checker http://pep8online.com/
61 issues were found, described as:
"blank line contains whitespace"
"block comment should start with '# '"
"indentation is not a multiple of four (comment)"
"line too long (100 > 79 characters)"
"missing whitespace after ','"
"module level import not at top of file"
"too many blank lines (2)"
"too many leading '#' for block comment"
"trailing whitespace"

All errors and issues flagged by PEP 8 have been resolved.
<img width="982" alt="pep_code_check_final" src="https://user-images.githubusercontent.com/92268504/159061433-5ebb5709-018e-4532-a989-2fbf20af353d.png">

### Unfixed Bugs

No unfixed bugs remain in code at time of submission. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- This game was built using Github, utilising Python and deployed via Heroku with a moch terminal accessible via a webpage. The steps for deployment are as follows: 
  1. Add a new line at the end of code requesting input. This is to accomodate a quirk in the software used tocreate the mock terminal.  
  2. Add list of dependencies to requirements.txt file using code "Pip3 freeze > requirements.txt" in the terminal 
  3. Commit these changes and push to Github
  4. Utilising a Heroku account, navigate to the option of "Create a new app" from the main menu 
  5. Name app with a unique name and confirm geographical region -> Select create app
  6. Within the Setting section, update a new key with name "PORT" and value of "8000"
  7. Within settings, add Python and nodejs build packs in this order
  8.  Within the Deploy section, selectGithub and confirm connection between your Github and Heroku accounts
  9.  Search for the repository name, in the case of this project, it is "johnjmci/Hangman" -> Select Connect 
  10.  Regarding deploy method, I have chosen to select the option of Automatic deploys
  11.  App willbe built and link to view app will be presented below the build section in button labelled "View" 
  
The live link can be found here - https://six-hangman.herokuapp.com/

### Credits: Content & Media 

- The dictionary of possible mystery words used within the game were sourced from the free dictionary https://www.thefreedictionary.com/6-letter-words.htm 
- Instructional text was created specifically for this project
- The main game play graphics of the gallows and hangman were sourced from Hangman ASCII Art https://ascii.co.uk/art/hangman 
- Other stylised text was created using the ASCII Generator http://www.network-science.de/ascii/ 

## Credits: Other General Project Advice

The build of this project has been informed by reference material made available in the Code Institute Diploma in Software Development.
Instructional and trouble shooting support accessed via Stack Overflow and W3Schools.
Refernce also made to community content shared by the Code Insitite community via Slack. 

### Technologies & Resources
- Heroku https://dashboard.heroku.com/
- Github https://github.com/johnjmci
- Hangman ASCII Art https://ascii.co.uk/art/hangman 
- ASCII Generator http://www.network-science.de/ascii/ 
