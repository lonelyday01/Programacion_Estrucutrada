#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int secret_number = 7;
    int user_number = 0;

    cout << "Elija un numero del 1 al 10: ";
    cin >> user_number;

    while(user_number != secret_number)
    {
        cout << "Ese no es el numero secreto, intentalo de nuevo: ";
        cin >> user_number;
    }

    cout << "Felicidades! Has adivinado el numero secreto: 7!!";

}