str = input("enter a string of characters")
 
recopy = ""
for copyStr in str:
    recopy += copyStr + '*'
recopy = recopy[0:-1]
 
print(recopy)