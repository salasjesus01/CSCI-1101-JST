
#initial commit
import re
answer_characters = "What's up , Doc?"
answer_characters = answer_characters.upper()
answer_guesses = []

for current_answer_character in answer_characters:
  if re.search("^[A-Z]$", current_answer_character):
    answer_guesses.append(False)
  else:
    answer_guesses.append(True)

#logic
guessed_letters=[]
num_of_incorrect_guesses = 0

while num_of_incorrect_guesses < 5 and False in answer_guesses:
  print("------------------")
  print("Guessed Letters: ", end = "")
  
  for current_guessed_letter in guessed_letters:
    print(f"{current_guessed_letter} ", end = "")

  print()
  print(f"Number of incorrect guesses remaining: {5 - num_of_incorrect_guesses}")
  print()
 
    
  for answer_index in range(len(answer_characters)):
    if answer_guesses[answer_index]:
      print(answer_characters[answer_index], end = "")
    else:
      print ("_", end = "")
  
  print ()
  print("------------------")      
  letter = input("Enter a Letter: ")
  
  letter = letter.upper()


  if letter not in guessed_letters and len(letter) == 1 and re.search("^[A-Z]$", letter):
   guessed_letters_insert_index = 0
   for current_guessed_letters in guessed_letters:
     if letter < current_guessed_letter:
      break
     guessed_letters_insert_index += 1
   guessed_letters.insert(guessed_letters_insert_index, letter)
   if letter in answer_characters:
     for current_answer_index in range(len(answer_characters)):
       if letter == answer_characters[current_answer_index]:
         answer_guesses[current_answer_index] = True
   else:
     num_of_incorrect_guesses += 1

#gameover

if num_of_incorrect_guesses < 5:
  print()
  print("Congratulations!!!")
else:
  print()
  print("Sorry, you ran out of guesses...")

print(f"{answer_characters} is the answer to the puzzle.")