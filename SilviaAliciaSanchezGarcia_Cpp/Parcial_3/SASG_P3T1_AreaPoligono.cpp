#include <iostream>
using namespace std;

#include "SASG_P3T1_AreaPoligonosLibrary.h"

int main(){

    int lados = 0;
    int base = 0;
    int altura = 0;
    int perimetro = 0;
    int apotema = 0;

    cout << "Ingresa cuantos lados tiene tu poligono: ";
    cin >> lados;

    switch (lados)
    {
    case 3:
        cout << "Ingresa la base: ";
        cin >> base;
        cout << "Ingresa la altura: ";
        cin >> altura;

        cout << "El area de tu poligono es de: " << areaTresLados(base, altura);
        break;
    
    case 4:
        cout << "Ingresa la base: ";
        cin >> base;
        cout << "Ingresa la altura: ";
        cin >> altura;

        cout << "El area de tu poligono es de: " << areaCuatroLados(base, altura);
        break;

    case 5:
        cout << "Ingresa el perimetro: ";
        cin >> base;
        cout << "Ingresa el apotema: ";
        cin >> altura;

        cout << "El area de tu poligono es de: " << areaMuchosLados(perimetro, apotema);
        break;
    }
}