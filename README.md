# HANGMAN

This project set out to build a version of the well-known word game, hangman. The game aims to provide a fun challenge aimed at an adult audience based on the variety and lebgth of words. Users should find enjoyment in completing the challenge of the game and it also provides the opportunities for users to build their vocabulary or English language knowledge. 

- __Design__
Planning and design of the game was aided by using Lucidchart. The below visual lays out the user journey and logic flow behind which informed the structure and code utilised in the build of the game. 
This includes mapping of:
- Instructions and other information to be conveyed to players.
- Requests for user input in order to progress game.
- Instances where input needs to be evaluated for validity. 
- Evaluation ot input and decisions on game progression or feedback to players. 

![hangman_design_flow](https://user-images.githubusercontent.com/92268504/159022155-b9448577-6597-4259-9d2e-7bd7a1ed5b18.png)


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

  - In both instances, the player is served a feedback message and graphic informing them of their results. 

- __Graphics__


![Club Ethos](https://github.com/lucyrush/readme-template/blob/master/media/love_running_ethos.png)


### Future Expansion & Build

- Another feature idea
- new word packs
- difficulty
- new game
- leader board 

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

### Unfixed Bugs

No unfixed bugs remain in code at time of submission. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 

### Credits: Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Credits: Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Credits: Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 
