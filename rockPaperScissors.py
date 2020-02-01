
#set variable keepPlaying to true

keepPlaying = True

#While keepPlaying is true:

while keepPlaying == True:
    print("Welcome to Rock, Paper, Scissors!")
    print("The way you will play is you will choose 1 for rock, 2 for paper, 3 for scissors. Rock beats scissors, paper beats rock, and scissors beats paper. The game will be best 2 out of 3. If you wish to quit, you can type q.")

    #print statement welcoming players to the game
    #print statement stating the rules (best 2 out of 3. Press 'q' to quit)
    
    #make a key that assigns a number to each choice for the computer
    #(rock is 1, scissors is 2, paper is 3)
    '''rock = 1
    paper = 2
    scissors = 3 '''
    #import the random function - the computer makes its choice randomly from this function
    
    import random
    #set computer's score to 0
    cpu = 0
    #set player's score to 0
    player = 0
    #while player's score is less than 2 and computer's score is less than 2:
    while((player < 2) and (cpu < 2)):
        cpuChoice = random.randint(1,3)
        #computer's choice = random number between 1 and 3 (random function gets used here)
        #player's choice = input(ask player to select Rock, Paper, or Scissors)
        playerChoice = input("Pick 1, 2, or 3: ")
        #start checking user options
        #userChoice = userChoice.lower()
        #if players inputs 'q':
        if(playerChoice == "q"):
            keepPlaying = False
            break
            #set keepPlaying to False
            #stop the loop
        elif(((playerChoice == "1") and (cpuChoice == 1)) or ((playerChoice == "2") and (cpuChoice == 2)) or ((playerChoice == "3") and (cpuChoice == 3))):
            print("Draw!")
            print("Computer Score:" + str( cpu))
            print("Player Score:" + str( player))
        #else if (player inputs rock and computer chooses rock) or
        #(player inputs paper and computer chooses paper) or 
        #(player inputs scissors and computer chooses scissors):
            #print out DRAW
            #print out player's score and computer's score
        elif(((playerChoice == "1") and (cpuChoice == 3)) or ((playerChoice == "2") and (cpuChoice == 1)) or ((playerChoice == "3") and (cpuChoice == 2))):
            player += 1
            print("You won this round!")
            print("Computer Score:" + str( cpu))
            print("Player Score:" + str( player))  
        #else if (player inputs rock and computer scissors) or
        #(player inputs scissors and computer chooses paper) or
        #(player inputs papers and computer chooses rock):
            #add one to the player's score
            #print out player's score and computer's score
        elif(((playerChoice == "1") and (cpuChoice == 2)) or ((playerChoice == "2") and (cpuChoice == 3)) or ((playerChoice == "3") and (cpuChoice == 1))):
            cpu += 1
            print("You lost this round :(")
            print("Computer Score:" + str( cpu))
            print("Player Score:" + str( player))    
        #else if (player inputs rock and computer paper) or
        #(player inputs scissors and computer rock) or
        #(player inputs paper and computer scissors):
            #add onne to the computer's score
            #print out player's score and computer's score
        else:
            print("Your input was invalid, try again...")
        #else:
            #tell the user their input was invalid

    if player >= 2:
        print("Congrats! You won... thanks for playing!")
    elif cpu >= 2:
        print("Oh no! You lost... thanks for playing.")
    print("Computer Score: " + str(cpu))
    print("Player Score: " + str(player)) 
        #print statement tanking the players for playing
        #if player's score is 2:
            #print statement letting the player know they won
        #if computer's score is 2:
            #print statement letting player know that the computer won
        #print out the player's score and computer's score