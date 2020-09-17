#include<stdio.h>
int main()
{
int a,b,sum,operator,k,m;
printf("Enter a number\n");
scanf("%d",&a);
printf("Enter second number\n");
scanf("%d",&b);
do{
printf(" 1.) Enter 1 for Addition\n 2.) Enter 2 for Subtraction \n 3.) Enter 3 for Multiplication \n 4.) Enter 4 for Division\n");
scanf("%d",&operator);
if(operator== 1)
{
    sum=a+b;
    printf("Result of %d and %d is %d",a,b,sum);
}
else if(operator== 2)
{
    sum=a-b;
    printf("Result of %d and %d is %d",a,b,sum);
}
else if(operator== 3)
{
    sum=a*b;
    printf("Result of %d and %d is %d",a,b,sum);
}
else if(operator== 4)
{
    sum=a/b;
    printf("Result of %d and %d is %d",a,b,sum);
}
else
{
    printf("The operation doesn't exist");
}
printf("\nDo you want to continue \nEnter 0 for continue or anything else not\n");
scanf("%d",&k);
if(k==0)
{
printf("Enter a number\n");
scanf("%d",&m);
a=sum;
b=m;

}
else
{
    printf("Thanks for using this");
}




}while(k==0);

return 0;








}