operator = input("what operator do you want: ") # gets the operator from 

num1 = input() #string -> text
num2 = input() #string -> text


if operator == "+": # checks if the the operator inputed is a plus, then adds if it is.
    answer = float(num1) + float(num2) # coverting to number then doing the corrisponding operation
    
    print(num1+"+"+num2+"="+str(answer)) #prints the results
if operator == "-": # checks if the the operator inputed is a minus, then subtracts if it is.
    answer = float(num1) - float(num2) # coverting to number then doing the corrisponding operation
    
    print(num1+"-"+num2+"="+str(answer)) #prints the results
if operator == "*": # checks if the the operator inputed is a multiply symbol (instead of an x, programers use the star), then Multiplies if it is.
    answer = float(num1) * float(num2) # coverting to number then doing the corrisponding operation
    
    print(num1+"*"+num2+"="+str(answer)) #prints the results
if operator == "/": # checks if the the operator inputed is a division symbol (instead of an devision symbol, programers use the slash), 
                    #then divides if it is.
    
    
    answer = float(num1) / float(num2) # coverting to number then doing the corrisponding operation
    
    print(num1+"/"+num2+"="+str(answer)) #prints the results

