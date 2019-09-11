num = int(input())
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print("no")
           break
   else:
       print("yes")
