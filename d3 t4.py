a=str(input("请输入任意正整数:"))
i=0
j=len(a)-1
while(i<j):
    if(a[i]!=a[j]):
        print("No")
        break
    i+=1
    j-=1
if(i>=j):
    print("Yes")