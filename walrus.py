#using walrus operator 
if (n:= len([1,2,3,4,5])) > 3:
    print(f"List is to long( {n} element, expected <=3)") 
# output: List is to long (5 element , expected <=3)
    