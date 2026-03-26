s = {}

def l(a):
    b = a.replace('=', ' = ').replace('+', ' + ').split()
    print("Tokens : ", b)
    return b

def m(a):
    for b in a:
        if b.isalpha() and b not in s:
            s[b] = len(s) + 100

def n(a):
    print("t1 =", a[2], a[3], a[4])
    print(a[0], "= t1")

def r(a):
    b = l(a)

    m(b)
    print("Symbol table : ", s)

    print("ICG : ")
    n(b)

r("a=b+c")