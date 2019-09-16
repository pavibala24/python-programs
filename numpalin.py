n=int(input())
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if (rev%10==0):
    trim(rev)
    print(rev)
else:
    print(rev)
