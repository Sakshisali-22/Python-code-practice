from random import randint

class Train:
    
    def __init__(self,tranNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from{fro} to {to}")
        
         
    def getstatus(self):
        print(f"Train no: {self,traiNo}is running on time")
        
    def getFare(self,fro, to):
        print(f"Ticket fare in train no:{self.trainNo} from {fro} to {to} is 
        {randint(222,555)}")
        )
        
        
        
t = Train(12399)
t.book("Rampur","Delhi") 
t.getstatus()
t.getFare("Rampur","Delhi")
            
        
        
        
                  
        
        
        

    
    

    
    
 