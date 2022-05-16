# ==========Exercise==================

initialList = [32, 5, 12, 8, 3, 75, 2, 15]
even = []
odd = []

i = 0
while i < len(initialList):
    if initialList[i] % 2 == 0:
         even.append(initialList[i])
    else:
         odd.append(initialList[i])
    i = i + 1

print ("even number:", even)
print ("Odd number :", odd)