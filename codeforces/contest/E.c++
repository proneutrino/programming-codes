#include <bits/stdc++.h>
using namespace std;
long int func (long int x,long int y)
{
	if (y == 0)
		return 0;
	else
		return 1+func(x,y-__gcd(x,y));
}
int main()
{
	long int x,y;
	scanf ("%ld%ld",&x,&y);
	printf ("%ld \n",func (x,y));
	return 0;
}
