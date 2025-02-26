import random # modules add us more functions (blocks in scratch) that we can use, but to use them, we need to import them
value = 0# this is a game where the player has to get to below 21, this variable tracks what number was said.
while True: # repeats the game infinitly 
    user_num = input("A number between 1 and 3: ") # the user is asked for a number between 1 and 3, and their response is stored in a variable.
    while not user_num in ["1", "2", "3"]: # checks if the user inputed something we dont want and repeatedly ask them for a "correct" number until they give us one.
        print("that number was not in the range") #part if the wrong number system i explained last line
        user_num = input("A number between 1 and 3: ")
    
    
    value += int(user_num) # if the value is 1, 2 or 3, we add this number to the total. you might see the int() function, it is there because the user_num is a string (a bit of text)
                           # and not a proper number, so we cant do addition with it.
    
    
    print(value) #prints the value, you know this

    if value >= 21: # if after the players turn the total number is above or equal to 21, they have lost, so this if statement checks that.l
        print("player lost") # this code tells the player that they lost and then resets the game (on the next line)
        value = 0
    

    value += random.randrange(1,3) # the computer has their turn by generating a random value between 1 and 3 then adds it 

    print(value)
    if value >= 21: # does the same for the computer as on line 16, so go to line 16 for the explaination.
        print("computer lost")
        value = 0