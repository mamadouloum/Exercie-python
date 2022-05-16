t1=['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
i=0
t2=[] 
t3=[]  
for nom in t1:
    if len(nom)<6:
        t2.append(nom)
    else:
        t3.append(nom)
print("la 1er liste:",t2)
print("la deuxiéme liste:",t3)