#include <stdio.h>

int main()
{
    int i,j,n;
    scanf("%d",&n);
    for (i=0;i<n;i++)
    {
        for (j=i;j<n;j++)
        {
            printf("1");
        }
        printf("\n");
    }
    return 0;
}
