//Project Euler #9
//Last Edit : 29.3.17 16.37

#include <stdio.h>
#include <math.h>


int main()
{
	const int sum = 1000;
	//sum = a+b+c
	//theorem : a^2+b^2=c^2 , a<b<c
	int a,b,c;
	
	for(a=1 ; a < (sum-3)/3 ; a++)
	{
		for(b=a+1 ; b<(sum-a)/2 ; b++)
		//Used b = a+1 for preventing errors
		{
			c = sum - (a+b) ;
			if(pow(a,2)+pow(b,2) == pow(c,2))
				printf("%d",a*b*c);
		}
	}

	return 0;
}


