
question_bank = [
    ["What is Python", "low-level lang", "high-level lang", "medium-level lang", "none"],
    ["What is PEP 8?", "Pip Package", "Python protocols", "Python Enhancement Proposal", "none"],
    ["Type of list?", "dynamic", "immutable", "mutable", "none"],
    ["Which makes set?", "[]", "()", "{}", "''"],
    ["int('10.5')?", "10", "10.5", "Error", "none"],
    ["id() use?", "data type", "memory address", "copy var", "none"],
    ["Output of 2**3?", "6", "8", "9", "Error"],
    ["len('abc')?", "2", "4", "3", "Error"],
    ["float(5)?", "none", "0.5", "5.0", "Error"],
    ["Which is tuple?", "[1]", "{1}", "none", "(1,)"],
    ["What is pass?", "break", "skip loop", "none", "do nothing"],
    ["x=5; x//=2?", "3", "2", "2.5", "none"],
    ["range(1,5)?", "1–5", "0–5", "1–4", "none"],
    ["type([])?", "tuple", "list", "set", "none"],
    ["str[0:2] of 'Python'?", "Pyt", "Py", "th", "Error"],
    ["Output of 'A'>'B'?", "True", "False", "Error", "none"]
]
answer_bank = ["high-level lang", "Python Enhancement Proposal", "mutable", "{}", "Error", "memory address", "8", "3", "5.0", "(1,)", "do nothing", "2", "1–4", "list", "Py", "False"]
points=[1000,2000,5000,10000,20000,40000,80000,120000,320000,640000,2500000,5000000,10000000,20000000,50000000,70000000]
quit=False
score=0
print("----------------------------------------------------------------------")
print("\t\t\t\tKBC QUIX\t\t")
print("----------------------------------------------------------------------")
while True:
    for i in range(0,len(question_bank)):
        if quit:
            break
        choice=int(input("\n\tEnter 1 for next question, 0 for quit: "))
        if(choice==1):
            ans=int(input(f"\n->QUESTION {i+1}: {question_bank[i][0]}\n1.{question_bank[i][1]}\t 2.{question_bank[i][2]}\n3.{question_bank[i][3]} \t 4.{question_bank[i][4]} \n(e.g. enter (1/2/3/4) or 0 for lifeline )    :    "))
            if(question_bank[i][ans]==answer_bank[i]):
                print(f"\n\t>>>>>{points[i]} points EARNED<<<<<")
                score=score+points[i]
            elif(ans==0):
                print("\n\t>>>NOW You Are Given 2 Chances : ")
                for j in range(0,3):
                     ans=int(input(f"\n->QUESTION {i+1}: {question_bank[i][0]}\n1.{question_bank[i][1]}\t 2.{question_bank[i][2]}\n3.{question_bank[i][3]} \t 4.{question_bank[i][4]} \n(e.g. enter (1/2/3/4)    :    "))
                     if(question_bank[i][ans]==answer_bank[i]):
                        print(f"\n\t>>>>>{points[i]} points EARNED<<<<<")
                        score=score+points[i]
                        break
                     elif(j==2):
                         quit=True
                         break
                            
                     else:
                        print("\n\tWRONG INPUT TRY AGAIN")

            else:
                 if(score>points[3]):
                    score=points[3]
                 elif(score>points[8]):
                    score=points[8]
                 quit=True
                 print("\tWRONG INPUT")
        elif(choice==0):
            quit=True
            break
        else:
            print("\tWRONG INPUT")
        


    if quit:
        print("\n----------------------------------------------------------------------")
        print("\t\tYOUR TOTAL SCORE : ",score)
        print("----------------------------------------------------------------------")
        print("\t\t\t\tEND OF GAME\t\t")
        print("----------------------------------------------------------------------")
        break
