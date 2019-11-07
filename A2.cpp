#include <iostream>
#include <vector>
using namespace std;
int main(int argc, char const *argv[])
{
	vector<int>v;
	cout<<"Enter character"<<endl;
	char ch;
	cin>>ch;
	int w = (int)ch;
	int b;
	cout<<"ASCII value of character is "<<w<<endl;
	while(w != 0)
	{
		b = w%2;
		v.push_back(b);
		w = w/2;
	}
	std::reverse(v.begin(), v.end());
	int i,j,k;
	int fs,gs,rs;
	fs = 0;
	int f[20];
	fs = v.size();
	for(i = 0;i<fs;i++)
	{
		f[i] = v[i];
	}
	cout<<"Frame entered is : "<<endl;
	for (int i = 0; i < fs; ++i)
	{
		cout<<f[i];
	}
	cout<<"\n";
	// cout<<"Enter Generator size"<<endl;
	// cin>>gs;
	int g[20];
	cout<<"Enter Int Generator"<<endl;
	int chr;
	cin>>chr;
	vector<int>v1;
	while(chr != 0)
	{
		b = chr%2;
		v1.push_back(b);
		chr = chr/2;
	}
	std::reverse(v1.begin(), v1.end());
	gs = v1.size();
	for (int i = 0; i < gs; ++i)
	{
		g[i] = v1[i];
	}
	cout<<"Generator entered is : "<<endl;
	for (int i = 0; i < gs; ++i)
	{
		cout<<g[i];
	}
	cout<<"\n";
	rs = gs - 1;
	cout<<"Number of zeros to be appended is"<<rs<<endl;
	int temp[20];
	for(i = fs;i<fs + rs;i++)
	{
		f[i] = 0;
	}
	for (int i = 0; i < 20; ++i)
	{
		/* code */
		temp[i] = f[i];
	}
	cout<<"Frame after appending zeros is : "<<endl;
	for (int i = 0; i < fs + rs; ++i)
	{
		/* code */
		cout<<temp[i];
	}
	cout<<"\n";
	for (int i = 0; i < fs; ++i)
	{
		k = i;
		j = 0;
		if (temp[k] >= g[j])
		{
			for ( j= 0, k = i;j < gs; j++,k++)
			{
				temp[k] = temp[k]^g[j];
			}
		}
	}

	int crc[20];
	for (int i = fs,j=0; i < fs+rs; ++i,++j)
	{
		crc[j] = temp[i];
	}
	cout<<"CRC is : "<<endl;
	for (int i = 0; i < rs; ++i)
	{
		cout<<crc[i];
	}
	cout<<"\n";
	int tf[20];
	for(i=0;i<fs;i++)
	{
		tf[i] = f[i];
	}
	for(int i =fs,j=0;i<fs + rs;i++,j++)
	{
		tf[i] = crc[j];
	}
	cout<<"Transmitted Frame is : "<<endl;
	for (int i = 0; i < fs+rs; ++i)
	{
		cout<<tf[i];
	}
	cout<<"\n";
	for (int i = 0; i < fs+rs; ++i)
	{
		temp[i] = tf[i];
	}
	for (int i = 0; i < fs; ++i)
	{
		k = i;
		j = 0;
		if(temp[k] >= g[j])
		{
			for (k=i,j=0; j<gs; ++j,++k)
			{
				temp[k] = temp[k]^g[j];
			}
		}
	}
	int rem[20];
	for (int i = fs,j=0; i < fs+rs; ++i,++j)
	{
		rem[j] = temp[i];
	}
	int flag = 0;
	for (int i = 0; i < rs; ++i)
	{
		if(rem[i]!=0)
		{
			flag = 1;
		}
	}
	if(flag == 1)
	{
		cout<<"Wrong"<<endl;
	}
	else
	{
		cout<<"Correct"<<endl;
	}
	return 0;
}