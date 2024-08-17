//
#include <iostream>
#include <map>
using namespace std;
string Romano(int numero);

int main()
{
    int numero;
    cout<<"*********************************"<<endl;
    cout<<"      DE ENTEROS A ROMANOS"<<endl;
    cout<<"*********************************"<<endl;
    cout<<"INGRESA UN NUMERO QUE NO EXCEDA 1001: "<<endl;
    cin >> numero;
    //sentencia que asegure que el numero sea menoa a 1001
    if(numero > 1001)
    {
        cout<<"ecxedes la limitante intenta otro numero: "<<endl;
        cin>> numero;
    }
    //se llama a la funcion para que se aplique la conbercion.
    string resultado = Romano(numero);
    cout<<"Tu numero es: "<<numero<<"a Romano es:"<<resultado<<endl;
    return 0;
}

string Romano(int numero)
{
    int resta = numero;
    string resultado = "";
    
    //se declara la funcion map
    map<int,string>rmo;
    rmo[1000] = "M";
    rmo[900] = "CM";
    rmo[500] = "D";
    rmo[400] = "CD";
    rmo[100] = "C";
    rmo[90] = "XC";
    rmo[50] = "L";
    rmo[40] = "XL";
    rmo[10] = "X";
    rmo[9] = "IX";
    rmo[5] = "V";
    rmo[4] = "IV";
    rmo[1] = "I";
    
    map<int, string>::reverse_iterator it = rmo.rbegin();
    
    while(it != rmo.rend())
    {
        if(resta >= it->first)
        {
            resultado = resultado + it->second;
            resta = resta - it->first;
        }else
        {
            it++;
        }
        
    }
    return resultado;
}