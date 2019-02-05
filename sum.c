#include<stdio.h>
void main()
{
int v,b,sum=1,i;
scanf("%d",&v);
scanf("%d",&b);
for(i=1;i<=b;i++)
{
sum=sum*v;
}
printf("%d",sum);
}
