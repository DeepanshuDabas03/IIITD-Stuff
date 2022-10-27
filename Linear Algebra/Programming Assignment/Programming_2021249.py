#First we took input of set from user also providing format 
print("Sample Input: (0,0,0,0),(1,0,1,0),(0,0,1,1),(1,1,1,1)")
t=input("Please enter comma separated set in same format as sample input: ")
#Then we removed extra brackets and commas in order to convert  elements into list
t=t.replace("(","")
t=t.replace(")","")
t=t.replace(","," ")
t=t.split()
#After converting it into list we created two empty list in one list we stored elements as a string and in another list we stored element as int for example 0000 will be 0 in int value therefore every number in set will have different value
#We compared these int values only of the tuple like for example we compared 1000 int value which will be same as 1000
q=[]
o=[]
a=int(len(t)/4)
for i in range(a):
    s=str(t[4*i])+str(t[4*i+1])+str(t[4*i+2])+str(t[4*i+3])
    q.append(s)
    o.append(int(s))
#after creating our required lists, then we do addition first and then replace1+1=2 with 0 (Converted it into string first and later on into int for comparison)
#For checking if it is in subspace we compared second list(contating int values)and used if set not in it then we added 1 to an arbitary number m(inital value 0)
#If it is a subspace then not in "loop will not be executed at any time therefroe value of m will remain 0 only

m=0
for i in range(len(q)):
    for j in range(len(q)):
        s=int(q[i])+int(q[j])
        s=str(s)
        s=s.replace("2","0")
        s=int(s)
        if s not in o:
            m+=1
#Used nested for loop for multiplication(fixed range of inner loop to 2 therefire it will multiply tuple by 0 and 1 respectively and then we will compare it in orignal space if it is there or not,If not then we will be adding 1 to m)
for i in q:
    for j in range(2):
        s=int(i)*j
        if s not in o:
            m+=1
#We used if else loop to check value of m. If it is greater than or equal to 1 then it is not subspace of set and if it is equal to 0 then it is subspace of set and true will be the result
if m>=1:
    print("Result: False")
else:
    print("Result: True")