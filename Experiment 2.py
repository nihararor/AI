# Write a Program to implement Tautology, Contradiction and satisfiable

#tautology
p=[True,True,False,False]
q=[True,False,True,False]
l1=list()
l2=list()
l3=list()

for i in range(0,4):
    l1.append(not p[i] or q[i])
    l2.append(not q[i] or p[i])
    l3.append(l1[i] or l2[i])
print(l1)
print(l2)
print(l3)


#Contradiction
p=[True,True,False,False]
q=[True,False,True,False]
l1=list()
l2=list()
l3=list()

for i in range(0,4):
    l1.append(not p[i] and  q[i])
    l2.append(p[i] and not q[i])
    l3.append(l1[i] and l2[i])

print(l1)
print(l2)
print(l3)

#satisfiable
p=[True,True,False,False]
q=[True,False,True,False]
l1=list()
l2=list()
r=[False,False,False,False]
for i in range(0,4):
    l1.append(not p[i] or q[i])
    l2.append(r)
print(l1)
if(l1[0]==True or l1[1]==True or l1[2]==True or l1[3]==True):
    print("Satisfiable")
else:
    print("Not satisfied")

if(l2[0]==True or l2[1]==True or l2[2]==True or l2[3]==True):
    print("Satisfiable")
else:
    print("Not satisfied")


'''#Method 2
p=[True,True,False,False]
q=[True,False,True,False]
while(1):
    n = int(input("Enter the number corresponding to the smybol : \n1. not \n2. implies \n3. union \n4. intersection \n5. Biconditional\n6.or\n7.and\n8. (p->q)->(~q->~p)\n"))
    l=list()

# negation
    if(n==1):
        x = int(input("Negation of which number : \n1. p \n2. q \n"))
        l=list()
        if(x==1):
            for i in range(len(p)):
                l.append((p[i] + 1) % 2)
        elif(x==2):
            for i in range(len(q)):
                l.append((q[i] + 1) % 2)
        else:
            print("Wrong Choice")

# implies
    elif(n==2):
        x = int(input("implies of which number : \n1. p->q \n2. q->p\n"))
        l = list()
        if(x==1):
            for i in range(len(p)):
                if(q[i] == 0 and p[i] == 1):
                    l.append(0)
                else:
                    l.append(1)
            
        else:
            for i in range(len(p)):
                if(q[i] == 1 and p[i] == 0):
                    l.append(0)
                else:
                    l.append(1)
        

# union
    elif(n==3):
        c=list()
        for i in range(len(p)):
            if(q[i] == 0 and p[i] == 0):
                l.append(0)
            else:
                l.append(1)

#intersection
    elif(n==4):
        l=list()
        for i in range(len(p)):
            if(q[i] == 1 and p[i] == 1):
                l.append(1)
            else:
                l.append(0)

# bidirectional 
    elif(n==5):
        l = list()
        for i in range(len(p)):
            if(q[i] == p[i]):
                l.append(1)
            else:
                l.append(0)

#or
    elif(n==6):
        l=list()
        l1=list()
        l2=list()
        for i in range(len(p)):
            l1.append(not p[i] or q[i])
            l2.append(not q[i] or p[i])
            l.append(l1[i] or l2[i])

#and
    elif(n==7):
        l=list()
        l1=list()
        l2=list()
        for i in range(len(p)):
            l1.append(not p[i] and  q[i])
            l2.append(p[i] and not q[i])
            l.append(l1[i] and l2[i])

    elif(n==8):
        l1=list()
        l2=list()
        l=list()
        

        for i in range(len(p)):
            l1.append(not p[i] or q[i])
            l2.append(not q[i] or p[i])
            l.append(l1[i] or l2[i])

            

        
    print(l)

    if(l == False or any(l) == True):
        print("Satisfiable ...")
    if(l[0] == False and l[1] == False and l[2] == False and l[3] == False):
        print("Contingency ...")
    if (l[0]==True and l[1]==True and l[2]==True and l[3]==True):
        print("Tautology ...")
'''

    