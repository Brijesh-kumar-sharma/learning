#include<stdio.h>
int main()
{

int d1,m1,y1,d2,m2,y2,r1,r2,r3;

printf("====================================================================================\n");
printf("                                             Age Calculator                         \n");
printf("====================================================================================\n");

printf("Enter Your Birthday day");
scanf("%d",&d1);
printf("Enter Your Birthday Month");
scanf("%d",&m1);
printf("Enter Your Birthday Year");
scanf("%d",&y1);
printf("Enter Your Current day");
scanf("%d",&d2);
printf("Enter Your Current Month");
scanf("%d",&m2);
printf("Enter Your Current Year");
scanf("%d",&y2);
if((d1 > 31 || d1 <1) ||(d2 > 31 || d2 <1) || (m1<1 || m1>12) || (m2<1 || m2>12) || (y1<0 && y2<0))
{
    printf("You Enter Wrong Something Try Again");

}
else
{
    
    r3=y2-y1;
    if(d2>=d1)
    {
        r1=d2-d1;
    }
    else{
        m2=m2-1;
        d2=d2+30;
        r1=d2-d1;

    }
    if(m2>=m1)
    {
        r2=m2-m1;
    }
    else{
       r3=r3-1;
       m2=m2+12;
       r2=m2-m1;

    }


printf("Your AGe is %d day %d month %d year",r1,r2,r3);
}

















}