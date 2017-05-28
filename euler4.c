//Project Euler #4
//Last Edit : 17.02.17

#include <stdio.h>

int palindrome(int x);

int main ()
{
	int ans = 0;
	int memory = 0;
	
	for(int i = 999; i >= 100; i--)
	{
		for(int j = 999; j >= 100; j--)
		{
			ans = i*j;
			if(ans != 0 & ans > memory)
				if(palindrome (i*j) == 1)
				{
					memory = ans;
				}
				
		}	
	}
	printf("%d" ,memory);
	
	return 0;
}

int palindrome(int x)
{
	
	int reverse = 0;
	int number = x;
	while(x>0) //Calculates reverse of the number
	{
		reverse = reverse*10 + x%10;
		x /= 10;
	}
	
	if(number == reverse)
		return 1;
	else
		return 0;
		
};

