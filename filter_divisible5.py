def Divisible5(n):
    if(n%5 ==0):
        return True
    return False

a = [1,333,55,44,888,15,35] 

f =list(filter(Divisible5,a))

print(f)