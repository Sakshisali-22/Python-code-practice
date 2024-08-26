class demo:
    a = 4
    
    
o = demo()
print(o.a)# print the class attribute because instance attribute is not present

o.a =0 #Instance attribute is set

print(o.a)#print the instance attribute because instance attribute is set

print(demo.a) #print the class attribute 

    