x=int(input("enter a number"))
y=x
s=0
z=len(str(x))
while(y>0):
    r=y%10
    s+=(r**z)
    y//=10
if(s==x):
    print("armstrong") 
else:
    print("not armstrong")       