p1 = "buy now"
p2 ="nice video"
p3 = "subscribe this"
p4 = "click this"

message =input("Enter your comment:")
if((p1 in message) or (p2 in message )or (p3 in message )or (p4 in message )):
    print("This comment is spam")
    
else:
    print("This comment is not spam")