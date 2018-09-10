import random #importing random to choose a random word from the list
def Hangman_Game(): #making a function
   gameOver=False #Boolean to check whether game ended
   count = 0
   hangman = []
   wordList = ["firewood", "snowstorm", "snowman","trump","morals", "funny", "chair", "flirt", "steak", "computer"]
   choice=random.randrange(len(wordList)) #choose random index
   answer = wordList[choice]#answer is the actual word at that index
   i = 0 #makes sure you start from beginning
   nTries = 0
   counter=6 #making 6 tries
   for char in answer:  #for each letter in the word you will guess, you are making enough blanks
       hangman.append("_") #appending blanks
   answer=list(answer) #turning the word into a list form to go through them easier
   guessed=[] #list of guessed letters
   while("_" in hangman): #while there are blanks in the word that needs to be guessed, keep looping through
      print(hangman) #displaying the state of the game
      print("Tried letters:", guessed) #print Tried letters
      guess=input("Type a letter:") #ask to enter a letter
      if guess not in guessed: #if the letter you entered is not in the letters you already guessed
         if guess in answer: #if the letter you guessed is in the actual word, then do a loop which goes through each character and reveals the letter if it matches the one you guessed
            for i in range(len(answer)):
               if answer[i]==guess:
                  hangman[i]=guess
         else: #if the letter you guessed is not in the actual word, then substract the amount of tries
            counter-=1 #decreasing the amount of tries
         guessed.append(guess) #appending the letter you guessed to the list of guessed letters
      else: #tells you if you guessed the letter already
         print("You already guessed this letter")
      if(counter==0): #if there are no more tries left, end the game
         print("GAME OVER!")
         gameOver=True #sends the boolean to true implying the game is over
         break #a way to exit the loop so the game does not keep running
      else: #if you do have more tries, then display the amount of tries you have left
         if(counter!=1): #if there is one try left, then print there is one try remainining vs. "tries" remaining
            print("You have {} tries remaining!".format(counter))
         else:
            print("You have 1 try remaining!")
      nTries += 1
   if(gameOver): #if you ran out of tries and the game is over, print "try again next time"
      print("Try again next time")
   else: #otherwise they won and display the amount of tries it took
      print("You win! Number of total guesses it took:{} ".format(nTries))
Hangman_Game()
