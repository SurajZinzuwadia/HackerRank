//Gridland train track program
#include<stdio.h>
void main()
{
    int a[3][2],i,j,sum=0;
    for(i=0;i<4;i++)
    {
        for(j=0;j<3;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    for(i=0;i<4;i++)
    {
        if(a[i][1] < a[i][2])
        {
            if((a[i][2]-a[i][1])==3)
            {
                sum = sum + 0;
            }
            else if((a[i][2] - a[i][1])==2)
            {
                sum = sum + 1;
            }
            else if((a[i][2] - a[i][1])==1)
            {
                sum = sum + 2;
            }
        }
    }printf("%d",sum);
}
