#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n, i;
	string s;
	cin>>n;
	cin>>s;
	int f=0, ct=0;
	for (i=0;i<n;i++)
	{
		if (s[i]!='?'&&s[i]==s[i+1]){
			cout<<"no";
			return 1;
		}
		else {
			if(s[i]=='?')
			{
				if (i==0||i==n-1||s[i+1]=='?'){
					f=1;
				}else{
					if(s[i-1]!=s[i+1])
						continue;
					else 
						ct+=2;
				}
			}
		}
	}
	if(f==1||ct>=2)
		cout<<"Yes"<<endl;
	else 
		cout<<"No"<<endl;
	
}
