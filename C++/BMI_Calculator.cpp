#include<iostream>
using namespace std;

int main()
{
 float bmi,weight,height;
  cout<<"Please Enter your weight in Kilograms : ";
  cin>>weight;
  cout<<"Please Enter your Height in Meters : ";
  cin>>height;
  bmi=(weight*703)/(height*height);
  cout<<"Your BMI is : "<<bmi<<endl;
  if(bmi>25)
    cout<<"Thus, you are overweight ";
  else if(bmi<25 && bmi>18.5)
    cout<<"This is the normal BMI.";
  else
    cout<<"Thus, you are underweight.";
  return 0;
}
