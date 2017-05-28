//Project Euler #1
//Created : 28.2.2016
//Last Edit : 28.05.2017

#include <stdio.h>

int main()
{
  int sum = 0, sum15 = 0;

  for (int i = 0; i < 1000; i++) 
	{
		if (i % 3 == 0 || i % 5 == 0) 
			sum += i;
		else if (i % 15 == 0) //Used for eliminating repetitions
			sum15 += i;
	}
	
	
  printf("%d", sum - sum15);

  return 0;
}
