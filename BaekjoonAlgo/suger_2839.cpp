#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    int N=0;
    cin >> N;
    if(N<3 or N>5000){
        cout << -1 << endl;
        return 0;
    }
    if(N%5==0){
        cout << N/5 <<endl;
        return 0;
    }
    else{
        int n = N/5;
        for(int i = n; i>0; i--){
            int n5 = N - i*5;
            if(n5%3==0){
                cout << i+n5/3 << endl;
                return 0;
            }
        }
    }
    if(N%3==0)
        cout << N/3 << endl;
    else
        cout << -1 << endl;
    
}
