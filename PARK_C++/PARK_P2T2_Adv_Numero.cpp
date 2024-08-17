//Kevin Alejandro Parra Ramos  Ing.software  3er cuatrimestre 

#include <iostream>
using namespace std;

int main()
{
    srand(time(NULL));
    int num, ale = rand()%5;
    cout<<"+++++++++++++++++++++++++++++++++++++"<<endl;
    cout<<"      ADIVINA EL NUMERO OCULTO"<<endl;
    cout<<"+++++++++++++++++++++++++++++++++++++"<<endl;
    cout<<"Ingresa cualquier nuero del 0 al 5: "<<endl;
    cin >> num;
    while(num != ale)
    {
        cout<<"fallaste intenta de nuevo:"<<endl;
        cin>>num;
    }
    cout<<"has adivinado el numero oculto\n"<<ale<<endl;
}