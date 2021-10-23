pin = '0805'
    
for y in range (3):
    x = input("Enter the 4-digit pin: ")
        
    if x==pin:
        Print("Pin correct. Payment has been processed")
        break
    
    if x!=pin:
        print("Incorrect")
        
    if y==2:
        print("Sorry your payment couldn't be processed")