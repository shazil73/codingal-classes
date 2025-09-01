def shazil (a, b):
    print("function is running")
    return a + b

result = shazil(565, 683)
print(result)

def shazil2 (a, b, c, d):
    print("function is running")
    return a * b + c - d

ans = shazil2(5, 6, 7, 8)
print(ans)

def hello (n):
    if n == 0:
        return 
    print(n)
    hello(n-1)

hello(5)

