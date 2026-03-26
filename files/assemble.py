code = ["t1 = a + b","t2 = t1 * c"]
reg = 1

for line in code:
    left , right = line.split('=')
    left = left.strip()
    a,op,b = right.strip().split()

    print("MOV R"+str(reg)+",",a)

    if op == '+':
        print("ADD R"+str(reg)+",",b)
    elif op == '-':
        print("SUB R"+str(reg)+",",b)
    elif op == '*':
        print("MUL R"+str(reg)+",",b)
    elif op =='/':
        print("DIV R"+str(reg)+",",b)

    print("MOV",left + ", R"+str(reg))
    print()

    reg +=1