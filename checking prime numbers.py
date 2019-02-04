n = 350
if n > 1:
for i in range(2,n):
if (n % i) == 0:
print(n,"is not a PRIME NUMBER")
print(i,"times",n//i,"is",n)
break
else:
print(n,"is a PRIME NUMBER")
else:
print(n,"is not a PRIME NUMBER")
