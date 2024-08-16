#include <iostream>
#include <map>

using namespace std;

string enteroRomano(int numero);

int main(){
    int numero = 0;
    

    cout << "Ingresa un numero menor a 1001" << endl;
    cin >> numero;

    /*Revisar que se trate de un numero menor a 1001*/
    if(numero > 1001){
        cout << "Es un numero muy grande!!! Ingresa un numero MENOR a 1001" << endl;
        cin >> numero;
    }

    /*Se llama a la funcion que realiza la conversion y se almacena el resultado en una variable*/
    string respuesta = enteroRomano(numero);

    cout << "Tu numero " << numero << " en romano es: " << respuesta << endl;

}

string enteroRomano(int numero){
    int resta = numero;
    string resultado = "";

    /*Declaracion del map*/
    map<int, string> roman;
    /*Relleado del map*/
    roman[1000] = "M";
    roman[900] = "CM";
    roman[500] = "D";
    roman[400] = "CD";
    roman[100] = "C";
    roman[90] = "XC";
    roman[50] = "L";
    roman[40] = "XL";
    roman[10] = "X";
    roman[9] = "IX";
    roman[5] = "V";
    roman[4] = "IV";
    roman[1] = "I";

    /*Iterador que recorra el map desde el numero mayor al menor*/
    map<int, string>::reverse_iterator it = roman.rbegin();

    /*Ciclo que calcula el numero romano*/
    while(it != roman.rend()){
        if(resta >= it->first){
            resultado = resultado + it->second;
            resta = resta - it->first;
        }else{
            it++;
        }
                
    }

    return resultado;
}