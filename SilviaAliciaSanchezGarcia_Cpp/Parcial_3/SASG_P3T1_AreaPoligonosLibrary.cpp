#include "SASG_P3T1_AreaPoligonosLibrary.h"


float areaTresLados(int base, int altura){
    return (base * altura)/2;
}

int areaCuatroLados(int base, int altura){
    return base * altura;
}

float areaMuchosLados(int perimetro, int apotema){
    return (perimetro * apotema)/2;
}

