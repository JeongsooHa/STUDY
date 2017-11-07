#include<stdlib.h>
#include<iostream>

using namespace std;

int main(int argc, char* argv[])
{
    cout << "Executing <some_script.hs>" << endl;
    system("./some_script.sh");
    return 0;
}
