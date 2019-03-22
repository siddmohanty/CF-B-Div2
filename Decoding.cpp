#include<iostream>
#include <string.h>
using namespace std;
int main()
{
    int n;
    string s;
    cin>>n;
    cout<<"\n";
    cin>>s;
    string ns="";
    
    if(n%2!=0){
    for(int i=n-1;i>=0;i--)
    {
        if((n-1-i)%2==0)
        {
            ns+=s[n-1-i];
        }
        if((n-1-i)%2!=0)
        {
            ns=s[n-1-i]+ns;
        }
    }
    cout<<ns<<endl;
    return 0;
    }
    
    if(n%2==0)
    {
    for(int i=n-1;i>=0;i--)
    {
        if((n-1-i)%2!=0)
        {
            ns+=s[n-1-i];
        }
        if((n-1-i)%2==0)
        {
            ns=s[n-1-i]+ns;
        }
    }
    cout<<ns<<endl;
    return 0;
    }
    

}