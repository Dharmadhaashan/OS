expr = input("Enter expression : ")

expr = list(expr)

temp = 1
print("\nThree Address Code:\n")

for op in ['*','/']:
    while op in expr:
        i = expr.index(op)
        left = expr[i-1]
        right = expr[i+1]

        t = "t" +str(temp)
        temp =temp+1

        print(t,"=",left,op,right)

        expr[i-1:i+2] = [t]

for op in ['+','-']:
    while op in expr:
        i = expr.index(op)
        left = expr[i-1]
        right = expr[i+1]

        t = "t"+str(temp)
        temp = temp+1

        print(t,"=",left,op,right)

        expr[i-1:i+2] = [t]

print("\nFInal Result: ",expr)