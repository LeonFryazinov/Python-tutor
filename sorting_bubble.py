import random #python does not have many functionality in its base self, to get more features, you can import "libraries and modules" to add more features. Random gives elements
#of randomness as a feature. In this project, we use this library, which adds additional functions, to randomise our list so that we can sort it.
import time #same as the other import, 
mylist = [] # the creation of our list that we will sort (smallest to highest)
if True: # IGNORE THIS, THIS IS NOT SOMETHING WE DID TOGETHER, this is the randomiser that randomises our list. 
    for i in range(16):
        mylist.append(random.randint(0,16))
print(mylist)#prints the randomised list that waws created line 5-7, ignore that code as it is not something we covered yet, but if you want to try to understand it, go ahead 


while True: # A "Forever loop" that will run forever, until our code has sorted the list and detects that it is sorted on line 22, then it stops the loop using the keyword "break"
    swaps = 0 # a variable used to detect how many "swaps" our code does, if no numbers in our list need to be swapped, then it is sorted.
    counter = 0 # counts what number in the list we are currently swapping
    while counter < len(mylist): # the loop that will swap the numbers until they are sorted
        if mylist[counter] > mylist[counter+1]: # if the number infront of the current number is smaller, then we need to swap the two numbers 
            # an example would be [1,7,3] if we were currently looking at the number 7, the number after that (3) is smaller, so 7 and 3 should be swapped
            temp = mylist[counter]
            mylist[counter] = mylist[counter+1]
            mylist[counter+1] = temp # the last three lines are here to swap the numbers, because when "seting" a variable or something in a list, it overwrites it, 
                                    # we need a temporary variable to store the number being overwritten so we can swap them. 
            swaps = swaps + 1 # The swaps variable counts how many times we do the swapping, if we dont swap at all, the list is sorted and there is no need to run the loop
        counter += 1
    
    if swaps == 0: # as i said on line 23, if nothing is being swapped, it is sorted and no need to run the loop, break keyword leaves the forever loop
        break




