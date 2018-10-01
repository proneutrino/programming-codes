#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	string s;
	cin >> n;
	cin >> s;
	int f = 0;
	int i;
	for (i=0;i<n-1;i++){
		if (s[i]== '?' ){
			if (i-1 >=0 && i+1<n){
			if (s[i-1]!=s[i+1] && s[i-1]!= '?' && s[i+1]!= '?')
				continue;
			else 
				f=1;
			}else{
				f=1;
			}
		}
	}
	if (f)
		cout<<"Yes"<<endl;
	else 
		cout<<"No"<<endl;
}
