# Count Digit

user_input = int(input("Enter the number: "))
counter=0

while user_input > 0:
    user_input = user_input // 10
    counter +=1
    
print(counter)