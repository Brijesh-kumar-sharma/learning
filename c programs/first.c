#include<stdio.h>
#include<stdlib.h>
int  main()
{

int a,b,sum,operator,t,c;
printf("Enter first number\n");
scanf("%d",&a);
printf("Enter second number\n");
scanf("%d",&b);

do{
printf(" 1.) Enter 1 for Addition\n 2.) Enter 2 for Subtraction \n 3.) Enter 3 for Multiplication \n 4.) Enter 4 for Divide\n");
scanf("%d",&operator);

if(operator==1)
{
sum=a+b;
printf("Result is %d\n",sum);
}
else if(operator==2)
{
sum=a-b;
printf("Result is %d\n",sum);
}
else if(operator==3)
{
sum=a*b;
printf("Result is %d\n",sum);
}
else if(operator==4)
{
sum=a/b;
printf("Result is %d\n",sum);
}
else
{
printf("Operation not defined");
}
printf(" 'You Want to perform opertion again or not'\n Enter 0 for continue else press anything for not\n");
scanf("%d",&c);
if(c==0)
{
    printf("Enter the mumber\n");
    scanf("%d",&t);
    a=sum;
    b=t;
}
else
{
    printf("Thanks for Using This");
    exit(0);
}

}while(c==0|| c==0);




return 0;



}