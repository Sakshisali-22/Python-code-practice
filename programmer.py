class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin): 
        
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = programmer("Harry", 1200000, 425109)
print(p.name,p.salary,p.pin,p.company)