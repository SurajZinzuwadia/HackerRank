#include<stdio.h>
int main()
{
    int i,j,n,m,k;
    scanf("%d",&n);
    m=n;
    for(i=0;i<n;i++)
    {
        for(j=m-1;j>0;j--)
        {
            printf("\t");
        }
        for(k=0;k<=i;k++)
        printf("#\t");
        printf("\n");
        m--;
    }

    return 0;
}
