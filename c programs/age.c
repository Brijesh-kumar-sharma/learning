#include<stdio.h>
int main()
{

int d1,m1,y1,d2,y2,m2,r1,r2,r3,nu;
printf("===============================================================================================\n");
printf("                                             Age Calculator                                    \n");
printf("===============================================================================================\n");
printf("Enter Birthday Date\n");
scanf("%d",&d1);
printf("Enter Birthday Month \n");
scanf("%d",&m1);
printf("Enter Birthday Year \n");
scanf("%d",&y1);
printf("Enter Current Date \n");
scanf("%d",&d2);
printf("Enter Current Month \n");
scanf("%d",&m2);
printf("Enter Current Year \n");
scanf("%d",&y2);
if(((d1<1 || d1>30) && (m1<1 || m2>12) && (y1<0 ))&&((d1<1 || d1>30) && (m1<1 || m2>12) && (y1<0 )))
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
    else
    {

        d2=d2+30;
        r2=d2-d1;
        m2=m2-1;

    }
    if(m2>=m1)
    {
        r2=m2-m1;
    }
    else
    {   m2=m2+12;
       r2=m2-m1;
       r3=r3-1;

    }


    if(d1==d2 && m1==m2)
    {
        printf("Happy Birthday\n");
    }
    printf("Your Age is %d Year %d Month %d days",r3,r2,r1);
    
   
  
    
}

return 0;






}