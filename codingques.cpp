//Accenture Coding Test Questions and Answers
/*
Problem Description :
The Binary number system only uses two digits, 0 and 1 and number system can be called binary string. You are required to implement the following function:

int OperationsBinaryString(char* str);

The function accepts a string str as its argument. The string str consists of binary digits eparated with an alphabet as follows:

– A denotes AND operation
– B denotes OR operation
– C denotes XOR Operation
You are required to calculate the result of the string str, scanning the string to right taking one opearation at a time, and return the same.

Note:

No order of priorities of operations is required
Length of str is odd
If str is NULL or None (in case of Python), return -1
Input:
str: 1C0C1C1A0B1

Output:
1
*/
#include<bits/stdc++.h>
using namespace std;
int OperationsBinaryString (char *str)
{
  if (str == NULL)
    return -1;
  int i = 1;
  int a = *str - '0';
  str++;
  while (*str != '\0')
    {
      char p = *str;
      str++;
      if (p == 'A')
	a &= (*str - '0');
      else if (p == 'B')
	a |= (*str - '0');
      else
	a ^= (*str - '0');
      str++;
    }
  return a;
}
int main ()
{
  string s;
  getline (cin, s);
  int len = s.size ();
  char *str = &s[0];
  cout << OperationsBinaryString (str);
}
