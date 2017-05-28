//Project Euler #2
//Last Edit : 25.3.17 - 19:36

#include <stdio.h>
#include <stdlib.h>

#define last 4000000 //Makes program faster

int fibonacci(); //Calculates the sum of all even fibonacci numbers bellow 4 million

int main()
{
	fibonacci();
	int result = fibonacci();
	printf("%d",result);


	return 0;
}//main ends

int fibonacci() 
	//returns sum of even fibonacci numbers below than 'last'
{
	int first=1; //fibonacci #2
	int second=2; //fibonacci #3
	int sum = 0; //keeps sum of even fibonacci
	
	for(int i=0;second<=last;i++)
	{
		if(second % 2 == 0) //controls even numbers
		{
			sum += second;
		}
		int temp = second;
		second += first;
		first = temp;
	}	
		
	return sum;
}




