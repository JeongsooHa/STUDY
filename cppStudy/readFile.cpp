#include <fstream>
#include <string>
#include <iostream>

using namespace std;

int main() 
{ 
    ifstream file("./OUTIMAGE.txt");
    //file.open("/Users/jeongsooha/git/STUDY/cppStudy/OUTIMAGE.txt");
    string str; 
    while (getline(file, str))
    {
        cout << str << endl;
    }
    return 0;
}
