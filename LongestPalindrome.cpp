#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm> 
#include<vector>
#include<stack>
#define ll long long
using namespace std;
 
bool checkPalindrome(string str, int size)
{
    //Check if a string is palindrome or not
    if(size==1)
    {
        return true;
    }
    int left=0;
    int right = size-1;
    while(left<right)
    {
        if(str[left]!=str[right]){
            return false;
        }
 
        left++;
        right--;
    }
    return true;
}
 
bool checkSymmetry(string str1, string str2, int size) 
{
    //To check if 2 strings are mirror image of each other
    int left = 0;
    int right = size-1;
    while(left<size)
    {
        if(str1[left] != str2[right])
        {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
 
 
int main()
{
    int n, m;
    cin>>n>>m;
    string arr[n];
    stack<string> leftStrings;
    stack<string> rightStrings;
    vector<string> middleStrings; //In case of middleStrings, we need the largest middle string
    vector<string> :: iterator it;
    string left, right, mid="";
    string solution = "";
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
 
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(checkSymmetry(arr[i],arr[j], m))
            {
                leftStrings.push(arr[i]);
                rightStrings.push(arr[j]);
            }
        }
        if (checkPalindrome(arr[i], m))
        {
            middleStrings.push_back(arr[i]);
        }
    }
 
    //Sort middleStrings vector in descending order of length
    if(middleStrings.size()!=0){
    sort(middleStrings.begin(), middleStrings.end());
    it = middleStrings.end()-1;
    mid = *it;
    }
    solution = mid;
 
    while(!leftStrings.empty())
    {
        left = leftStrings.top();
        right = rightStrings.top();
        leftStrings.pop();
        rightStrings.pop();
        if(left==right){
            right="";
        }
        solution = left+solution+right;   
    }
    cout<<solution.length()<<endl;
    cout<<solution<<endl;
    return 0;
}
