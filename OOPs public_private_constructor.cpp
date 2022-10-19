#include<iostream>
#include<string>
using namespace std;
 class student{
    public:
    string name;
    int rollno;
    int marks;

    void study(){
        cout<<name<<"can study"<<endl;
    }
    student(string name, int rollno, int marks){
        this->name=name;
        this->rollno=rollno;
        this->marks=marks;
    }
    student(){

    }
 };
 int main(){
    student std1;
    std1.name="shakti ";
    std1.rollno=205;
    cout<<std1.name<<" "<<std1.rollno<<" "<<endl;
    std1.study();

    student std2;
    std2.name="shakti ";
    std2.rollno=205;
    cout<<std2.name<<" "<<std2.rollno<<" "<<endl;
    std2.study();

    student std3("shakti",205, 90);
    cout<<std3.name<<" "<<std3.rollno<<" "<<"\n"<<"marks "<<std3.marks<<endl;

 }
