//Kevin Alejandro Parra Ramos  Ing.software  3er cuatrimestre 
#include <iostream>
float CalcArea(float longitud,float nlados);
using namespace std;
int main()
{
    float longitud,nlados;
    cout << "+++++++++++++++++++++++++++++++++++" << endl;
    cout << "  Calcula el area de un poligono" << endl;
    cout << "+++++++++++++++++++++++++++++++++++" << endl;
    cout << "ingresa el numero de loados de la figura:" << endl;
    cin >> nlados;
    cout <<"ingresa la longitud de cada lado:" << endl;
    cin >> longitud;
    cout << CalcArea(longitud,nlados) << endl;
    
}

float CalcArea(float longitud,float nlados)
{
    float area =  ((nlados * longitud) * 4.1 / 2);
    return area;
}