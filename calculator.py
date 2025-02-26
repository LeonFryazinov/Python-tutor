operator = input("what operator do you want: ") # gets the operator from 

num1 = input() #string - text
num2 = input() #string - text


if operator == "+":
    answer = float(num1) + float(num2) # coverting to number
    
    print(num1+"+"+num2+"="+str(answer))
if operator == "-":
    answer = float(num1) - float(num2) # coverting to number
    
    print(num1+"-"+num2+"="+str(answer))
if operator == "*":
    answer = float(num1) * float(num2) # coverting to number
    
    print(num1+"*"+num2+"="+str(answer))
if operator == "/":
    answer = float(num1) / float(num2) # coverting to number
    
    print(num1+"/"+num2+"="+str(answer))

