#include <bits/stdc++.h>
using namespace std;
int main()
{
	vector<int> k;
	int n, i, j, flag = 0;
	cin >> n;
	string a, b;
	char x, y;
	cin >> a;
	cin >> b;
	int l[26]={0}, m[26] = {0}, index;
	for (i = 0; i < n; i++)
	{
		l[a[i]-'a'] += 1;
		m[b[i]-'a'] += 1;
	}
	for (i = 0; i < 26; i++)
	{
		if (l[i] != m[i])
			flag = 1;
	}
	if (flag == 1)
		cout << "-1" << endl;

	else if (a == b)
		cout << "0" << endl;
	else 
	{
		for (i = 0; i < n; i++)
		{
			if (a[i] == b[i])
				continue;
			else 
			{
				for (j = i; j < n; j++)
				{
					if (a[j] == b[i])
					{
						index = j;
						break;
					}
				}
				x = a[i];
				y = a[index];
				a[i] = y;
				a[index] = x;
				for (j = i; j <= index; j++)
				{
					if (j != n-1)
						k.push_back(j+1);
				}
			}

		}
		cout << k.size() << endl;
		for (i = 0; i < k.size(); i++)
			cout << k[i] << " ";

	}
	
	return 0;
}

