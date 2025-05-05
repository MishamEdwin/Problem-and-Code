#include<iostream>
using namespace std;

class Students{
    string name;
    float math_mark,phys_mark,chem_mark,cutoff;

  public:
    Students(string name, float math_mark, float phys_mark, float chem_mark){
        this->name=name;
        this->math_mark=math_mark;
        this->phys_mark=phys_mark;
        this->chem_mark=chem_mark;

    }


    void cut(){
        cutoff=math_mark+phys_mark+chem_mark;
        cutoff=cutoff/3;
        cout<<cutoff  ;
    }

};


int main(){
    Students s1("chris",95.6,98,97);
    s1.cut();
    return 0;
}