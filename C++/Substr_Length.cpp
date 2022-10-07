
#include<bits/stdc++.h>
using namespace std;

int main(){
    
    string s;
    cin>>s;
    map<char,int> m;
    int cur=0;
    int maxx=INT_MIN;
    for(int i=0;i<s.size();i++)
    {
        if(!m[s[i]])
        {
        m[s[i]]++;
        cur++;
        if(cur>maxx){
            maxx=cur;
            
        }
        }
        else{

            m.erase(m.begin(),m.end());
            m[s[i]]++;
            cur=1;
        }
      
    }  
    cout<<maxx;
    return 0;
} 
    
