# Readme Project Plan

Abstract: 
To have a chess game with an HTML user interface as well as a CHESS AI to allow for users to play against the computer. (A majority of the original chess game was made during the first 6 weeks of the trimester, however along with the chess ai, there were a few parts that we worked on during the last 6 weeks.)
As this was a huge scope we split the project into two:


##### Chess with HTML interface:
A port of the original ascii chess game to a html user experience. This project is a test of understanding POST and how to tie python code (backend/ what the user cannot see) with jinja to the HTML (front end/what the user can see). Here was the original Ascii Chess Game (where all of the backend logic came from): https://repl.it/@KyleMyint/ASCII-Chess#0README.md. As one can see the input of having the user type in the start and end square was very tedious and hard for new players to understand how to move the pieces. We wanted to create a more intuitive user interface. As seen here:

##### Chess AI: 
Delving deep into the logic of code creating the chess AI allows the team to understand the concept of creating a bot and training it. We emphasize certain aspects as a priority to others. Without user input, the chess AI code can respond to their opponent by moving chess pieces based on the calculated value of each possible move. 
Features: 
Main menu using POST:
This is to allow for the interaction with the page run specific functions rather than just using hrefs to decorators (routes). 
Notice the styling on the POST button: https://bit.ly/35Xa862.
In Game: 
64 submit buttons configured with JInja from the chessData.py document. 
A table that shows all the previous moves that correspond to the move number: https://bit.ly/2Hpsbbl.
We were able to implement auto scrolling into the table with javascript so no longer how long the game is played, the players will always see the most recent move made: https://bit.ly/3q3kVDI.
Messages that allow for debugging.
This is a simple implementation of jinja: https://bit.ly/3fnh3Iw.

# Todos
## Cleaning up the HTML and JINJA
<ul>
<li>Create a more user friendly ui with the chess board (can you change the css of the chess board when the user selects a specific cell to highlight the specific cell selected)</li>
<li>Consolidate the jinja that is passed into each of the render template within Main.py (currently if we want to change some of the code to redo the function of updating the jinja variables, we have to copy and paste the</li>
<li>Customization, currently on the menu there is a button for customization that is currently disabled, we want this to allow the users to customize the color of the board, customize the color of their pieces. Can you also implement a preview of customization in the selector screen before starting the game?</li>
<li>CSS and JS, can we create custom animation much like the button to start the game: https://bit.ly/35Xa862 with custom icons to represent each option (cogs for setting, a clip board with rules, etc)</li>
<li>Implement a forfeit button (implemented with POST to allow for each player to give up)</li>
<li>Implement restrictive selection of the pieces. Currently any person can move any piece, can you implement the restriction of player 1 only moving the white pieces while player 2 can only move the black pieces?</li>
<li>Need to implement a proper board reset, when restarting the board there are some posittions that are carried over from previous games</li>
</ul>
## Implementing Databases:
<ul>
<li>Implement multiplayer, with the dawn of learning databases, can you implement playing online onto the game so that when players log in they are able to play with people who have also connected up onto the raspberry pi to play</li>
<li>Implement replay game, this was an original feature of the ASCII CHESS game, can we tie each saved game to the login of the user to allow each player to look at their past games</li>
</ul>
