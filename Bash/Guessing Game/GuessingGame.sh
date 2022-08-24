#!/usr/bin/env bash
# File: guessinggame.sh

#store ls | wc -l cmd in files variable, create while loop that prompts the user
#store users guess in answer variable
#create while loop that checks if user guess matches files variable
#create if/elif/else statement to tell user if guess is too high/low/spot on
#break loop when user guesses correctly
#Not much repeated code here.. but lets create a function to echo "guess again" 

files=$(ls | wc -l) 

function guess {
  echo "Guess again."
}

while [[ $answer != $files ]]
do
  echo "How many files are in the current directory?"
  read answer
  if [[ $answer =~ [0-9]+ ]]
  then
    if [[ $answer -gt $files ]]
    then
      echo "Too high."
      guess
    elif [[ $answer -lt $files ]]
    then
      echo "Too low."
      guess
    elif [[ $answer -eq $files ]]
    then
      echo "Got it!"
    fi
  else
    echo "Please enter your guess by using the number pad"
  fi
done

