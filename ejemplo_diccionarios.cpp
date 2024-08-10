#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    // Crear un diccionario (mapa) que asocia cadenas de texto (string) con enteros (int)
    map<string, int> diccionario;

    // Agregar elementos al diccionario
    diccionario["uno"] = 1;
    diccionario["dos"] = 2;
    diccionario["tres"] = 3;
    diccionario["cuatro"] = 4;

    // Acceder a un elemento del diccionario
    cout << "El valor de 'tres' es: " << diccionario["tres"] << endl;

    // Iterar sobre todos los elementos del diccionario
    cout << "Contenido del diccionario:" << endl;
    for (const auto& par : diccionario) {
        cout << par.first << ": " << par.second << endl;
    }

    // Buscar un elemento en el diccionario
    string clave = "dos";
    if (diccionario.find(clave) != diccionario.end()) {
        cout << "El valor de '" << clave << "' es: " << diccionario[clave] << endl;
    } else {
        cout << "La clave '" << clave << "' no se encuentra en el diccionario." << endl;
    }

    return 0;
}
