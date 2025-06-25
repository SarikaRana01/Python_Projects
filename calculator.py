while True:
        choice=int(input("Enter 0 for action perform ,1 for quit ,2 for view history ,3 for clear history : "))
        if(choice==0):
            expression=input("Enter the expression(must be 2 digits(0<=n<=9) and 1 operator(+,-,/,%,//,*,**)) e.g.(8+8) : ")
            if not (len(expression)==3):
                print("WRONG INPUT")
                break
            num1=float(expression[0])
            num2=float(expression[2])
            operator=expression[1]
            if(operator=='+'):
                result=num1+num2
                print(f"ANS : {result}")
                with open("history_sheet.txt",'a') as file:
                    file.write(f" {expression} = {result}\n")
            elif(operator=='-'):
                result=num1-num2
                print(f"ANS : {result}")
                with open("history_sheet.txt",'a') as file:
                    file.write(f" {expression} = {result}\n")
            elif(operator=='/'):
                result=num1/num2
                print(f"ANS : {result}")
                with open("history_sheet.txt",'a') as file:
                    file.write(f" {expression} = {result}\n")
            elif(operator=='%'):
                result=num1%num2
                print(f"ANS : {result}")
                with open("history_sheet.txt",'a') as file:
                    file.write(f" {expression} = {result}\n")
            elif(operator=='//'):
                result=num1//num2
                print(f"ANS : {result}")
                with open("history_sheet.txt",'a') as file:
                    file.write(f" {expression} = {result}\n")
            elif(operator=='*'):
                result=num1*num2
                print(f"ANS : {result}")
                with open("history_sheet.txt",'a') as file:
                    file.write(f" {expression} = {result}\n")
            elif(operator=='**'):
                result=num1**num2
                print(f"ANS : {result}")
                with open("history_sheet.txt",'a') as file:
                    file.write(f" {expression} = {result}\n")
            else:
                print("WRONG INPUT")
        elif(choice==1):
            print("EXIT")
            break
        elif(choice==2):
            with open("history_sheet.txt",'r') as file:
                  lst= file.readlines()
                  for i in lst:
                        print(i)
        elif(choice==3):
            with open("history_sheet.txt",'w') as file:
                  file.write("")
            print("HISTORY CLEARED")
        else:
            print("WRONG INPUT")

print("END OF PROGRAM")


                      
                      
            
        


