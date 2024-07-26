#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    for(int i = 0; i < 10; i += 1)
    {
        for(int j = 0; j < 10; j +=1)
        {
            cout << i+1 << " X " << j+1 << " = " << (i+1)*(j+1) << "\n";
        }
    }
}