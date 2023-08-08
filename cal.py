def Calculator():
    #num1 = float(input( "Enter the first no)")) 
    #num2 = float (input("Enter the second no"))
    numbers = []

    while True:
        num = input("Enter a number (or 'done' to finish): ")

        if num == "done":
            break
#float(num)` is used to convert the string `num` into a floating-point number        
        numbers.append(float(num))  # Add the entered number to the list

    
    operation = (input(" Choose an operation   (+ , -,*, /):"))
# we use sum function because list having  more than 2 numbers 
    if operation == '+':
        result = sum(numbers)
    elif  operation == '-':
 #  list first contain 0 pos index and then - sum(numbers[1:])means index pos ke 1 se leke jitna user number
 # diya hoga utna add karega sum karke  0 index pos se - minus karega        
        result = numbers[0] - sum(numbers[1:]) 

    elif  operation == '*':

        result = 1 
        for num in numbers:
            result *= num 

    elif  operation == '/':
         result = numbers[0]
         for num in numbers[1:]:
            result /= num

    else:
        print("Invalid operation ")
        

    print("The result is: ",result) 

Calculator()    







