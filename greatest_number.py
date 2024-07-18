def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b 
    elif(c>b and c>a):
        return c 
    
    
a = 100
b = 90
c = 80


    
print(greatest(a, b, c))