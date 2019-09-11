#include<stdio.h>
int main(void)
{
    int a[100],n,i,count1=0,count2=0,count3=0;
    float sum1,sum2,sum3;
    printf("Enter the number:");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        if(a[i]<0)
        {
            count1=count1+1;
        }
        else if(a[i]>0)
        {
            count2=count2+1;
        }
        else
            count3=count3+1;
    }
    sum2=(float)count2/n;
    printf("%6f\n",sum2);
    sum1=(float)count1/n;
    printf("%6f\n",sum1);
    sum3=(float)count3/n;
    printf("%6f\n",sum3);
    return 0;
}
