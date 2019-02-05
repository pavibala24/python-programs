#include<stdio.h>
#include<string.h>
void main()
{
	char name[20];
	int i;
	printf("Enter the string");
	scanf("%s",name);
	for(i=0;name[i]!='\0';i++)
	{
	if(name[i]>='a'&&name[i]<='z')
	printf("%3c",name[i]-32);
	printf("%c",name[i]);
	}
}
